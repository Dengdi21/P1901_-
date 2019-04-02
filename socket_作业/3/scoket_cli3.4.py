# 书写一个类似于qq群聊的聊天室,要求所有人都能收到所有人发送的消息,要求实现客户端和服务端。

# 客户端代码,每个客户端代码相同。

import socket


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('127.0.0.1', 60020)
ss.connect(addr)
print('已连接服务器，可以开始聊天啦')

while 1:
    try:
        print('等待输入：', end='')
        msg = input()
        ss.send(msg.encode())

        rcv1 = ss.recv(1024)
        if rcv1:
            print(rcv1.decode('utf-8'))
        else:
            continue

    except Exception:
        break

ss.close()
