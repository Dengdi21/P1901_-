# 书写一个socket服务器和客户端代码,要求客户端读取一个jpg或者png的媒体文件,
# 然后发送给服务器,服务器接受并保存在磁盘上面(位置随意)

# 客户端端代码

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('127.0.0.1', 443)
client.connect(server_addr)
while 1:
    msg = client.recv(1460)
    f = open(file=msg, mode='r')
    data = f.read()
    if data:
        client.send(data.encode())
    else:
        break

client.close()
print('客户端已关闭')
