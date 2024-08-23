import os
import sys
import shutil
import datetime
from configs import root_blog, temp_dir, root_path
from utils.union import check_filename
import glob
import time
from PicConvert.convert import convert_images
from loguru import logger
def generate_header(title, path_bg, description):
    # tag = ''
    # for t in title.split('/'):
        # tag = tag + f'    - {t}\n'
    # tag = tag[:-1]
    description = description[:500]
    try:
        if '##' in description:
            description = description.split('##')[1]
    except:
        pass
    description = description.split('**Authors')[0]
    description = description.replace(':', '')
    description = description.replace('\n', ' ')
    # print(title, description)
    tag = f'    - {title}'
    top = f'''
---
title: {title}
date: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
author: Kedreamix
cover: {path_bg}
categories: Paper
tags:
{tag}
description: {title} 方向最新论文已更新，请持续关注 Update in {datetime.datetime.now().strftime("%Y-%m-%d")} {description}
keywords: {title}
toc:
toc_number: false
toc_style_simple: true
copyright:
copyright_author:
copyright_author_href:
copyright_url:
copyright_info:
mathjax: true
katex:
aplayer:
highlight_shrink:
aside:
---

>⚠️ 以下所有内容总结都来自于 Google的大语言模型[Gemini-Pro](https://ai.google.dev/)的能力，如有错误，仅供参考，谨慎使用
>🔴 请注意：千万不要用于严肃的学术场景，只能用于论文阅读前的初筛！
>💗 如果您觉得我们的项目对您有帮助 [ChatPaperFree](https://github.com/Kedreamix/ChatPaperFree) ，还请您给我们一些鼓励！⭐️ [HuggingFace免费体验](https://huggingface.co/spaces/Kedreamix/ChatPaperFree)

# {datetime.datetime.now().strftime("%Y-%m-%d")} 更新
'''
    return top
import random, re
def search_bg(md_file):
    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()

    # Regular expression to find image URLs in Markdown with ![]() syntax
    markdown_pattern = re.compile('!\[.*?\]\((.*?)\)')

    # Regular expression to find image URLs in Markdown with <img> tag
    img_pattern = re.compile('<img.*?src=["\'](.*?)["\']', re.IGNORECASE)

    # Find all image URLs in the Markdown content
    markdown_urls = re.findall(markdown_pattern, md_content)
    img_urls = re.findall(img_pattern, md_content)

    # Combine the two lists of image URLs
    all_image_urls = markdown_urls + img_urls

    # Check if there are any images
    if not all_image_urls:
        print("No images found in the Markdown file.")
        return None

    # Select a random image URL
    random_image_url = random.choice(all_image_urls)

    return random_image_url

def control_blog(title, path_md, daily = False):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    # now = '2024-08-05'
    if daily:
        now += '-daily'
    filename = check_filename(title)
    # filename = os.path.join(check_filename(title), now)
    # 新建博客
    # print(os.path.join(root_blog, now))
    os.makedirs(os.path.join(root_blog, now), exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)
    # target_path = os.path.join(root_blog, filename, f'crop_{check_filename(title)}')
    # try:
    #     if os.path.exists(target_path):
    #         files = os.listdir(root_img)
    #         for f in files:
    #             if not os.path.exists(os.path.join(target_path, f)):
    #                 shutil.copytree(os.path.join(root_img, f), os.path.join(target_path, f))
    #     else:
    #         shutil.copytree(root_img, target_path)
    # except IOError as e:
    #     print("Unable to copy file. %s" % e)
    # except:
    #     print("Unexpected error:", sys.exc_info())
    # path_imgs = glob.glob(os.path.join(root_img, '*', '*.jpg'))
    # if len(path_imgs) > 0:
    #     bg_filename = str(int(time.time())) + '.jpg'
    #     shutil.copyfile(path_imgs[0], os.path.join(root_blog_images, bg_filename))
    #     path_bg = f'/images/{bg_filename}'
    # else:
    #     path_bg = '/images/bg.png'

    content = ''
    target_path_md = os.path.join(root_blog, now, filename + '.md')
    if os.path.exists(target_path_md):
        with open(target_path_md, 'r', encoding='utf-8') as f:
            content = f.read()
            content = content.split('---')[2]
    if not daily:
        try:
            logger.info("Start Convert Images {}".format(path_md))
            try:
                mode1 = 'bili'
                convert_images(path_md, mode1)
                new_file = os.path.join(temp_dir, f'New_{mode1}_{os.path.basename(path_md)}')
            except Exception as e:
                logger.error("write error {} {}".format(e,path_md))
                mode1 = 'csdn'
                convert_images(path_md, mode1)
                new_file = os.path.join(temp_dir, f'New_{mode1}_{os.path.basename(path_md)}')
            path_md = new_file
            convert_images(new_file, 'zhihu')
            # os.remove(new_file)
            path_md2 = os.path.join(temp_dir, f'New_zhihu_{os.path.basename(new_file)}')
            path_bg = search_bg(path_md2)
            path_md = path_md2
        except Exception as e:
            path_bg = ''
            logger.error("write error {} {}".format(e,path_md))
    else:
        path_bg = ''
    with open(path_md, 'r', encoding='utf-8') as f:
        text = f.read()
        header = generate_header(title, path_bg, text)
        # print(header)

        if content != '':
            md = header + '\n' + text + '\n' + content
        else:
            md = header + '\n' + text
    with open(target_path_md, 'w', encoding='utf-8') as f:
        f.write(md)
    # os.remove(path_md2)

    