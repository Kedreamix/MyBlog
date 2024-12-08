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

# def control_blog(title, path_md, daily = False):
#     """
#     根据提供的标题、Markdown文件路径和是否为日常更新来控制博客内容的生成和更新。

#     参数:
#     title (str): 博客文章的标题。
#     path_md (str): Markdown文件的路径，用于转换和生成博客内容。
#     daily (bool, optional): 是否为日常更新，默认为False。如果是日常更新，会在日期后添加'-daily'后缀。
#     """
#     # 获取当前日期并格式化，用于创建博客文件夹
#     now = datetime.datetime.now().strftime("%Y-%m-%d")
#     # 如果是日常更新，在日期后添加'-daily'后缀
#     if daily:
#         now += '-daily'
#     # 检查并处理博客标题，确保标题的合法性
#     filename = check_filename(title)
#     # filename = os.path.join(check_filename(title), now)
#     # 新建博客
#     # print(os.path.join(root_blog, now))
#     # 创建博客文件夹和临时文件夹，如果已存在则不执行任何操作
#     os.makedirs(os.path.join(root_blog, now), exist_ok=True)
#     os.makedirs(temp_dir, exist_ok=True)

#     content = ''
#     # 组合路径以访问目标Markdown文件
#     target_path_md = os.path.join(root_blog, now, filename + '.md')
#     # 如果目标Markdown文件已存在，则读取其内容并分割
#     if os.path.exists(target_path_md):
#         with open(target_path_md, 'r', encoding='utf-8') as f:
#             content = f.read() # 读旧文件
#             content = content.split('---')[2]
#     # 如果不是日常更新，则尝试转换图片格式以适配不同的平台
#     if not daily:
#         try:
#             logger.info("Start Convert Images {}".format(path_md))
#             try:
#                 # 首先尝试使用'bili'模式转换图片
#                 mode1 = 'bili'
#                 new_file = os.path.join(temp_dir, f'New_{mode1}_{os.path.basename(path_md)}_{now}')

#                 if not os.path.exists(new_file): 
#                     convert_images(path_md, mode1)
#                 else:
#                     convert_images(new_file, mode1)
#                     # logger.info("Already Convert Images {}".format(new_file))
                
#             except Exception as e:
#                 # 如果转换失败，记录错误并尝试使用'csdn'模式转换图片
#                 logger.error("write error {} {}".format(e,path_md))
#                 mode1 = 'csdn'
        
#                 convert_images(path_md, mode1)
#                 new_file = os.path.join(temp_dir, f'New_{mode1}_{os.path.basename(path_md)}')
#             # 更新Markdown文件路径为转换后的文件路径，并进一步转换图片格式为适配知乎平台
#             path_md = new_file
#             path_md2 = os.path.join(temp_dir, f'New_zhihu_{os.path.basename(new_file)}_{now}')
#             if not os.path.exists(path_md2):
#                 convert_images(new_file, 'zhihu')
#             else:
#                 convert_images(path_md2, 'zhihu')
#                 logger.info("Already Convert Images {}".format(path_md2))
#             # 搜索并获取博客背景图片路径
#             path_bg = search_bg(path_md2)
#             path_md = path_md2
#         except Exception as e:
#             # 如果在图片转换过程中发生任何错误，记录错误并设置背景图片路径为空
#             path_bg = ''
#             logger.error("write error {} {}".format(e,path_md))
#     else:
#         # 如果是日常更新，背景图片路径设置为空
#         path_bg = ''
#     # 读取Markdown文件内容
#     with open(path_md, 'r', encoding='utf-8') as f:
#         text = f.read()
#         # 生成博客头部信息
#         header = generate_header(title, path_bg, text)
#         # print(header)

#         # 根据是否存在旧内容，组合生成最终的Markdown内容
#         if content != '':
#             md = header + '\n' + text + '\n' + content
#         else:
#             md = header + '\n' + text
#     # 将最终的Markdown内容写入目标文件
#     with open(target_path_md, 'w', encoding='utf-8') as f:
#         f.write(md)
#     print(f"Control Blog {title} {target_path_md}")
#     # os.remove(path_md2)

    

def control_blog(title, path_md, daily=False):
    """
    根据提供的标题、Markdown文件路径和是否为日常更新来控制博客内容的生成和更新。

    参数:
    title (str): 博客文章的标题。
    path_md (str): Markdown文件的路径，用于转换和生成博客内容。
    daily (bool, optional): 是否为日常更新，默认为False。如果是日常更新，会在日期后添加'-daily'后缀。
    """
    # 获取当前日期并格式化，用于创建博客文件夹
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    if daily:
        now += '-daily'  # 如果是日常更新，在日期后添加'-daily'后缀

    # 检查并处理博客标题，确保标题的合法性
    filename = check_filename(title)
    
    # 创建博客文件夹和临时文件夹
    blog_dir = os.path.join(root_blog, now)
    os.makedirs(blog_dir, exist_ok=True)
    os.makedirs(temp_dir, exist_ok=True)
    
    # 目标Markdown文件路径
    target_path_md = os.path.join(blog_dir, filename + '.md')

    # 处理图片转换和背景图片的设置
    path_md, path_bg = handle_image_conversion(path_md, daily, now)

    # 读取并处理Markdown内容
    with open(path_md, 'r', encoding='utf-8') as f:
        text = f.read()

    header = generate_header(title, path_bg, text)
    md = header + '\n' + text

    # 写入最终的Markdown文件
    with open(target_path_md, 'w', encoding='utf-8') as f:
        f.write(md)

    logger.info(f"博客更新: {title} -> {target_path_md}")


def handle_image_conversion(path_md, daily, now):
    """
    处理图片转换的过程，根据是否为日常更新进行图片格式转换并返回最终的Markdown文件路径和背景图片路径。
    
    参数:
    path_md (str): 原始Markdown文件的路径。
    daily (bool): 是否为日常更新。
    now (str): 当前日期，用于文件名。

    返回:
    tuple: 转换后的Markdown文件路径和背景图片路径（如果有）。
    """
    path_bg = ''
    
    if not daily:
        try:
            logger.info("开始转换图片: {}".format(path_md))
            
            # 使用 'bili' 模式进行图片转换
            path_md = convert_images_to_format(path_md, 'bili', now)
            
            # 使用 'zhihu' 模式进行图片转换
            path_md = convert_images_to_format(path_md, 'zhihu', now)
            
            # 搜索并获取背景图片路径
            path_bg = search_bg(path_md)

        except Exception as e:
            logger.error(f"图片转换失败: {e}, 使用默认背景")
            path_bg = ''  # 如果图片转换失败，使用默认背景
    
    return path_md, path_bg

def convert_images_to_format(path_md, mode, now):
    """
    根据指定的模式转换图片格式，并返回转换后的文件路径。
    
    参数:
    path_md (str): 原始Markdown文件路径。
    mode (str): 转换模式，例如 'bili', 'csdn', 'zhihu'。
    now (str): 当前日期，用于文件名。

    返回:
    str: 转换后的文件路径。
    """
    new_file = os.path.join(temp_dir, f'New_{mode}_{os.path.basename(path_md)}_{now}')
    
    # 如果转换后的文件不存在，进行转换
    if not os.path.exists(new_file):
        convert_images(path_md, mode)  # 调用转换图片的函数
    else:
        convert_images(new_file, mode)
    return new_file