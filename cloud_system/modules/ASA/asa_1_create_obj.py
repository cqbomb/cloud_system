#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from cloud_system.modules.ASA.asa_0_login_info import ip, my_headers, auth_header
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def create_in_obj(vid, ip):
    vlanid = str(vid)
    ipaddress = "172.16." + vlanid + ".100"
    object_name = "VLAN_" + vlanid + "_HOST"

    json_data = {
                 "host": {
                          "kind": "IPv4Address",
                          "value": ipaddress
                         },
                 "kind": "object#NetworkObj",
                 "name": object_name
                 }
    url = 'https://' + ip + '/api/objects/networkobjects'  # 请求的URL
    requests.post(url, headers=my_headers, auth=auth_header, json=json_data, verify=False)  # 使用POST发起请求,并且使用认证头部


def create_out_obj(vid, ip):
    vlanid = str(vid)

    outside_ip = "202.100.1." + vlanid
    object_name = "outside_" + vlanid

    json_data = {
                 "host": {
                          "kind": "IPv4Address",
                          "value": outside_ip
                         },
                 "kind": "object#NetworkObj",
                 "name": object_name
                 }
    url = 'https://' + ip + '/api/objects/networkobjects'  # 请求的URL
    requests.post(url, headers=my_headers, auth=auth_header, json=json_data, verify=False)  # 使用POST发起请求,并且使用认证头部


if __name__ == "__main__":
    create_in_obj(6, ip)
    create_out_obj(6, ip)

