# -*- coding:utf-8 -*-

"""
author: FddDaiErBai
date: 2022.08.16
"""

import socket

# 创建套接字（socket）TCP协议
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建一个UDP协议的Socket
s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print(s1)