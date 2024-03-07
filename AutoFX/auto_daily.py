import time
import pandas as pd
from bs4 import BeautifulSoup
import os
import numpy as np
from tqdm import tqdm
from configs import proxy, root_path
# from web_uploader.main import control_upload, login
from utils.union import get_one_page, download_loop
from arxiv_content import parse_arxiv_content
from auto_crop_img import control

os.makedirs(root_path, exist_ok=True)


def download_new_submissions():
    keep_subjects = ['cs.CV', 'cs.AI', 'cs.LG', 'cs.CL']
    url = 'https://arxiv.org/list/cs/pastweek?show=1000'
    html = get_one_page(url)
    soup = BeautifulSoup(html, features='html.parser')
    all_day = soup.find_all('dl')
    # print("last day")
    content = all_day[1]
    list_ids = content.find_all('a', title='Abstract')
    list_title = content.find_all('div', class_='list-title mathjax')
    list_authors = content.find_all('div', class_='list-authors')
    list_subjects = content.find_all('div', class_='list-subjects')
    list_subject_split = []
    for subjects in list_subjects:
        subjects = subjects.text.split(': ', maxsplit=1)[1]
        subjects = subjects.replace('\n\n', '')
        subjects = subjects.replace('\n', '')
        subject_split = subjects.split('; ')
        list_subject_split.append(subject_split)
    items = []
    for i, paper in enumerate(zip(list_ids, list_title, list_authors, list_subjects, list_subject_split)):
        if paper[4][0].split('(')[1].split(')')[0] in keep_subjects:
            items.append([paper[0].text, paper[1].text, paper[2].text, paper[3].text, paper[4]])

    # print("today")
    content = all_day[0]
    list_ids = content.find_all('a', title='Abstract')
    list_title = content.find_all('div', class_='list-title mathjax')
    list_authors = content.find_all('div', class_='list-authors')
    list_subjects = content.find_all('div', class_='list-subjects')
    list_subject_split = []
    for subjects in list_subjects:
        subjects = subjects.text.split(': ', maxsplit=1)[1]
        subjects = subjects.replace('\n\n', '')
        subjects = subjects.replace('\n', '')
        subject_split = subjects.split('; ')
        list_subject_split.append(subject_split)
    for i, paper in enumerate(zip(list_ids, list_title, list_authors, list_subjects, list_subject_split)):
        if paper[4][0].split('(')[1].split(')')[0] in keep_subjects:
            items.append([paper[0].text, paper[1].text, paper[2].text, paper[3].text, paper[4]])

    name = ['id', 'title', 'authors', 'subjects', 'subject_split']
    paper = pd.DataFrame(columns=name, data=items)

    save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))
    os.makedirs(save_dir, exist_ok=True)
    if os.path.exists(os.path.join(save_dir, time.strftime("%Y-%m-%d") + '.csv')):
        os.remove(os.path.join(save_dir, time.strftime("%Y-%m-%d") + '.csv'))
    paper.to_csv(os.path.join(save_dir, time.strftime("%Y-%m-%d") + '.csv'))
    return paper


def filter_keywords(keywords, needParse=True):
    if needParse:
        pass
        # browser = login('./web_uploader/chromedriver.exe')  # 浏览器登录
    save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))
    path_daily_paper = os.path.join(save_dir, time.strftime("%Y-%m-%d") + '.csv')
    arXivs = pd.read_csv(path_daily_paper)['id'].to_list()
    id_list = ''
    for a in arXivs:
        id_list = id_list + a.split(':')[1] + ','
    id_list = id_list[:-1]
    query = ''
    for k in keywords:
        query = query + f'all:{k}'
        if k != keywords[-1]:
            query = query + '+OR+'

    response = get_one_page(f'https://export.arxiv.org/api/query?id_list={id_list}&search_query={query}')
    papers = parse_arxiv_content(response=response)
    np.save(os.path.join(save_dir, 'all_abs'), papers)
    for i, item in enumerate(tqdm(papers)):
        url_id, updated, published, title, summary, authors, categorys, comments = item
        download_loop(url_id, title, save_dir, desc=f'{i}/{len(papers)}')
    print(f'Finished download {len(papers)} files!')
    if needParse:
        print('Start parsing files！')
        control(save_dir)
        # print('Parsing the file is complete, and uploading is started!')
        # control_upload(browser, root_path)
        # print('All work done!')


if __name__ == '__main__':
    download_new_submissions()
    keywords = ['nerf', 'clip', 'gan', 'MLP', 'dynamic', 'stylegan', 'Vision MLP', 'ViT', 'bert', 'prompt']
    kw1 = ['Contrastive', 'kinship', 'vision transformer', 'unsupervised', 'semi-supervised', 'object tracking',
           'detection', 'segmentation', 'Generative Adversarial Network',
           'caption', 'adversarial training', 'Modality', 'Multimodal']
    kw2 = ['adversarial attack', 'adversarial example']
    filter_keywords(keywords + kw1, needParse=True)
