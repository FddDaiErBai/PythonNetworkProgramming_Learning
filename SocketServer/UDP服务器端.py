# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.08.16
"""

from socket import *

# 创建一个服务端端Socket
socket_server = socket(AF_INET, SOCK_DGRAM)

# 定义服务器端IP地址和端口号
host_port = ("192.168.2.4", 8090)

# 服务器端端Socket绑定地址和端口 只有绑定了地址和端口 才能称之为服务器端Socket
socket_server.bind(host_port)

# 接收客户端发送过来的数据 每次接收1KB的数据 收到的每一个数据报 里面是一个元组 第一个值是数据内容 第二个源地址和源端口号
data = socket_server.recvfrom(1024)

print(data[0].decode('utf-8'))
print(data)

# 关闭套接字来释放资源
socket_server.close()
