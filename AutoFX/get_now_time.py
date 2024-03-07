import datetime

now = datetime.datetime.now()  # 获取当前时间
time = now.strftime("%Y-%m-%d %H:%M:%S")  # 格式化时间为字符串
print(time)