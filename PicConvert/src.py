# -*- coding: utf-8 -*-
# @Time    : 2022/3/30 22:12
# @Author  : CYX
# @Email   : im.cyx@foxmail.com
# @File    : src.py
# @Software: PyCharm
# @Project : PicConvert

import os
import re
import json
import time
import uuid
import base64
import requests
import tenacity
from io import BytesIO
from requests_toolbelt.multipart.encoder import MultipartEncoder

from configs import CSDN_config, ZHIHU_config, BILI_config, JIANSHU_config, BOKEYUAN_config, Setting_config


class CSDNConvert(CSDN_config):
    """
    CSDN convert apply
    """
    def __init__(self, root):
        self.root = root

        def get_short_id():
            """
            get a uuid form array
            :return: uuid form short id
            """
            # support .jpg .gif .png .jpeg .bmp .webp, size less than 5 Mb
            array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                     "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                     "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                     "S", "T", "U", "V", "W", "X", "Y", "Z"]
            id_str = str(uuid.uuid4()).replace("-", '')
            buffer = []

            for i in range(0, 8):
                start = i * 4
                end = i * 4 + 4
                val = int(id_str[start:end], 16)
                buffer.append(array[val % 62])

            return "".join(buffer)

        self.fields.update({'uuid': 'img-' + get_short_id() + '-' + str(round(time.time() * 1000))})
    @tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4,
                                                   max=10),
                    stop=tenacity.stop_after_attempt(5),
                    reraise=True)
    def convert(self, src):
        # convert address
        if src.find('http') >= 0:
            self.fields.update({'imgUrl': src})
            payload = json.dumps(self.fields)
            res = requests.post(self.convert_url, data=payload, cookies=self.cookies, headers=self.headers)
        # upload imgs and get address
        else:
            self.up_headers['x-image-suffix'] = src.split('.')[-1]
            up_res = requests.get(self.up_url, cookies=self.cookies, headers=self.up_headers).json()
            # if request legal
            if up_res['code'] != 200:
                raise Exception(up_res['msg'])

            up_res = up_res['data']
            data = {
                'key': up_res['filePath'],
                'policy': up_res['policy'],
                'OSSAccessKeyId': up_res['accessId'],
                'signature': up_res['signature'],
                'callback': up_res['callbackUrl'],
                'file': open(os.path.join(self.root, src), 'rb').read()
            }
            multipart_encoder = MultipartEncoder(fields=data, boundary=self.boundary)
            res = requests.post(self.path_url, data=multipart_encoder, cookies=self.cookies, headers=self.path_headers)
        times = 0
        flag = False
        while True:
            try:
                times += 1
                time.sleep(5)
                # if request legal
                if res.json()['code'] != 200:
                    raise Exception(res.json()['msg'])
                res_url = res.json()['data']['url'] if src.find('http') >= 0 else res.json()['data']['imageUrl']
                flag = True
            except Exception as e:
                flag = False
                res_url = None
                time.sleep(5*(times+1))
            if flag or times > 5:
                break
        return res_url

class ZHIHUConvert(ZHIHU_config):
    """
    ZHIHU convert apply
    """
    def __init__(self):
        if self.mode not in self.mode_dict:
            raise Exception(" You enter a not support picture mode!")
    # 使用tenacity装饰器实现重试逻辑，配置指数退避等待时间和最大尝试次数
    @tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4,
                                                max=10),
                    stop=tenacity.stop_after_attempt(5),
                    reraise=True)
    def convert(self, src):
        """
        尝试转换给定的源数据，并返回转换后的URL。

        参数:
        src: 源数据，需要转换的数据。

        返回:
        转换后的URL，如果转换失败则返回None。
        """
        # 更新请求所需的字段
        self.fields['url'] = src
        # 创建multipart编码器，用于构建请求数据
        multipart_encoder = MultipartEncoder(fields=self.fields, boundary=self.boundary)
        # 发送POST请求以进行转换
        res = requests.post(self.convert_url, data=multipart_encoder, cookies=self.cookies, headers=self.headers)
        
        # 循环检查转换结果，直到成功或超过最大重试次数
        try:
            # if request legal
            if res.status_code != 200:
                raise Exception(res.json()['error']['message'])
            res_url = res.json()[self.mode]
        except Exception as e:
            res_url = None
            print("error", e)
        return res_url

class BILIConvert(BILI_config):
    def __init__(self, root):
        self.root = root
    @tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4,
                                                   max=10),
                    stop=tenacity.stop_after_attempt(5),
                    reraise=True)
    def convert(self, src):
        # concat data
        if src.find('http') >= 0:
            content = BytesIO(requests.get(src).content).read()
        else:
            content = open(os.path.join(self.root, src), 'rb').read()
        self.fields['cover'] = self.b64_head + str(base64.b64encode(content))[2:-1]

        res = requests.post(self.convert_url, data=self.fields, cookies=self.cookies, headers=self.headers)
        # if request legal
        if res.json()['code'] != 0:
            raise TypeError(res.json()['message'])
        res_url = res.json()['data']['url']

        return res_url

class JIANSHUConvert(JIANSHU_config):
    def __init__(self, root):
        self.root = root
        requests.get('https://www.jianshu.com/', cookies=self.cookies)

    def convert(self, src):
        # concat data
        payload = requests.get(self.token_url + src.split('.')[-1], headers=self.headers, cookies=self.cookies).json()

        if src.find('http') >= 0:
            payload['file'] = requests.get(src, headers=self.headers).content
        else:
            payload['file'] = open(os.path.join(self.root, src), 'rb').read()
        payload['x:protocol'] = 'https'
        multipart_encoder = MultipartEncoder(fields=payload, boundary=self.boundary)

        # request
        res = requests.post(self.convert_url, data=multipart_encoder, headers=self.headers)
        # if request legal
        if res.status_code != 200:
            raise Exception(res.json()['error'])
        res_url = res.json()['url']

        return res_url

class BOKEYUANConvert(BOKEYUAN_config):
    def __init__(self, root):
        self.root = root

    def convert(self, src):
        # concat data
        if src.find('http') >= 0:
            self.fields['imageFile'] = (src, requests.get(src).content, 'image/png')
        else:
            self.fields['imageFile'] = (src, open(os.path.join(self.root, src), 'rb').read(), 'image/png')
        multipart_encoder = MultipartEncoder(fields=self.fields, boundary=self.boundary)

        # request
        requests.options(self.convert_url)
        res = requests.post(self.convert_url, data=multipart_encoder, headers=self.headers, cookies=self.cookies)

        if not res.json()['success']:
            raise Exception(res.json()['message'])

        # if request legal
        res_url = res.json()['message']
        return res_url

def img_convert(mode, text, root, link=False):
    """
    根据指定的平台模式将文本中的图片转换为在线链接或处理后的文本。
    
    参数:
    - mode: str, 平台模式，例如 'zhihu', 'csdn' 等。
    - text: str, 包含需要转换图片的文本。
    - root: str, 文件操作的根目录。
    - link: bool, 是否仅返回图片链接，默认为 False。
    
    返回:
    - str, 转换后的文本或图片链接。
    """
    # 根据模式选择相应的平台转换器
    if mode == 'zhihu':
        handle = ZHIHUConvert()
    elif mode == 'csdn':
        handle = CSDNConvert(root)
    elif mode == 'bili':
        handle = BILIConvert(root)
    elif mode == 'jianshu':
        handle = JIANSHUConvert(root)
    elif mode == 'bokeyuan':
        handle = BOKEYUANConvert(root)

    # 如果仅需要图片链接
    if link:
        res_url = handle.convert(text)
        # 如果获取到有效的转换地址
        if res_url:
            print(f"-> {res_url}")
        else:
            print(Exception('Convert false!'))
            res_url = src
        return res_url

    else:
        res_text = ''
        # 如果 example.md 存在，读取其内容作为初始转换文本
        if os.path.exists('example.md'):
            with open('example.md', 'r', encoding='utf-8') as f:
                res_text += f.read()
        last_end = 0
        # 查找文本中的所有模式并替换为转换后的图片
        for query in re.finditer(Setting_config.pattern, text, re.I):
            src = query.group()[2:-1]
            print(f"{src}", end=' ')
            try:
                res_url = handle.convert(src)
                # 如果获取到有效的转换地址
                if res_url:
                    print(f"-> {res_url}")
                else:
                    res_url = src
            except Exception as e:
                print(f"转换出现问题: {e}，使用原始地址")
                res_url = src
            # 更改源文件，然后进行另一次搜索
            res_text += text[last_end:query.start() + 2] + res_url
            last_end = query.end() - 1
        res_text += text[last_end:]

        return res_text