# 题目: 实现一个多人聊天室
# 要求: 1.至少实现一个服务端客户端(C / S模式)的聊天室服务端和客户端代码(0 - 40分)
# 2.能够进行多人同时和服务器收发消息的服务端和客户端代码(40 - 60分)
# 3.能够实现多人同时和服务器收发消息, 并且服务器会广播消息的服务端和客户端代码(60 - 70分)
# 4.能够使用线程池来实现上面功能(70 - 80分)
# 5.能够在完成4要求的情况下考虑到多线程切换的问题, 并且对合适的地方上锁, 并说明为什么要上锁(80 - 90分)
# 6.能够在完成5的要求下实现客户端能顺利关闭退出, 并且其他客户端能收到有客户端退出的消息, 并且整体代码无bug(90 - 100分)

# 客户端代码:

import socket
from threading import Thread, RLock


def main():
    addr = ('127.0.0.1', 60034)
    ss.connect(addr)
    print('已连接服务器，可以开始聊天啦')

    t1 = Thread(target=send_cli)
    t2 = Thread(target=rcv_cli)

    t1.start()
    t2.start()

    t2.join()
    t1.join()


def rcv_cli():
    """
    客户端收消息
    :return: None
    """
    lock = RLock()
    try:
        while 1:
            lock.acquire()  # 避免在收消息过程中被操作系统退出导致收到的消息不完整
            rcv1 = ss.recv(1024)
            if rcv1:
                print(rcv1.decode('UTF-8'))
            else:
                continue
            lock.release()
    except Exception:
        ss.close()
        print('已退出')


def send_cli():
    """
    客户端发消息
    :return: None
    """
    lock1 = RLock()
    try:
        while 1:
            lock1.acquire()  # 避免在发消息过程中被操作系统退出导致发出的消息不完整
            msg = input('等待输入：')
            ss.send(msg.encode())
            lock1.release()

    except Exception:
        ss.close()
        print('已退出')


if __name__ == '__main__':
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main()
