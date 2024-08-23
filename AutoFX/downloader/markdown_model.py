import os
from configs import root_path
from chatgpt import gpt_35_api_stream
import google.generativeai as genai
import time
# from chatpaperfree import Paper, Reader
from chat_paper import Paper, Reader
from configs import GOOGLE_API_KEY, summary_prompt, proxy_gpt
import random
import tenacity
import g4f
import json, requests
from loguru import logger
import re
def check_filename(title):
    pdfname = title.replace("/", "_")  # pdf名中不能出现/和：
    pdfname = pdfname.replace("?", "_")
    pdfname = pdfname.replace("\"", "_")
    pdfname = pdfname.replace("*", "_")
    pdfname = pdfname.replace(":", "_")
    pdfname = pdfname.replace("\n", "")
    pdfname = pdfname.replace("\r", "")
    pdfname = pdfname.replace("  ", " ")
    if len(pdfname) > 130:
        pdfname = pdfname[:125]
    return pdfname

# def chatpaper_summary(file, p=1, temperature=0.5):
#     text = '''Abstract,Introduction,Related Work,Background,Preliminary,Problem Formulation,Methods,Methodology,Method,Approach,Approaches,Materials and Methods,Experiment Settings,Experiment,Experimental Results,Evaluation,Experiments,Results,Findings,Data Analysis,Discussion,Results and Discussion,Conclusion,References'''
#     section_list = text.split(',')
#     paper_list = [Paper(path=file, sl=section_list)]
#     # 创建一个Reader对象
#     api_key_list = ['AIzaSyDwlS-8OQvtPlwsGxZetRosm8Gebp342Vk',
#                     ]
#     if random.random() < 0.5:
#         api_key_list = api_key_list[::-1]
#     random.shuffle(api_key_list)
#     reader = Reader(api_keys=api_key_list,
#                     model_name='gemini-Pro',
#                     p=p,
#                     temperature=temperature)
#     sum_info, cost = reader.summary_with_chat(
#         paper_list=paper_list)  # type: ignore  
#     return sum_info 

def chatpaper_summary(file):
    # if sort == 'Relevance':
    #     sort = arxiv.SortCriterion.Relevance
    # elif sort == 'LastUpdatedDate':
    #     sort = arxiv.SortCriterion.LastUpdatedDate
    # else:
    #     sort = arxiv.SortCriterion.Relevance
    paper_list = []
    paper_list.append(Paper(path=file))
    reader1 = Reader(key_word="",
                         query="",
                         filter_keys="",
                        #  chatgpt_model='gpt-3.5-turbo',
                        chatgpt_model="ernie"
                         )
    reader1.show_info()
    sum_info = reader1.summary_with_chat(paper_list=paper_list)
    return sum_info
    
def set_detail(summary, content):
    content = content.strip()
    s = f'''
<details>
  <summary>{summary}</summary>
{content}
</details>

'''
    return s


def set_img(path_img_dir):
    files = os.listdir(os.path.abspath(path_img_dir))
    if len(files) == 0:
        return ''
    s = ''
    path_img_dir = path_img_dir.replace('\\', '/')
    prefix = path_img_dir.split('/')[-2] + '/' + path_img_dir.split('/')[-1]
    files = sorted(files)
    for f in files:
        s = s + f'<img src="./{prefix}/{f}" align="middle">\n'
    return set_detail('点此查看论文截图', s)

def get_access_token(api_key, secret_key):
    """
    使用 API Key 和 Secret Key 获取access_token。
    :param api_key: 应用的API Key
    :param secret_key: 应用的Secret Key
    :return: access_token
    """
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"
    
    response = requests.post(url, headers={'Content-Type': 'application/json'})
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception("获取 access_token 失败")
    
from configs import api_key, secret_key
access_token = get_access_token(api_key, secret_key)

@tenacity.retry(wait=tenacity.wait_exponential(multiplier=2, min=4, max=20),  # 增加 multiplier 和 max
                    stop=tenacity.stop_after_attempt(10),
                    reraise=True)
def gpt_gen(prompt, method='gemini', key_name=''):
    if method=='chatgpt':
        messages = [{'role': 'user','content': prompt},]
        
        message = summary_prompt % (key_name, prompt)
        messages = [{'role': 'user','content': message},]

        answer = gpt_35_api_stream(messages)
        response = answer[2]['content']
        
        return response
    elif method == 'gpt4free':
        from g4f.client import Client
        message = summary_prompt % (key_name, prompt)
        messages = [
            {"role": "system",
             "content": "You are a researcher in the field of [" + key_name + "] who is good at summarizing papers using concise statements"},
            {'role': 'user','content': message},]
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = messages,
            provider=g4f.Provider.Liaobots
        )
        response = response.choices[0].message.content
        if 'sorry' in response:
            raise Exception("gpt4free error")
        result = response
        if not any(keywork not in result for keywork in ['**Summary', 'Summary', '总结', '摘要', '**摘要', '**总结']):
            logger.error(f"error, didn't find Summary {result}")
            raise Exception("ernie error")

        # match = re.search(r'\*\*Summary(.*)', result, re.DOTALL)
        # 合并对 "Summary"、"总结" 和 "摘要" 以及其加粗形式的匹配
        match = re.search(r'\*?\*?(?:Summary|总结|摘要).*', result, re.DOTALL)

        if match:
            return match.group()
        else:
            logger.error(f"error, didn't find **Summary** {result}")
            raise Exception("summary error")
            return response
    elif method == 'ernie':
        message = summary_prompt % (key_name, prompt)
        url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token={access_token}"
        # message_content = messages[1]['content'] + messages[2]['content']
        payload = json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ],
            "system": "You are a researcher in the field of [" + key_name + "] who is good at summarizing papers using concise statements"
            })
        headers = {'Content-Type': 'application/json'}
        
        response = requests.post(url, headers=headers, data=payload)
        response_json = response.json()
        result = response_json['result']
        if not any(keywork not in result for keywork in ['**Summary', 'Summary', '总结', '摘要', '**摘要', '**总结']):
            logger.error(f"error, didn't find Summary {result}")
            raise Exception("ernie error")

        # match = re.search(r'\*\*Summary(.*)', result, re.DOTALL)
        # 合并对 "Summary"、"总结" 和 "摘要" 以及其加粗形式的匹配
        match = re.search(r'\*?\*?(?:Summary|总结|摘要).*', result, re.DOTALL)

        if match:
            return match.group()
        else:
            logger.error(f"error, didn't find **Summary** {result}")
            raise Exception("summary error")
            # print(result)
    elif method == 'gemini':
        message = summary_prompt % (key_name, prompt)
        os.environ['https_proxy'] = proxy_gpt['https']
        os.environ['http_proxy'] = proxy_gpt['http']
        genai.configure(api_key=GOOGLE_API_KEY)
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]
        times = 0
        flag = False
        while True:
            try:
                times += 1
                print("Try times", times)
                model = genai.GenerativeModel('gemini-pro', 
                                              safety_settings=safety_settings)
                response = model.generate_content(message)
                # response = response.text
                flag = True
            except Exception as e:
                time.sleep(5)
                print("error", e)
                flag = False
            
            if times > 5 or flag:
                break
                
                
        response = response.text
        return response

@tenacity.retry(wait=tenacity.wait_exponential(multiplier=2, min=4, max=20),  # 增加 multiplier 和 max
                    stop=tenacity.stop_after_attempt(10),
                    reraise=True)
def typing(item, img_dir, key_name, daily=False):
    url_id, updated, published, title, summary, authors, categorys, comments = item
    # print(item)
    auth = ''
    for a in authors:
        auth = auth + a + ', '
    auth = auth[:-2]
    # try:
    #     gptsummary1 = gpt_gen(summary, 'chatgpt', key_name)
    # except:
    #     gptsummary1 = gpt_gen(summary, 'gemini', key_name)
    try:
        gptsummary1 = gpt_gen(summary, 'gpt4free', key_name)
    except:
        gptsummary1 = gpt_gen(summary, 'ernie', key_name)

    logger.info("gptsummary1:\n{}".format(gptsummary1))
    if daily:
        save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d") + '-daily')
    else:
        save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))
    pdfname = check_filename(title)
    arxiv_id = os.path.basename(url_id)
    
    save_path = os.path.join(save_dir, arxiv_id + '_' + pdfname + ".pdf")

    if not daily:        
        gptsummary2 = chatpaper_summary(save_path)
        logger.info("gptsummary2:\n{}".format(gptsummary2))
            

    # time.sleep(5)
    img = set_img(img_dir)
    if daily:
        dsc = f'''
## {title}

**Authors:{auth}**

{summary.lstrip()}

[PDF]({url_id}) {comments[0] if len(comments) > 0 else ''}

{gptsummary1}

{img}


'''
    else:
        
        dsc = f'''
## {title}

**Authors:{auth}**

{summary.lstrip()}

[PDF]({url_id}) {comments[0] if len(comments) > 0 else ''}

{gptsummary1}

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

{gptsummary2}

{img}

'''
    return dsc
