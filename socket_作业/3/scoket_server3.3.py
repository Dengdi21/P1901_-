# 书写一个类似于百度的网站服务器,能够使用普通浏览器访问,只用返回简单的hello world即可。
import socket
from threading import Thread


def baidu_server():

    sev = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('127.0.0.1', 60000)
    sev.bind(addr)
    sev.listen(5)

    while 1:
        conn, conn_addr = sev.accept()
        net = Thread(target=server_answer, args=(conn, conn_addr))
        net.start()


def server_answer(conn, connaddr):
    print('{}已连接服务器'.format(connaddr))
    conn.send('hello world')
    msg = conn.recv(1024)
    print(msg)


def main():
    baidu_server()


if __name__ == '__main__':
    main()