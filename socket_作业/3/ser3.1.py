# 书写一个socket服务器和客户端代码,要求客户端读取一个jpg或者png的媒体文件,
# 然后发送给服务器,服务器接受并保存在磁盘上面(位置随意)

# 服务端代码

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ('119.75.217.109', 443)

server.bind(server_addr)
print('服务器已开启')

server.listen(5)

conn, conn_addr = server.accept()

add_png = '/Users/chunmu/Desktop/Python_P1901/homework/socket_作业/1.png'
conn.send(add_png.encode())
while 1:
    msg = str(conn.recv(1460))
    if msg:
        f = open(file='/Users/chunmu/Desktop/Python_P1901/homework/socket_作业/1_1.png', mode='wb')
        f.write(msg.encode("utf-8"))
        f.close()
    else:
        break

print('服务端已关闭')
