file=$1
filename=$(basename "$file")
echo "文件名：$filename"
python convert.py -f $file -m zhihu
# python convert.py -f $filename -m zhihu
