import os
import datetime
import time
import re
import json


def update_cover():
    root_cover = r'C:\Backup\blogs\public'
    # /home/ubuntu/blogs/public/2022/03/31
    years = []
    for t in os.listdir(root_cover):
        if t.isnumeric(): years.append(t)

    dir_y = os.path.join(root_cover, sorted(years)[-1])
    dir_M = os.path.join(dir_y, sorted(os.listdir(dir_y))[-1])
    dir_d = os.path.join(dir_M, sorted(os.listdir(dir_M))[-1])
    path_ds = [os.path.join(dir_d, f) for f in os.listdir(dir_d)]
    tmps = []
    for d in path_ds:
        url = d[len(root_cover):]
        url = url.replace("\\", "/")
        ff = open(os.path.join(d, 'index.html'), 'r', encoding='utf8')
        ss = ff.read()
        title = re.findall(r'<h1 class="description center-align post-title">(.*?)</h1>', ss, re.UNICODE)[0]
        cover_img = re.findall(r'''background-image: url\(\'(.*?)\'\)''', ss, re.UNICODE)[0]
        summary_date = re.findall(r'''<h1 id=\"(.*?)\">''', ss, re.UNICODE)[0]
        summary_title = re.findall(r'''<h3 id=\"(.*?)\">''', ss, re.UNICODE)[0]
        ff.close()
        cover = {'title': title,
                 'path': url,
                 'coverImg': cover_img,
                 'summary': summary_date.strip() + ' ' + summary_title.strip()}
        tmps.append(cover)
    return tmps


if __name__ == '__main__':
    tmp = update_cover()
    ss = json.dumps(tmp, ensure_ascii=False, indent=3)
    f = open(r'C:\Backup\blogs\source\_data\covers.json', 'w', encoding='utf8')
    f.write(ss)
    f.close()
