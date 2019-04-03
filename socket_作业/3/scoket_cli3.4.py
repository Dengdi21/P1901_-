# 书写一个类似于qq群聊的聊天室,要求所有人都能收到所有人发送的消息,要求实现客户端和服务端。

# 客户端代码,每个客户端代码相同。

import socket
from threading import Thread

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('127.0.0.1', 60024)
ss.connect(addr)
print('已连接服务器，可以开始聊天啦')

def rcv_cli():
    while 1:
        rcv1 = ss.recv(1024)
        if rcv1:
            print(rcv1.decode('utf-8'))
        else:
            continue

def send_cli():
    while 1:
        msg = input('等待输入：')
        ss.send(msg.encode())


t1 = Thread(target=send_cli)
t2 = Thread(target=rcv_cli)

t1.start()
t2.start()

t2.join()
t1.join()
