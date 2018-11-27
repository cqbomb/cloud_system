#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 登录设备用户名和密码
username = "admin"
password = "Cisc0123"

# JSON RPC的头部
my_headers_rpc = {"content-type": "application/json-rpc"}
# REST API的头部
my_headers = {"content-type": "application/json"}


# 获取REST API登录的会话
def get_session(ip):
    client = requests.session()
    login_url = 'http://' + ip + '/api/aaaLogin.json'
    name_pwd = {'aaaUser': {'attributes': {'name': username, 'pwd': password}}}
    client.post(login_url, json=name_pwd, headers=my_headers, verify=False)
    return client

