import textwrap
import google.generativeai as genai
import requests
from IPython.display import Markdown
from google.ai import generativelanguage as glm
import pprint

def configure_api(api_key, proxy_url=None):
    import os
    os.environ['https_proxy'] = proxy_url if proxy_url else ''
    os.environ['http_proxy'] = proxy_url if proxy_url else ''
    genai.configure(api_key=api_key)


def googleapi(message, method='api', api_key=None, proxy_url=None):
    if method == 'code':
        configure_api(api_key, proxy_url)
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
        model = genai.GenerativeModel('gemini-1.0-pro', safety_settings=safety_settings)
        # model = genai.GenerativeModel('gemini-1.5-pro-latest', safety_settings=safety_settings)
        # model = genai.get_tuned_model('tunedModels/gemini-pro')
        # pprint.pprint(model)
        response = model.generate_content(message)
        # text_token = model.count_tokens("hello")
        # print("Used {} tokens".format(text_token))

        try:
            response = response.text
        except Exception as e:
            print(f'{type(e).__name__}: {e}')
            response = None
    elif method == 'api':
        url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'
        headers = {'Content-Type': 'application/json'}

        data = {
            'contents': [
                {
                    'parts': [
                        {
                            'text': message
                        }
                    ]
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data, params={'key': api_key}).json()
        # print(response)
        try:
            response = response['candidates'][0]['content']['parts'][0]['text']
        except Exception as e:
            print(f'{type(e).__name__}: {e}')
            response = None

    return response


if __name__ == '__main__':
    api_key_list = ['AIzaSyA_uN9Ydd2ukKkP-FLoxY6nby1Ui5UFGgI',
                    'AIzaSyCJkNYVfofB3E6bBulTbwjkGHQENWu8VBQ',
                    # 'AIzaSyASdOyjqMbXQWi0h4xnGuKNWtovH6vrEmk',
                    ]
    GOOGLE_API_KEY = 'AIzaSyDwlS-8OQvtPlwsGxZetRosm8Gebp342Vk'
    
    # GOOGLE_API_KEY = api_key_list[1]
    # GOOGLE_API_KEY = 'AIzaSyCWiiXeTYLDm37lBbl8vgmucR_YlsG2LD8'
    PROXY_URL = 'http://127.0.0.1:7890'  # Replace with your proxy URL

    text = 'Audio-driven talking head generation has drawn much attention in recent years, and many efforts have been made in lip-sync, expressive facial expressions, natural head pose generation, and high video quality. However, no model has yet led or tied on all these metrics due to the one-to-many mapping between audio and motion. In this paper, we propose VividTalk, a two-stage generic framework that supports generating high-visual quality talking head videos with all the above properties. Specifically, in the first stage, we map the audio to mesh by learning two motions, including non-rigid expression motion and rigid head motion. For expression motion, both blendshape and vertex are adopted as the intermediate representation to maximize the representation ability of the model. For natural head motion, a novel learnable head pose codebook with a two-phase training mechanism is proposed. In the second stage, we proposed a dual branch motion-vae and a generator to transform the meshes into dense motion and synthesize high-quality video frame-by-frame. Extensive experiments show that the proposed VividTalk can generate high-visual quality talking head videos with lip-sync and realistic enhanced by a large margin, and outperforms previous state-of-the-art works in objective and subjective comparisons. The code will be publicly released upon publication.'  # Your long text here

    summary_prompt = '''
    User
    Ignore all previous instructions. You are a highly proficient researcher that can read and write properly and fluently, and can extract all important information from any text. Your task is to summarize and extract all key takeaways of the following text delimited by triple backticks in all relevant aspects.

    Output a summary and a list of key takeaways respectively. The summary should be a one-liner in at most 100 words. The key takeaways should be in up to seven bulletpoints, the fewer the better.

    Use the following format:
    ### Summary
    <summary of the text>

    ### Key Takeaways
    <list of key takeaways>

    Respond in Simplified Chinese.


    Text:
    ```
    %s
    ```
    '''

    question = summary_prompt % text
    print('Method: Code', '-'*50)
    content = googleapi(question, method='code', api_key=GOOGLE_API_KEY, proxy_url=PROXY_URL)
    
    print(content)
    print('Method: API', '-'*50)
    content = googleapi(question, method='api', api_key=GOOGLE_API_KEY, proxy_url=PROXY_URL)
    print(content)    