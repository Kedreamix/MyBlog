import requests
import time
import random
import sys

url = "https://ehall.szu.edu.cn/yjsxkapp/sys/xsxkapp/xsxkCourse/choiceCourse.do"
cookie = "_WEU=K6Pya96D*HIIaOpNJDvkYLjT36*3FDdp12I9zMC4BpEU6wTm852pKHmEjcTuC*3s; amp.locale=undefined; route=198e00865b1eb9ef945195bcaf7595f1; JSESSIONID=Mqr3yV6TsmP5P57doNp02IIuHcz85flCEwEObxHYwgLV2N6oLzlp!-430786260; XK_TOKEN=341fd8ce-d917-4948-954a-60357ceb2a16"

headers = {
    "Cookie": cookie,
    "Referer":"https://ehall.szu.edu.cn/yjsxkapp/sys/xsxkapp/xsxkHome/gotoChooseCourse.do",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# 课程bjdm
courses_map = {
    '机器学习 (高灿)': "20232-02027000-2706106-1705047743913",
    # '机器学习（刘凤）': "20232-02027000-2706106-1705284704736",
    # '机器学习 (陈杰)': "20232-02027000-2706106-1705284673596",
}


# 输出日志
def log(content, filename="course_record.txt"):
    try:
        with open(filename, "a") as f:
            f.write(content + "\n")
            print(f"Content '{content}' logged to '{filename}'")
    except Exception as e:
        print("Error:", str(e))


# def send_request(course_name, course_bjdm, timestamp):
#     url = "http://ehall.szu.edu.cn/yjsxkapp/sys/xsxkapp/xsxkCourse/choiceCourse.do"
#     cookie = "_WEU=gVizNLsLNw4T8OaMwVwCLRhyvA3COm0fKViQtZ5V_y4KhVfi*CmBtLUBkdsmyc7Y; amp.locale=undefined; zg_did=%7B%22did%22%3A%20%2218a93c664f584f-0c2c266b584983-26031d51-1aeaa0-18a93c664f611e6%22%7D; zg_=%7B%22sid%22%3A%201695028744968%2C%22updated%22%3A%201695028744976%2C%22info%22%3A%201694696367354%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22ehall.szu.edu.cn%22%2C%22cuid%22%3A%20%222310274033%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22firstScreen%22%3A%201695028744968%7D; route=3c6424d3e2e9c7fd55b40c389d0d016f; JSESSIONID=6kmuHysGkAvujam9uitceMTFuPaj4Ju1m05joZjFBwr3Bur9YFu2!966490498; XK_TOKEN=a8106fc2-c673-4410-a37f-00e851433a28"

#     headers = {
#         "Cookie": cookie,
#     }

#     data = {
#         "bjdm": course_bjdm,
#         "lx": "0",
#     }

#     params = {
#         "_": timestamp
#     }

#     try:
#         response = requests.post(url, headers=headers, data=data, params=params)
#         response.raise_for_status()  # Raise an exception for bad status codes
#         return response.json()
#     except requests.exceptions.HTTPError as errh:
#         print(f"HTTP Error: {errh}")
#     except requests.exceptions.ConnectionError as errc:
#         print(f"Error Connecting: {errc}")
#     except requests.exceptions.Timeout as errt:
#         print(f"Timeout Error: {errt}")
#     except requests.exceptions.RequestException as err:
#         print(f"An unexpected error occurred: {err}")
#     return None


for __ in range(10000000):
    for _ in range(1000):
        time.sleep(random.random())
        if _ % 100 == 0:
            print(f"抢课中，当前次数：{__ * 1000 + _}")

        for course_name, course_bjdm in courses_map.items():
            time.sleep(random.random())

            # Get the current timestamp for each request
            timestamp = str(int(time.time() * 1000))

            data = {
                "bjdm": course_bjdm,
                "lx": "0",
            }
            params = {
                "_": timestamp
            }
            response = requests.post(url, headers=headers,
                                     data=data, params=params)

            # Check the response code and take appropriate action
            if response.status_code == 200:
                try:
                    response_json = response.json()
                
                    code = response_json.get("code", -1)
                    msg = response_json.get("msg", "")

                    if code == 0:
                        if msg == "选择的教学班容量已满 (#q8mx9)":
                            print(
                                f"Normal {course_name} : {msg}")
                        else:
                            log(f"Normal {course_name}  code: {code}")
                            log(f"Normal {course_name} : {msg}")
                            print(
                                f"Normal {course_name}  code: {code}")
                            print(
                                f"Normal {course_name} : {msg}")
                    else:
                        log(f"Warn {course_name}  code: {code}")
                        log(f"Warn {course_name} : {msg}")
                        print(f"Warn {course_name}  code: {code}")
                        print(f"Warn {course_name} : {msg}")
                except Exception as e :
                    print(f"Error {e} || {str(response.text)}")
            else:
                log(f"Error {course_name}请求失败. Status code: {response.status_code}")
                print(
                    f"Error {course_name}请求失败. Status code: {response.status_code}")
    time.sleep(random.random())

print("Print output redirected to course_record.txt")
