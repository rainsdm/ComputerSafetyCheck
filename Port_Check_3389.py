import os


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


def jkestablished():
    connections = os.popen('netstat -n -p tcp').readlines()
    date = os.popen('date /t').readlines()
    t = os.popen('time /t').readlines()

    for connection in connections:
        if 'ESTABLISHED' in connection:
            parts = connection.split()
            if len(parts) >= 5:
                # local_address = parts[1]
                remote_address = parts[2]
                if ':' in remote_address:
                    remote_ip, remote_port = remote_address.split(':')
                    with open('success.txt', 'a+') as file:
                        if remote_address not in file.read():
                            file.write(f"{date[0].strip()},{t[0].strip()},{remote_port},{remote_ip}\n")
                            print(f"成功记录信息：{date[0].strip()},{t[0].strip()},{remote_port},{remote_ip}")
                            if remote_ip != "127.0.0.1":
                                print(f"入侵者提示：IP地址为 {remote_ip} 的主机通过端口 {remote_port} 进行了连接！")
