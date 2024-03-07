import requests
import string
import time
import hashlib
import json
import re
import numpy as np

api_url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
my_appid = '20210131000686767'  # 你的APP ID
cyber = 'nM7XJHAryHZdoS2WnMaY'  # 你的秘钥
lower_case = list(string.ascii_lowercase)


def baidu_translate(word):
    # init salt and final_sign
    salt = str(time.time())[:10]
    final_sign = str(my_appid) + word + salt + cyber
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()
    # 区别en,zh构造请求参数
    paramas = {
        'q': word,
        'from': 'en',  # 源语言
        'to': 'zh',  # 目标语言
        'appid': '%s' % my_appid,
        'salt': '%s' % salt,
        'sign': '%s' % final_sign
    }  # 翻译请求参数
    my_url = api_url + '?appid=' + str(
        my_appid) + '&q=' + word + '&from=' + 'en' + '&to=' + 'spa' + '&salt=' + salt + '&sign=' + final_sign
    response = requests.get(api_url, params=paramas).content
    content = str(response, encoding="utf-8")
    json_reads = json.loads(content)
    return json_reads['trans_result'][0]['dst']


if __name__ == '__main__':
    result = baidu_translate("hello")
    print(result)