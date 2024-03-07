import os
import requests
from PIL import Image
import google.generativeai as genai

def configure_api(api_key, proxy_url=None):
    os.environ['https_proxy'] = proxy_url if proxy_url else ''
    os.environ['http_proxy'] = proxy_url if proxy_url else ''
    genai.configure(api_key=api_key)

def generate_content(message, imgs, method='api', api_key=None, proxy_url=None):
    if method != 'api':
        configure_api(api_key, proxy_url)
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([message] + imgs, stream=True)
        response.resolve()
        response = response.text
    else:
        url = f"https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        data = {'prompt': {'text': message}}
        
        response = requests.post(url, headers=headers, json=data, proxies={'http': proxy_url, 'https': proxy_url}).json()
        try:
            response = response['candidates'][0]['output']
        except KeyError:
            print(response)
            response = None 

    return response

if __name__ == '__main__':
    GOOGLE_API_KEY = 'AIzaSyBdQdkgDbYAcjeTs-eB4Wog_CZCLhnJwFk'
    PROXY_URL = 'http://127.0.0.1:7890'  # Replace with your proxy URL

    vision_prompt = '''
    These images correspond to the paper. Please describe in Chinese what you have learned from these papers, including the methods used, results obtained, benefits, and innovations.

    Some points you can touch upon in your Chinese description:

    The research methods and techniques employed in the paper
    The types of data and results generated
    Key conclusions drawn from analysis and comparisons
    Any innovative aspects of the methods or approaches used
    The contributions of this work to the relevant field of study or research
    Provide a brief but comprehensive overview in Chinese of the above details regarding the paper's research methodology, findings, and significance. Understanding the methods and outcomes of papers can be helpful for our learning. Thank you for the description.
    '''

    folder = r'D:\workdirs\AutoFX\arxiv\2023-12-14\crop_Audio Driven Generation\2301.03786v2'
    img_paths = [os.path.join(folder, f) for f in os.listdir(folder)]

    content = generate_content(vision_prompt, img_paths, method='api', api_key=GOOGLE_API_KEY, proxy_url=PROXY_URL)
    print(content)
