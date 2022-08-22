# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.08.17
"""
# 客户端可以发送多条 客户端如果发送一个exit 则客户端退出 服务器端收到什么就返回什么


# 创建一个UDP协议的套接字 然后发送一个数据到网络上的另外一个进程
from socket import *

# 自定义变量 是否退出客户端的标记
flag = True

client_socket = socket(AF_INET, SOCK_DGRAM)


while flag:
    # 定一个接收消息的目标 8090是一个目标服务器端口 192.168.2.4是目标服务器的地址
    server_host_port = ("192.168.2.4", 8090)
    # server_host_port = ("www.baidu.com", 8080)

    # 准备即将发生的数据 encode表示按照一种编码格式把数据变成字节数据bytes
    # 数据一定是字节数据才能对外发送
    datum = input("请输入:").encode("utf-8")

    # 发送数据
    client_socket.sendto(datum, server_host_port)

    # 一定可以从服务接收到返回过来的数据 打印服务器返回的数据
    print("返回的数据是:", client_socket.recvfrom(1024)[0].decode("utf-8"))
    print("发送成功")
    if (datum == "exit"):
        flag = False


# 关闭套接字 其实就是释放了系统资源
client_socket.close
