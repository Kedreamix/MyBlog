import os
import requests
import time
import random
import re
import json
import tenacity
from configs import proxy, root_path
from utils.multi_download import download
from loguru import logger
@tenacity.retry(wait=tenacity.wait_exponential(multiplier=1, min=4,
                                                   max=10),
                    stop=tenacity.stop_after_attempt(5),
                    reraise=True)
def get_one_page(url):
    logger.info(f'GET {url}')
    time.sleep(16)

    response = requests.get(url, verify=False, proxies=proxy)
    if response.status_code == 200:
        return response.text

    return None

"""
pip install pdfminer.six
"""
from pdfminer.high_level import extract_text

def check_if_pdf_valid(filename):
    """
    判断pdf文件是否可用
    :param filename:
    :return:
    """
    try:
        text = extract_text(filename)
    except Exception as e:
        logger.error(f"PDF {filename} is corrupted: {e}")
        return False
    
    # print("PDF is not corrupted.")
    return True

def download_loop(url, title, save_dir, desc):
    os.makedirs(save_dir, exist_ok=True)
    pdfname = check_filename(title)
    arxiv_id = os.path.basename(url)
    save_path = os.path.join(save_dir, arxiv_id + '_' + pdfname + ".pdf")
    if os.path.exists(save_path) and check_if_pdf_valid(save_path): 
        logger.info(f"{arxiv_id} hase download success in {save_path}" )
        return
    times = 0
    while True:
        try:
            times += 1
            if times > 2:
                pdf_url = url[:-2].replace('abs', 'pdf') + 'v1' + ".pdf"
            else:
                pdf_url = url[:-2].replace('abs', 'pdf') + ".pdf"
            flag = download(pdf_url, save_path, desc=desc)
            if check_if_pdf_valid(save_path): 
                logger.info(f"download success {arxiv_id} in {save_path}")
            else:
                flag = False
                logger.info(f"download failed {arxiv_id}")
                if os.path.exists(save_path): os.remove(save_path)
                time.sleep(11)
        except:
            flag = False
            logger.info(f'File download failed: {arxiv_id}')
            if os.path.exists(save_path): os.remove(save_path)
            time.sleep(11)
        
        if (flag and check_if_pdf_valid(save_path))or times >= 3:
            break


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


def check_cond(abs, comment):
    abs = abs.lower()
    keep = {
        'SOTA': ['state-of-the-art', 'sota', 'state of the art', 'significant improvements', 'outperforms',
                 'outstanding', 'highest', 'lowest', 'first place', 'successfully', 'superiority'],
        'code': ['github.com', 'http:', 'https:'],
        'first': ['to the best of our knowledge', 'best']
    }
    for k in keep.keys():
        for word in keep[k]:
            if word.lower() in abs:
                return True
    meets = ['ACM MM', 'ICLR', 'CVPR', 'ECCV', 'ICCV', 'IJCAI', 'ICIP', 'UAI', 'ICML', 'SIGGRAPH', 'FG', 'ICAPS',
             'ICME', 'ACCV', 'PRCV', 'KDD', 'UAI', 'MICCAI', 'ECML', 'NeurIPS', 'WACV', 'AAAI', 'CV', 'AI', 'ML',
             'ICASSP', 'InterSpeech']
    for c in comment:
        if c in meets:
            return True

    return False


def update_cover(max_page=5):
    root_cover = r'C:\Backup\blogs\public'
    years = []
    while True:
        for t in os.listdir(root_cover):
            if t.isnumeric(): years.append(t)
        if len(years) > 0:
            break
        else:
            time.sleep(2)

    dir_y = os.path.join(root_cover, sorted(years)[-1])
    dir_M = os.path.join(dir_y, sorted(os.listdir(dir_y))[-1])
    dir_d = os.path.join(dir_M, sorted(os.listdir(dir_M))[-1])
    path_ds = [os.path.join(dir_d, f) for f in os.listdir(dir_d)]
    tmps = []
    for d in path_ds[: max_page]:
        try:
            # url = d[len(root_cover) - 1:] # linux
            url = d[len(root_cover):]   # win
            url = url.replace("\\", "/") # win
            ff = open(os.path.join(d, 'index.html'), 'r', encoding='utf8')
            ss = ff.read()
            title = re.findall(r'<h1 class="description center-align post-title">(.*?)</h1>', ss, re.UNICODE)[0]
            cover_img = re.findall(r'''background-image: url\(\'(.*?)\'\)''', ss, re.UNICODE)[0]
            summary_date = re.findall(r'''<h1 id=\"(.*?)\">''', ss, re.UNICODE)[0]
            summary_title = re.findall(r'''<h3 id=\"(.*?)\">''', ss, re.UNICODE)[0]
            ff.close()
            cover = {'title': title,
                     'path': url,
                     'coverImg': cover_img,
                     'summary': summary_date.strip() + ' ' + summary_title.strip()}
            tmps.append(cover)
        except:
            pass
    ss = json.dumps(tmps, ensure_ascii=False, indent=3)
    f = open(r'C:\Backup\blogs\source\_data\covers.json', 'w', encoding='utf8')
    f.write(ss)
    f.close()
