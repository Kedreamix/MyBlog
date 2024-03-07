import time
import os
import numpy as np
from tqdm import tqdm
from configs import proxy, root_path
from arxiv_content import parse_arxiv_content
from utils.union import check_filename, get_one_page, download_loop
from auto_crop_img import control

os.makedirs(root_path, exist_ok=True)


def search(keyword, start=0, max_results=20, needParse=True):
    subjects = ['cs.CV', 'cs.AI', 'cs.LG', 'cs.CL']
    save_dir = os.path.join(root_path, check_filename(keyword))
    os.makedirs(save_dir, exist_ok=True)
    keyword = keyword.replace(' ', '+')
    url = f'https://export.arxiv.org/api/query?search_query=all:{keyword}&sortBy=lastUpdatedDate&sortOrder=descending&start={start}&max_results={max_results}'
    response = get_one_page(url)
    papers = parse_arxiv_content(response=response)
    np.save(os.path.join(save_dir, 'all_abs'), papers)
    urls_idxs = []
    for i, item in enumerate(papers):
        url_id, updated, published, title, summary, authors, categorys, comments = item
        if categorys[0] in subjects:  # 只考虑主类别
            urls_idxs.append(i)
    for i, idx in enumerate(urls_idxs):
        url_id, updated, published, title, summary, authors, categorys, comments = papers[idx]
        download_loop(url_id, title, save_dir, desc=f'{i}/{len(urls_idxs)}')
    print(f'Finished download {len(urls_idxs)} files!')
    if needParse:
        print('Start parsing files！')
        control(save_dir, 'all')
        print('All work done!')


if __name__ == '__main__':
    search('talking head', start=0, max_results=100, needParse=True)

