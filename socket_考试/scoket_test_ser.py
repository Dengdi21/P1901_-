# 题目: 实现一个多人聊天室
# 要求: 1.至少实现一个服务端客户端(C / S模式)的聊天室服务端和客户端代码(0 - 40分)
# 2.能够进行多人同时和服务器收发消息的服务端和客户端代码(40 - 60分)
# 3.能够实现多人同时和服务器收发消息, 并且服务器会广播消息的服务端和客户端代码(60 - 70分)
# 4.能够使用线程池来实现上面功能(70 - 80分)
# 5.能够在完成4要求的情况下考虑到多线程切换的问题, 并且对合适的地方上锁, 并说明为什么要上锁(80 - 90分)
# 6.能够在完成5的要求下实现客户端能顺利关闭退出, 并且其他客户端能收到有客户端退出的消息, 并且整体代码无bug(90 - 100分)

# 服务端代码：
import socket
from threading import Thread, RLock


def pel_chat_server():
    people_list = []
    sev = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('127.0.0.1', 60034)
    sev.bind(addr)
    sev.listen(5)
    print('服务器已打开')
    
    while 1:
        conn, conn_addr = sev.accept()
        people_list.append(conn)
        
        net = Thread(target=wechat, args=(conn, conn_addr, people_list))
        net.start()


def wechat(conn, connaddr, people_list):
    lock = RLock()
    try:
        while 1:
            lock.acquire()  # 服务器在收发消息时需要上锁，避免在收发消息过程中被操作系统退出导致收发的消息不完整。

            msg = conn.recv(65535).decode('utf-8')
            print('{}发来消息：{}'.format(connaddr, msg))
            re_msg = "\n{}说：{}".format(connaddr, msg)  # 服务器广播聊天消息

            for j in people_list:
                j.send(re_msg.encode())

            lock.release()
    except Exception:
        exit_msg = '{}已退出群聊'.format(connaddr)
        for j in people_list:
            j.send(exit_msg.encode())


def main():
    pel_chat_server()


if __name__ == '__main__':
    main()
