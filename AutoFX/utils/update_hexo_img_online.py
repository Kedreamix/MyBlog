import os
import sys
import shutil
import datetime
from configs import root_blog, root_blog_images
from utils.union import check_filename
from utils.image_uploader import upload
import glob
import time
import re


def generate_header(title, path_bg):
    tag = ''
    for t in title.split('/'):
        tag = tag + f'  - {t}\n'
    top = f'''
---
title: {title}
date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
author: 木子已
img: {path_bg}
cover: true
coverImg: {path_bg}
mathjax: true
categories: {title}
tags:
{tag}
---
# {datetime.datetime.now().strftime("%Y-%m-%d")} 更新
'''
    return top


def refresh_md(content, path_md):
    pattern = re.compile(r'<img src="(.*?)" align="middle">')
    path_img_dir = os.path.dirname(path_md)

    res = pattern.findall(content)
    for i, fpath in enumerate(res):
        cpy = fpath
        if fpath.startswith("http"): continue
        fpath = fpath.replace("./", "")
        fpath = fpath.replace("/", "\\")
        path_img = os.path.join(path_img_dir, fpath)
        if not os.path.exists(path_img): exit(1)
        img_url = upload(path_img)
        # 报错，则循环等待上传
        while img_url.startswith("error"):
            print(img_url)
            time.sleep(15)
            img_url = upload(path_img)
        # 替换原来文本
        content = content.replace(cpy, img_url)
    return content


def control_blog(title, path_md, root_img):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = now + '_' + check_filename(title)

    path_imgs = glob.glob(os.path.join(root_img, '*', '*.jpg'))
    if len(path_imgs) > 0:
        path_bg = upload(path_imgs[0])
    else:
        path_bg = '/images/bg.png'

    content = ''
    target_path_md = os.path.join(root_blog, filename + '.md')
    if os.path.exists(target_path_md):
        with open(target_path_md, 'r', encoding='utf-8') as f:
            content = f.read()
            content = content.split('---')[2]
    with open(path_md, 'r', encoding='utf-8') as f:
        text = f.read()
        header = generate_header(title, path_bg)
        if content != '':
            md = header + '\n' + text + '\n' + content
        else:
            md = header + '\n' + text
    md = refresh_md(md, path_md)
    with open(target_path_md, 'w', encoding='utf-8') as f:
        f.write(md)


if __name__ == '__main__':
    # 2018-09-07 09:25:00
    img_list = os.listdir(r'D:\MyWork\AutoFX\arxiv\2022-02-14\crop_无监督_半监督_对比学习\2202.05830v1')
    print(img_list)
    print(sorted(img_list))
    pass
