cd /home/ubuntu/blogs
hexo clean
hexo g && python /home/ubuntu/PythonProject/AutoFX/qiniu_sync.py
hexo d
