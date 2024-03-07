import os
import sys
import shutil
import datetime
from configs import root_blog, root_blog_images
from utils.union import check_filename
import glob
import time


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


def control_blog(title, path_md, root_img):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = now + '_' + check_filename(title)
    # 新建博客
    os.makedirs(os.path.join(root_blog, filename), exist_ok=True)
    target_path = os.path.join(root_blog, filename, f'crop_{check_filename(title)}')
    try:
        if os.path.exists(target_path):
            files = os.listdir(root_img)
            for f in files:
                if not os.path.exists(os.path.join(target_path, f)):
                    shutil.copytree(os.path.join(root_img, f), os.path.join(target_path, f))
        else:
            shutil.copytree(root_img, target_path)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())
    path_imgs = glob.glob(os.path.join(root_img, '*', '*.jpg'))
    if len(path_imgs) > 0:
        bg_filename = str(int(time.time())) + '.jpg'
        shutil.copyfile(path_imgs[0], os.path.join(root_blog_images, bg_filename))
        path_bg = f'/images/{bg_filename}'
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
    with open(target_path_md, 'w', encoding='utf-8') as f:
        f.write(md)


if __name__ == '__main__':
    # 2018-09-07 09:25:00
    img_list = os.listdir(r'D:\MyWork\AutoFX\arxiv\2022-02-14\crop_无监督_半监督_对比学习\2202.05830v1')
    print(img_list)
    print(sorted(img_list))
    pass
