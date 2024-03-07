import time
import pandas as pd
from bs4 import BeautifulSoup
import os
import numpy as np
from tqdm import tqdm
from configs import proxy, root_path
# from web_uploader.main import control_upload, login
from utils.union import get_one_page, download_loop, check_filename, check_cond
from arxiv_content import parse_arxiv_content
from auto_crop_img import control
# from utils.update_hexo import control_blog
from utils.update_hexo_kedreamix import control_blog
os.makedirs(root_path, exist_ok=True)


def download_new_submissions(num = 500):
    keep_subjects = ['cs.CV', 'cs.AI', 'cs.LG', 'cs.CL']
    url = f'https://arxiv.org/list/cs/pastweek?show={num}'
    html = get_one_page(url)
    soup = BeautifulSoup(html, features='html.parser')
    all_day = soup.find_all('dl')
    # print(len(all_day))
    # print("last day")
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

    save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d") + '-daily')
    os.makedirs(save_dir, exist_ok=True)
    if os.path.exists(os.path.join(save_dir, time.strftime("%Y-%m-%d") + '.csv')):
        os.remove(os.path.join(save_dir, time.strftime("%Y-%m-%d") + '.csv'))
    paper.to_csv(os.path.join(save_dir, time.strftime("%Y-%m-%d") + '.csv'))
    return paper


def filter_keywords(keywords, needParse=True, daily = True):
    save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d") + '-daily')
    path_daily_paper = os.path.join(save_dir, time.strftime("%Y-%m-%d") + '.csv')
    arXivs = pd.read_csv(path_daily_paper)['id'].to_list()

    batch_size = 30

    arXivs_list = [arXivs[i:i + batch_size] for i in range(0, len(arXivs), batch_size)]

    for key in keywords.keys():
        keyword = keywords[key]
        query = ''
        papers = []
        for k in keyword:
            query = query + f'abs:"{k}"'
            if k != keyword[-1]:
                query = query + '+OR+'
        # for k in keyword:
        #     # query = query + f'abs:{k}'
        #     if k != keyword[-1]:
        #         query = query + '(' + k + ')' + '+OR+'
        #     else:
        #         query += '(' + k + ')'
        for arXiv_idxs in arXivs_list:
            id_list = ''
            for a in arXiv_idxs:
                id_list = id_list + a.split(':')[1] + ','
            id_list = id_list[:-1]
            response = get_one_page(
                f'https://export.arxiv.org/api/query?id_list={id_list}&search_query={query}&sortBy=lastUpdatedDate&sortOrder=descending&start=0')
            papers = papers + parse_arxiv_content(response=response)
            # break
        print(f'{key} -> {len(papers)} files!')
        key_name = check_filename(key)
        np.save(os.path.join(save_dir, f'{key_name}_abs'), papers)
        has_download = 0
        for i, item in enumerate(tqdm(papers)):
            url_id, updated, published, title, summary, authors, categorys, comments = item
            if check_cond(summary, comments):
                download_loop(url_id, title, save_dir, desc=f'{i}/{len(papers)}')
                has_download += 0
                if has_download > 20:
                    break
        print(f'{key} -> Finished download {len(papers)} files!')
        if needParse and len(papers) > 0:
            print('Start parsing files！')
            control(save_dir, key_name, daily)
            print('Parsing the file is complete, and uploading is started!')
            control_blog(key, os.path.join(save_dir, f'{key_name}_abs.md'), daily)
            # print('Parsing the file is complete, and uploading is started!')
            # control_blog(key, os.path.join(save_dir, f'{key_name}_abs.md'), os.path.join(save_dir, f'crop_{key_name}'))
            # os.system('nohup sh ./utils/hexo_server.sh &')

    print('All work done!')


if __name__ == '__main__':
    download_new_submissions(500)
    from configs import keywords_daily_dict
    filter_keywords(keywords_daily_dict, needParse=True, daily = True)
    # keywords_dict = {
        # # 'GAN': ['GAN', 'Generative Adversarial Network', 'stylegan'],
        # # 'NeRF/Diffusion Model': ['NeRF', 'diffusion model', 'diffusion based'],
        
        # # 'Transformer/多模态/动态网络': ['vision transformer', 'Vision MLP', 'ViT', 'prompt learning',
        # #                          'image caption', 'Modality', 'dynamic network architecture'],
        # # '检测/分割/跟踪': ['object detection', 'semantic segmentation', 'instance segmentation', 'object tracking'],
        # # '对抗攻击': ['adversarial attack', 'adversarial example', 'DeepFake'],
        # # '人脸相关': ['face recognition', 'face detection', 'face parse', 'face landmark', 'face localization',
        # #          'head pose estimation', 'kinship', 'Descendant'],
        # # '无监督/半监督/对比学习': ['unsupervised learning', 'semi-supervised learning', 'contrastive learning',
        # #                  'zero shot', 'few shot']
        # 'Audio Driven Generation': ['all:"Talking Head"+OR+all:"Talking Portrait"+OR+all:"Talking Face"',
        #                             'all:"Audio-driven"+OR+all:"Speech Driven"',
        #                             '(ti:NeRF+OR+ti:"Neural Radiance")+AND+(all:"Talking Head"+OR+all:"Talking Face"+OR+all:"Audio-driven"+OR+all:"Talking Portrait"+OR+all:"Speech Driven")',
        #                             '(ti:Diffusion+OR+ti:Diffuse)+AND+(all:"Talking Head"+OR+all:"Talking Face"+OR+all:"Audio-driven"+OR+all:"Talking Portrait"+OR+all:"Speech Driven")',
        #                             '(all:"Gaussian Splatting"+OR+all:Gaussian-based)"+AND+(all:"Talking Head"+OR+all:"Talking Face"+OR+all:"Audio-driven"+OR+all:"Talking Portrait"+OR+all:"Speech Driven")',
        #                             'all:Talk',
        # ],
        # "Gaussian Splatting": ['all:"Gaussian Splatting"+OR+all:Splatting+OR+all:Gaussian', 
        #                        '(ti:"Gaussian Splatting"+OR+ti:Gaussian-based+OR+ti:Splatting+OR+ti:Gaussian)+AND+(ti:Head+OR+ti:Avatar+OR+ti:Human)'],
        
        # '3D reconstruction': ['all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction"',
        #                         'all:"human-object interaction reconstruction"+OR+all:"hand-object interaction reconstruction"+OR+all:"human reconstruction"+OR+all:"object reconstruction"',
        #                         'all:"shape generation"+OR+all:"shape synthesis"',
        #                         'all:"implicit field"+OR+all:"deformation"',
        #                         'all:"image-to-3d"+OR+all:"text-to-3d"',
        #                         '(ti:NeRF+OR+ti:"Neural Radiance")+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
        #                         '(ti:Diffusion+OR+ti:Diffuse)+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
        #                         'all:"Gaussian Splatting"+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
        #                     ],
    # }
    
