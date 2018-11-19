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
from requests.auth import HTTPBasicAuth


vcip = '172.16.1.200'
username = 'administrator@vsphere.local'
password = 'Cisc0123,,..//'
login_url = 'https://' + vcip + '/rest/com/vmware/cis/session'  # 请求的URL


def get_session():
    client = requests.session()
    client.post(login_url, auth=HTTPBasicAuth(username, password), verify=False)

    return client


vc_session = get_session()

