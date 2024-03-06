file=$1
filename=$(basename "$file")
echo "文件名：$filename"
python convert.py -f $file -m csdn
python convert.py -f $filename -m zhihu
