import requests
import json
from configs import proxy

def deepl_trans(word):
    url = 'https://api-free.deepl.com/v2/translate'
    # 使用post需要一个链接
    data = {'auth_key': '5911d39c-6c3b-f87b-b85a-07b03188d794:fx',
            'text': word,
            'target_lang': 'ZH'}

    r = requests.post(url, data, proxies=proxy, verify=False)
    answer = json.loads(r.text)
    result = answer['translations'][0]['text']
    return result

if __name__ == '__main__':
    result = deepl_trans("The DeepL API is an interface that allows other computer programs to send texts to our servers and receive high-quality translations. This opens a whole universe of opportunities for developers worldwide: Any translation product you can imagine can now be built on top of DeepL's superior translation technology.")
    print(result)