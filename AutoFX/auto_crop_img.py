import os
import glob
import shutil

import numpy as np
from paper_layout_parser.parse_pdf import convert_pdf2img, parse_page
from downloader.markdown_model import typing
from configs import proxy, root_path
from tqdm import tqdm
from loguru import logger

def parse_pdf(path_pdf, save_dir, max_file=6):
    os.makedirs(save_dir, exist_ok=True)
    pil_images = convert_pdf2img(path_pdf)
    total_files = 0
    for page_num, img in enumerate(pil_images):
        if page_num == 0:
            img.save(os.path.join(save_dir, 'page_' + str(page_num) + '_' + str(0) + '.jpg'))
            continue
        if page_num > 5:  # 只要前20页
            break
        total_files += parse_page(img, page_num, save_dir=save_dir)
        if total_files > max_file:
            break


def load_abs(root_pdf, filename_abs='all_abs.npy'):
    all_abs = np.load(os.path.join(root_pdf, filename_abs), allow_pickle=True)
    abs_dict = {}
    for item in all_abs:
        url_id, updated, published, title, summary, authors, categorys, comments = item
        abs_dict[os.path.basename(url_id)] = item
    return abs_dict


def control(root_pdf, key_name, daily=False):
    abs_dict = load_abs(root_pdf, f'{key_name}_abs.npy')
    files = glob.glob(os.path.join(root_pdf, '*.pdf'))
    files.sort(reverse=True)
    if len(files) == 0:
        return len(files)
    if os.path.exists(os.path.join(root_pdf, f"{key_name}_abs.md")):
        file_path = os.path.join(root_pdf, f"{key_name}_abs.md")

        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            # Use np.loadtxt to load the data from the opened file
            all_md = file.read()

    else:
        all_md = ''
    for f in tqdm(files):
        logger.info("Processing: {}".format(f))
        aid = os.path.basename(f).split('_')[0]
        save_dir = os.path.join(root_pdf, f'crop_{key_name}', aid)
        tmp_all = glob.glob(os.path.join(root_pdf, 'crop_*', aid))
        if aid not in abs_dict.keys():
            logger.info(f'{aid} not in abs_dict')
            continue
        elif os.path.exists(save_dir):
            logger.info(f'{aid} already exists')
            continue
        if len(tmp_all) > 0:
            shutil.copytree(tmp_all[0], save_dir)
        else:
            parse_pdf(f, save_dir)
        item = abs_dict[aid]
        logger.info("Start Chat With paper")
        md = typing(item, os.path.join(root_pdf, f'crop_{key_name}', aid), key_name, daily)
        all_md = all_md + md
        # np.savetxt(os.path.join(root_pdf, f"{key_name}_abs.md"), [all_md], "%s", encoding='utf-8')
    np.savetxt(os.path.join(root_pdf, f"{key_name}_abs.md"), [all_md], "%s", encoding='utf-8')
    return len(files)


if __name__ == '__main__':
    control(os.path.join(root_path, 'nerf'))
