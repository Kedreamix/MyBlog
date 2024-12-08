import os
from configs import root_path
from chatgpt import gpt_35_api_stream
import google.generativeai as genai
import time
# from chatpaperfree import Paper, Reader
from chat_paper import Paper, Reader
from configs import *
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


def chatpaper_summary(file):
    paper_list = [Paper(path=file)]
    reader = Reader(key_word="",
                         query="",
                         filter_keys="",
                        #  chatgpt_model='gpt-3.5-turbo',
                        chatgpt_model="ernie"
                         )
    reader.show_info()
    sum_info = reader.summary_with_chat(paper_list=paper_list)
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


def validate_result(result, task_type='summary', custom_keywords=None):
    """
    验证结果中是否包含指定关键字，并返回不包含关键字的部分.

    :param result: 待验证的文本结果
    :param task_type: 任务类型 ('summary' 或 'translate')
    :param custom_keywords: 自定义关键词列表（可选）
    :return: 不包含关键字的部分文本
    :raises Exception: 如果未找到匹配的关键词
    """

    # 设置关键词列表
    if custom_keywords is not None:
        keywords = custom_keywords
    elif task_type == 'summary':
        keywords = ['**Summary', 'Summary', '总结', '摘要', '**摘要', '**总结']
    elif task_type == 'translate':
        keywords = ['**Translation', 'Translation', '翻译', '译文', '**译文', '**翻译']
    else:
        raise ValueError(f"Unknown task_type: {task_type}")

    # 检查关键词是否存在
    if not any(keyword in result for keyword in keywords):
        logger.error(f"Error: did not find expected keywords in result. Task: {task_type}, Result: {result}")
        raise Exception(f"{task_type} error: Keywords not found")

    # 动态匹配关键词，并排除关键词本身
    keyword_pattern = '|'.join(re.escape(kw) for kw in keywords)
    match = re.search(rf'\*?\*?(?:{keyword_pattern})(.*)', result, re.DOTALL)

    if match:
        if task_type == 'translate':
            # 返回不包含关键词的部分
            return match.group(1).strip().strip('*').strip('\n')
        else:
            return match.group()
    else:
        logger.error(f"Error: failed to parse {task_type} result: {result}")
        raise Exception(f"{task_type} parsing error")


@tenacity.retry(
    wait=tenacity.wait_exponential(multiplier=3, min=4, max=40),
    stop=tenacity.stop_after_attempt(10),
    reraise=True
)
def gpt_gen(system_prompt, prompt, method='chatglm', key_name=''):
    # 
    result = None
    message = system_prompt % (key_name, prompt)

    if method == 'chatgpt':
        messages = [{'role': 'user', 'content': message}]
        response = gpt_35_api_stream(messages)
        result = response[2]['content']

    elif method == 'gpt4free':
        from g4f.client import Client
        messages = [
            {"role": "system", "content": f"You are a researcher in the field of [{key_name}] who is good at summarizing papers using concise statements"},
            {'role': 'user', 'content': message}
        ]
        client = Client()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            provider=g4f.Provider.Liaobots
        )
        result = response.choices[0].message.content

    elif method == 'ernie':
        url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie-speed-128k?access_token={access_token}"
        payload = json.dumps({
            "messages": [{"role": "user", "content": message}],
            "system": f"You are a researcher in the field of [{key_name}] who is good at summarizing papers using concise statements"
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=payload)
        result = response.json().get('result', '')

    elif method == 'chatglm':
        messages = [
            {"role": "system", "content": f"You are a researcher in the field of [{key_name}] who is good at summarizing papers using concise statements"},
            {'role': 'user', 'content': message}
        ]
        client = ZhipuAI(api_key="your_api_key_here")
        response = client.chat.completions.create(
            model="glm-4-flash",
            messages=messages
        )
        result = response.choices[0].message.content

    if 'sorry' in result.lower():
        raise Exception(f"{method} error: 'sorry' found in response")

    if 'translate' in system_prompt.lower():
        return validate_result(result, task_type='translate')
    else:
        return validate_result(result, task_type='summary')

@tenacity.retry(wait=tenacity.wait_exponential(multiplier=2, min=4, max=20),  # 增加 multiplier 和 max
                    stop=tenacity.stop_after_attempt(10),
                    reraise=True)
def typing(item, img_dir, key_name, daily=False):
    url_id, updated, published, title, summary, authors, categorys, comments = item
    auth = ''
    for a in authors:
        auth = auth + a + ', '
    auth = auth[:-2]
    
    gpt_translate = gpt_gen(translate_prompt, summary, 'ernie', key_name)

    gpt_summary = gpt_gen(summary_prompt, summary, 'ernie', key_name)


    # logger.info("gptsummary1:\n{}".format(gptsummary1))
    if daily:
        save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d") + '-daily')
    else:
        save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))
    pdfname = check_filename(title)
    arxiv_id = os.path.basename(url_id)
    
    save_path = os.path.join(save_dir, arxiv_id + '_' + pdfname + ".pdf")

    if not daily:        
        gptsummary2 = chatpaper_summary(save_path)
        # logger.info("gptsummary2:\n{}".format(gptsummary2))
            

    # time.sleep(5)
    img = set_img(img_dir)
    if daily:
        dsc = f'''
## {title}

**Authors:{auth}**

{summary.lstrip()}

>{gpt_translate}

**论文及项目相关链接**

[PDF]({url_id}) {comments[0] if len(comments) > 0 else ''}

{gpt_summary}

{img}


'''
    else:
        
        dsc = f'''
## {title}

**Authors:{auth}**

{summary.lstrip()}

>{gpt_translate}

**论文及项目相关链接**

[PDF]({url_id}) {comments[0] if len(comments) > 0 else ''}

{gpt_summary}

**[ChatPaperFree](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)**

{gptsummary2}

{img}

'''
    return dsc
