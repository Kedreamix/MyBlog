import subprocess
from PIL import Image
from io import BytesIO


def paste_img(file_img):
    """
    图片转换成二进制字符串，然后以位图的格式写入剪贴板

    主要思路是用Image模块打开图片，
    用BytesIO存储图片转换之后的二进制字符串

    :param file_img: 图片的路径
    """
    # 把图片写入image变量中
    # 用open函数处理后，图像对象的模式都是 RGB
    image = Image.open(file_img)

    # 声明output字节对象
    output = BytesIO()

    # 用BMP (Bitmap) 格式存储
    # 这里是位图，然后用output字节对象来存储
    image.save(output, 'BMP')

    # BMP图片有14字节的header，需要额外去除
    data = output.getvalue()[14:]

    # 关闭
    output.close()
    setClipboardData(data)


def getClipboardData():
    p = subprocess.Popen(['xclip', '-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data


def setClipboardData(data):
    p = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()
