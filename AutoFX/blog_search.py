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

def filter_keywords(keywords, keep_subjects, needParse=True, page_number=10):
    save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))
    os.makedirs(save_dir, exist_ok=True)
    
    for key, querys in keywords.items():
        papers = []
        
        # 获取每个关键词的论文数据
        for query in querys:
            url = f'https://export.arxiv.org/api/query?search_query={query}&sortBy=lastUpdatedDate&sortOrder=descending&start=0&max_results={page_number}'
            response = get_one_page(url)
            
            if response is None:
                logger.warning("Warning: Failed to obtain source information, please check the network!")
                continue
            
            papers = papers + parse_arxiv_content(response=response)
        
        unique_papers = []
        for item in papers:
            if item not in unique_papers:
                unique_papers.append(item)
        papers = unique_papers

        # 去重和排序，根据updated时间排序
        papers.sort(key=lambda x: x[1], reverse=True)

        key_name = check_filename(key)
        np.save(os.path.join(save_dir, f'{key_name}_abs.npy'), papers)
        
        # 处理每篇论文
        urls_idxs = []
        folders = sorted([f for f in os.listdir('arxiv') if os.path.isdir(os.path.join('arxiv', f))])
        latest_time = datetime.datetime.strptime(folders[-1], "%Y-%m-%d").replace(tzinfo=pytz.utc)
        
        for i, item in enumerate(papers):
            url_id, updated, published, title, summary, authors, categorys, comments = item
            published_date = datetime.datetime.strptime(published, "%Y-%m-%dT%H:%M:%S%z")
            updated_date = datetime.datetime.strptime(updated, "%Y-%m-%dT%H:%M:%S%z")
            now = datetime.datetime.now(pytz.utc)
            
            if categorys[0] in keep_subjects or check_cond(summary, comments):
                arxiv_id = os.path.basename(url_id)
                
                if arxiv_id in urls_idxs and (now - published_date).days > 1:
                    continue
                
                if glob.glob(os.path.join(root_path, '*', f'crop_{key_name}', arxiv_id)):
                    continue
                
                if (now - published_date).days > 60:
                    continue
                
                urls_idxs.append(i)
        
        # 下载并处理选定的论文
        logger.info(f'{key} -> {len(urls_idxs)} files!')
        has_download = 0
        
        for i, idx in enumerate(urls_idxs):
            url_id, updated, published, title, summary, authors, categorys, comments = papers[idx]
            download_loop(url_id, title, save_dir, desc=f'{i+1}/{len(urls_idxs)}')
            has_download += 1
            
            if has_download >= 50:
                break
        
        logger.info(f'{key} -> Finished downloading {has_download} files!')
        
        # 解析和上传文件
        if needParse and urls_idxs:
            logger.info('Start parsing files!')
            n = control(save_dir, key_name)
            
            if n > 0:
                logger.info('Parsing complete, starting upload!')
                control_blog(key, os.path.join(save_dir, f'{key_name}_abs.md'))
    
    # 更新封面并启动本地服务器
    os.system(r'D:\MyBlog\AutoFX\utils\hexo_server_win.bat')
    logger.info('All work done!')

if __name__ == '__main__':
    filter_keywords(keywords_dict, keep_subjects, needParse=True, page_number=20)
