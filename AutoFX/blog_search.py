import os
import glob
import time
import datetime
import numpy as np
import pytz
from loguru import logger

from configs import proxy, root_path, keywords_dict, keep_subjects
from utils.union import update_cover, get_one_page, download_loop, check_filename, check_cond
from arxiv_content import parse_arxiv_content
from auto_crop_img import control
from utils.update_hexo_kedreamix import control_blog

# 创建根路径目录
os.makedirs(root_path, exist_ok=True)

def filter_keywords(keywords, keep_subjects, needParse=True, max_search_results=10, max_downloads=50, max_age_days=60):
    """
    根据关键词从Arxiv获取相关论文，下载并解析。

    参数:
    keywords (dict): 包含关键词和查询字符串的字典。
    keep_subjects (list): 保留的主题类别。
    needParse (bool): 是否需要解析并上传文章。默认为True。
    max_search_results (int): 每次搜索时获取的最大论文数量。默认为10。
    max_downloads (int): 限制下载的最大论文数量。默认为50。
    max_age_days (int): 下载时最大允许的论文更新时间，单位为天。默认为60天。
    """
    # 按日期创建保存文件夹
    save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))
    os.makedirs(save_dir, exist_ok=True)

    # 遍历每个关键词及其对应的查询
    for key, queries in keywords.items():
        papers = []

        # 获取每个查询的论文数据
        for query in queries:
            url = f'https://export.arxiv.org/api/query?search_query={query}&sortBy=lastUpdatedDate&sortOrder=descending&start=0&max_results={max_search_results}'
            response = get_one_page(url)
            if response is None:
                logger.warning("获取信息失败，请检查网络！")
                continue
            papers += parse_arxiv_content(response)

        # 去重并按更新时间排序
        papers = list({item[0]: item for item in papers}.values())  # 根据 URL 去重
        papers.sort(key=lambda x: x[1], reverse=True)  # 按更新时间降序排序

        key_name = check_filename(key)
        np.save(os.path.join(save_dir, f'{key_name}_abs.npy'), papers)

        # 处理每篇论文
        urls_idxs = []
        now = datetime.datetime.now(pytz.utc)

        for i, (url_id, updated, published, title, summary, authors, categories, comments) in enumerate(papers):
            updated_date = datetime.datetime.strptime(updated, "%Y-%m-%dT%H:%M:%S%z")  # 更新时间
            # 筛选符合条件的论文
            if categories[0] in keep_subjects or check_cond(summary, comments):
                arxiv_id = os.path.basename(url_id)

            # 防止重复下载
            if arxiv_id in urls_idxs and (now - updated_date).days > 1:
                print(f"跳过论文 {arxiv_id} {title}：已下载，且更新时间超过1天，不重复下载")
                continue

            # 如果已经存在了，不需要下载
            if glob.glob(os.path.join(root_path, '*', f'crop_{key_name}', arxiv_id)):
                print(f"跳过论文 {arxiv_id} {title}：已存在，文件夹中已包含此论文")
                continue

            # 如果已经超过 max_age_days 天了，说明不需要再下载了
            if (now - updated_date).days > max_age_days:
                print(f"跳过论文 {arxiv_id} {title}：更新时间超过 {max_age_days} 天，超过限制不再下载")
                continue

            urls_idxs.append(i)

        # 限制下载数量并下载论文
        logger.info(f'{key} -> 共 {len(urls_idxs)} 份文件待下载!')
        has_download = 0

        for i, idx in enumerate(urls_idxs):
            if has_download >= max_downloads:  # 限制下载数量
                break

            url_id, updated, published, title, summary, authors, categories, comments = papers[idx]
            download_loop(url_id, title, save_dir, desc=f'{i+1}/{len(urls_idxs)}')
            has_download += 1

        logger.info(f'{key} -> 已下载 {has_download} 份文件!')

        # 解析并上传文件
        if needParse and urls_idxs:
            logger.info('开始解析文件!')
            n = control(save_dir, key_name)

            if n > 0:
                logger.info('解析完成，开始上传!')
                control_blog(key, os.path.join(save_dir, f'{key_name}_abs.md'))

    # 更新封面并启动本地服务器
    os.system(r'D:\MyBlog\AutoFX\utils\hexo_server_win.bat')
    logger.info('All work done!')

if __name__ == '__main__':
    # 执行关键词过滤与下载处理
    filter_keywords(
        keywords_dict, 
        keep_subjects, 
        needParse=True, 
        max_search_results=30, 
        max_downloads=100, 
        max_age_days=60
    )