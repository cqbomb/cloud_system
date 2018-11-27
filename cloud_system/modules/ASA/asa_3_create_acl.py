#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from cloud_system.modules.ASA.asa_0_login_info import ip, my_headers, auth_header
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# 配置ACL放行Any访问内部服务器的TCP和ICMP流量
def create_acl(vid, ip):
    # 内部真实服务器的Object
    object_name = "VLAN_" + str(vid) + "_HOST"
    # 构建ACL的JSON数据,放行ICMP
    json_data_icmp = {
                "sourceAddress": {
                "kind": "AnyIPAddress",
                "value": "any"
                },
                "destinationAddress": {
                "kind": "objectRef#NetworkObj",
                "objectId": object_name
                },
                "destinationService": {
                "kind": "NetworkProtocol",
                "value": "icmp"
                },
                "permit": True,
                "active": True
                }

    url = 'https://' + ip + '/api/access/in/Outside/rules'  # 请求的URL
    # 使用POST发起请求,添加头部,认证信息和JSON数据
    requests.post(url, headers=my_headers, auth=auth_header, json=json_data_icmp, verify=False)

    # 等待两秒后继续添加ACL
    time.sleep(2)
    # 构建ACL的JSON数据,放行TCP
    json_data_tcp = {
                "sourceAddress": {
                "kind": "AnyIPAddress",
                "value": "any"
                },
                "destinationAddress": {
                "kind": "objectRef#NetworkObj",
                "objectId": object_name
                },
                "destinationService": {
                "kind": "NetworkProtocol",
                "value": "tcp"
                },
                "permit": True,
                "active": True
                }
    # 使用POST发起请求,添加头部,认证信息和JSON数据
    requests.post(url, headers=my_headers, auth=auth_header, json=json_data_tcp, verify=False) # 使用POST发起请求,并且使用认证头部


if __name__ == "__main__":
    create_acl(6, ip)

