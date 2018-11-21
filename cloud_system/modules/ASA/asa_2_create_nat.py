#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from asa_0_login_info import ip, my_headers, auth_header
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def create_nat(vid, ip):
    vlanid = str(vid)
    inside_obj = "VLAN_" + vlanid + "_HOST"
    outside_obj = "outside_" + vlanid

    json_data = {
                "isPatPool": False,
                "useInterfaceIPv6": False,
                "isRoundRobin": False,
                "isNetToNet": False,
                "isNoProxyArp": False,
                "translatedService": "original",
                "originalSource": {
                    "kind": "objectRef#NetworkObj",
                    "objectId": inside_obj
                },
                "isRouteLookup": False,
                "mode": "static",
                "translatedSource": {
                    "kind": "objectRef#NetworkObj",
                    "objectId": outside_obj
                },
                "isDNS": False,
                "originalInterface": {
                    "kind": "objectRef#Interface",
                    "name": "Inside"
                },
                "translatedInterface": {
                    "kind": "objectRef#Interface",
                    "name": "Outside"
                },
                "isInterfacePAT": False
                }
    url = 'https://' + ip + '/api/nat/auto'  # 请求的URL
    requests.post(url, headers=my_headers, auth=auth_header, json=json_data, verify=False)  # 使用POST发起请求,并且使用认证头部


if __name__ == "__main__":
    create_nat(6, ip)

