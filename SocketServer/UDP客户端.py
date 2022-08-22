# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.08.16
"""

from socket import *


# 创建一个UDP协议的套接字 然后发送一个数据到网络上的另外一个进程
client_socket = socket(AF_INET, SOCK_DGRAM)

# 定一个接收消息的目标 8090是一个目标服务器端口 192.168.2.4是目标服务器的地址
server_host_port = ("192.168.2.4", 8090)
# server_host_port = ("www.baidu.com", 8080)

# 准备即将发生的数据 encode表示按照一种编码格式把数据变成字节数据bytes
# 数据一定是字节数据才能对外发送
datas = input("请输入:").encode("utf-8")

# 发送数据
client_socket.sendto(datas, server_host_port)

print("发送成功")

# 关闭套接字 其实就是释放了系统资源
client_socket.close
