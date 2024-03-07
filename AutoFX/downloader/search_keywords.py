import requests
import time
from bs4 import BeautifulSoup
import os
import glob
import random
import numpy as np
from utils.multi_download import download
from tqdm import tqdm
from downloader.gather_info import create_markdown  # AOverview
from configs import proxy, root_path
from utils.zip_tools import zip_ya

if not os.path.isdir(root_path): os.makedirs(root_path)


def get_one_page(url):
    print('GET', url)
    response = requests.get(url, verify=False, proxies=proxy)
    time.sleep(15)

    while response.status_code == 403:
        time.sleep(500 + random.uniform(0, 500))
        response = requests.get(url)
    if response.status_code == 200:
        return response.text

    return None


def get_abstract(arxiv_id='2101.12159'):
    html = get_one_page("https://arxiv.org/abs/" + arxiv_id)
    soup = BeautifulSoup(html, features='html.parser')
    titles = soup.find_all('h1', class_='title mathjax')
    title = titles[0].text
    abstracts = soup.find_all('blockquote', class_='abstract mathjax')
    abs = abstracts[0].text
    abs = abs.replace('-\n', '')  # 连接换行单词
    abs = abs.replace('\n', " ")  # 删除换行
    return title, abs


def save_markdown(save_dir, title, abs, url):
    detail = {}
    detail['title'] = title
    detail['abs'] = abs
    detail['url'] = url
    np.save(os.path.join(save_dir, "details.npy"), detail)
    print("write abs txt finish")


def get_paper_list(keyword='kinship', only_title=True):
    keyword = keyword.replace(' ', '+')
    # 只取前两百篇
    if only_title:
        url = 'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=' + keyword + '&terms-0-field=title&classification-computer_science=y&classification-physics_archives=all&classification-include_cross_list=exclude&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=200&order=-announced_date_first'
    else:
        url = 'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=' + keyword + '&terms-0-field=all&classification-computer_science=y&classification-physics_archives=all&classification-include_cross_list=exclude&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=200&order=-announced_date_first'
    html = get_one_page(url)
    soup = BeautifulSoup(html, features='html.parser')
    pdfs = soup.find_all('p', class_='list-title is-inline-block')
    arXivIDs = [p.text.split("\n")[0].split(':')[1] for p in pdfs]
    return arXivIDs


def check_filename(title):
    pdfname = title.replace("/", "_")  # pdf名中不能出现/和：
    pdfname = pdfname.replace("?", "_")
    pdfname = pdfname.replace("\"", "_")
    pdfname = pdfname.replace("*", "_")
    pdfname = pdfname.replace(":", "_")
    pdfname = pdfname.replace("\n", "")
    pdfname = pdfname.replace("\r", "")
    pdfname = pdfname.replace("  ", " ")
    if len(pdfname) > 130:
        pdfname = pdfname[:125]
    return pdfname


def download_loop(arxiv_id, keyword):
    title, abs = get_abstract(arxiv_id)

    pdfname = check_filename(title)
    dname = check_filename(keyword)
    save_dir = os.path.join(root_path, dname, arxiv_id)
    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, arxiv_id + "_" + pdfname + ".pdf")
    try:
        download('https://arxiv.org/pdf/' + arxiv_id + ".pdf", save_path)
    except:
        print('cannot download', id)
    save_markdown(save_dir, title, abs, 'https://arxiv.org/pdf/' + arxiv_id)


def finish(root_dir, needPDF, needZip):
    if not needPDF:
        pdf = glob.glob(os.path.join(root_dir, '*', '*.pdf'))
        for p in pdf:
            print(p)
            os.remove(p)
    if needZip:
        zip_ya(root_dir)


if __name__ == '__main__':
    keyword = input("input keyword:")
    print(keyword)
    only = input("only search in title(yes/no):")
    if only == 'yes':
        arXivIDs = get_paper_list(keyword, only_title=True)
    else:
        arXivIDs = get_paper_list(keyword, only_title=False)

    for id in tqdm(arXivIDs):
        download_loop(id, keyword)
    dname = check_filename(keyword)
    print("finish download files, and start to parse!", 'list length:', len(arXivIDs))
