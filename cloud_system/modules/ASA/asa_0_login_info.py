#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from requests.auth import HTTPBasicAuth

# 登录用户名,密码和ASA的IP地址
username = 'admin'
password = 'Cisc0123'
ip = "192.168.1.104"

# HTTP头部内容
my_headers = {"content-type": "application/json"}

# HTTP基本认证的认证信息
auth_header = HTTPBasicAuth(username, password)



