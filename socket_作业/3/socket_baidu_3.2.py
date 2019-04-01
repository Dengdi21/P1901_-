# 2. 写一个socket用来请求百度网页,并把请求下来的报文体部分保存

import socket
from urllib.parse import urlparse

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url1 = urlparse("https://www.baidu.com")

host = url1.netloc
path = url1.path

if path == "":
    path = "/"

ss.connect((host, 80))

data = "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\nUser-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6)" \
       " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36\r\n\r\n".format(
    path, host).encode('utf8')

ss .send(data)
res = b''

while True:
    d = ss.recv(1460)
    if d:
        res += d
    else:
        break

f = open(file='/Users/chunmu/Desktop/Python_P1901/homework/socket_作业/baidu.txt', mode='wb')
f.write(d)
f.close()

ss.close()