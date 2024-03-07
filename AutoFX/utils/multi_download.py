import time

import requests
from tqdm import tqdm
from configs import proxy, proxy_gpt


def download(url: str, file_name: str, desc: str):
    # 请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    time.sleep(16)
    try:
        response = requests.get(url, headers=headers, stream=True, proxies=proxy_gpt, verify=False)
        file_size = response.headers['Content-Length']  # 文件大小，以 B 为单位
        chunk_size = 1024 * 256
        bar = tqdm(total=int(file_size), ascii=True, desc=desc)
        with open(file_name, mode='wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                bar.update(chunk_size)
        bar.close()
        return True
    except:
        return False


if "__main__" == __name__:
    url = 'https://arxiv.org/pdf/2107.01063.pdf'
    file_name = '2107.01063.pdf'
    download(url, file_name)
