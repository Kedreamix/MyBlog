import os

import requests

url = "https://api.superbed.cn/upload"
token = "d1395ee466b34bfa8cb8c60e67d78309"


def upload(path):
    assert os.path.exists(path)
    resp = requests.post(url, data={"token": token}, files={"file": open(path, "rb")})
    resp = resp.json()
    if resp['err'] == 0:
        return resp['url']
    else:
        return 'error:' + resp['msg']


if __name__ == '__main__':
    path_file = r'C:\Backup\blogs\source\_posts\2022-02-23_检测_分割_跟踪\crop_检测_分割_跟踪\2110.14223v2\page_0_0.jpg'
    resp = upload(path_file)
    print(resp)
