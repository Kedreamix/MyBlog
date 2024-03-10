import glob
import time
import datetime
import os
import numpy as np
from configs import proxy, root_path
from utils.union import update_cover
from utils.union import get_one_page, download_loop, check_filename, check_cond
from arxiv_content import parse_arxiv_content
from auto_crop_img import control
# from utils.update_hexo import control_blog
from utils.update_hexo_kedreamix import control_blog
# from utils.update_hexo_img_online import control_blog
import pytz
root_path = "./CVPR"
os.makedirs(root_path, exist_ok=True)


def filter_keywords(keywords, keep_subjects, needParse=True, page_number = 10):
    save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))
    os.makedirs(save_dir, exist_ok=True)
    for key in keywords.keys():
        querys = keywords[key]
        papers = []
        for query in querys:
            response = get_one_page(
                f'https://export.arxiv.org/api/query?search_query={query}&sortBy=submittedDate&sortOrder=descending&start=0&max_results={page_number}')
            if response is None:
                print("Warning: Failed to obtain source information, please check the network!")
                continue
            papers = papers + parse_arxiv_content(response=response)
        # querys = [f"({query})" for query in querys]
        # querys = "+OR+".join(querys)
        # response = get_one_page(
        #     f'https://export.arxiv.org/api/query?search_query={querys}&sortBy=submittedDate&sortOrder=descending&start=0&max_results={page_number}')
        # if response is None:
        #     print("Warning: Failed to obtain source information, please check the network!")
        #     continue
        # papers = papers + parse_arxiv_content(response=response)
        unique_papers = []
        for item in papers:
            if item not in unique_papers:
                unique_papers.append(item)
        # print(unique_papers)
        papers = unique_papers
        papers.sort(key=lambda x: x[2], reverse=True)
        # print(papers)
        # papers = papers[:20]
        key_name = check_filename(key)
        np.save(os.path.join(save_dir, f'{key_name}_abs'), papers)
        urls_idxs = []
        select_tags = []
        folders = [folder for folder in os.listdir('arxiv') if os.path.isdir(os.path.join('arxiv', folder))]
        folders.sort()
        # print(folders)
        latest_folder = folders[-1]
        latest_time = datetime.datetime.strptime(latest_folder, "%Y-%m-%d").replace(tzinfo=pytz.utc)
        for i, item in enumerate(papers):
            url_id, updated, published, title, summary, authors, categorys, comments = item
            t1 = datetime.datetime.strptime(published, "%Y-%m-%dT%H:%M:%S%z")
            p1 = datetime.datetime.strptime(updated, "%Y-%m-%dT%H:%M:%S%z")
            now = datetime.datetime.now()
            now = datetime.datetime.strftime(now, "%Y-%m-%dT%H:%M:%S%z")
            now = datetime.datetime.strptime(now + '+08:00', "%Y-%m-%dT%H:%M:%S%z")
            if 'CVPR'  in comments:
                arxiv_id = os.path.basename(url_id)
                urls_idxs.append(i)
                select_tags.append(arxiv_id)
            # if categorys[0] in keep_subjects and check_cond(summary, comments):  # 只考虑主类别，只使用主类别进行操作，不进行筛选
            #     # print(now, t1, (now - t1).days)
            #     arxiv_id = os.path.basename(url_id)
            #     if arxiv_id in select_tags and (now - t1).days > 1: continue
            #     # 判断之前是不是运行过，但其实后面也有，所以这一部分，可能会有点多余
            #     tmp_cur = glob.glob(os.path.join(root_path, '*', f'crop_{key_name}', arxiv_id))
            #     if len(tmp_cur) > 0: continue
            #     if (now - t1).days > 60: continue # 如果已经发布了两个多月了，那就不用看了
            #     urls_idxs.append(i)
            #     select_tags.append(arxiv_id)
        # urls_idxs = urls_idxs[:25] # 25篇中可能有重复的，但是后续会筛选，如果太久没有更新，这里可以提高
        '''
        if len(urls_idxs) == 0:
            for i, item in enumerate(papers):
                url_id, updated, published, title, summary, authors, categorys, comments = item
                t1 = datetime.datetime.strptime(updated, "%Y-%m-%dT%H:%M:%S%z")
                now = datetime.datetime.now()
                now = datetime.datetime.strftime(now, "%Y-%m-%dT%H:%M:%S%z")
                now = datetime.datetime.strptime(now + '+08:00', "%Y-%m-%dT%H:%M:%S%z")
                if categorys[0] in keep_subjects:  # 只考虑主类别
                    arxiv_id = os.path.basename(url_id)
                    if arxiv_id in select_tags and (now - t1).days > 1: continue
                    tmp_cur = glob.glob(os.path.join(root_path, '*', f'crop_{key_name}', arxiv_id))
                    if len(tmp_cur) > 0: continue
                    urls_idxs.append(i)
                    select_tags.append(arxiv_id)
        '''

        has_download = 0
        print(f'{key} -> {len(urls_idxs)} files!')
        for i, idx in enumerate(urls_idxs):
            url_id, updated, published, title, summary, authors, categorys, comments = papers[idx]
            
            download_loop(url_id, title, save_dir, desc=f'{i}/{len(urls_idxs)}')
            has_download += 1
            if has_download > 50:
                break
        print(f'{key} -> Finished download {has_download} files!')
        
        if needParse and len(urls_idxs) > 0:
            print('Start parsing files！')
            n = control(save_dir, key_name)
            if n == 0: continue
            print('Parsing the file is complete, and uploading is started!')
            control_blog(key, os.path.join(save_dir, f'{key_name}_abs.md'))

            
    # update_cover(max_page=5)
    # os.system('./utils/hexo_server_win.bat')
    # os.system(r'D:\MyBlog\AutoFX\utils\hexo_server_win.bat')
    print('All work done!')


if __name__ == '__main__':
    from configs import keywords_dict, keep_subjects
    filter_keywords(keywords_dict, keep_subjects, needParse=True, page_number = 20)