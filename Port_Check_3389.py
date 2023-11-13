import os
import time


def jkmstsc():
    mstsc = (os.popen('netstat -n -p tcp | find "3389"').readlines())
    date = os.popen('date /t').readlines()
    t = os.popen('time /t').readlines()

    for x in mstsc:
        if x.strip():
            with open('success.txt', 'a+') as file:
                if x not in file.read():  # 判断是否存在，防止数据多次写入
                    file.write(f"{date[0].strip()},{t[0].strip()},{x.strip()}\n")
                    print(f"成功记录连接信息：{date[0].strip()},{t[0].strip()},{x.strip()}")