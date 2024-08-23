from configs import root_path
import os 
import time
from utils.update_hexo_kedreamix import check_filename
from utils.update_hexo_kedreamix import control_blog


from configs import keywords_dict, keep_subjects
# save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))
save_dir = os.path.join(root_path, "2024-08-05")
for key in keywords_dict.keys():
    key_name = check_filename(key)
    target_md = os.path.join(save_dir, f'{key_name}_abs.md')
    if not os.path.exists(target_md): continue
    control_blog(key, target_md)
    # time.sleep(120)