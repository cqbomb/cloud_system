#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from nexus_0_login_info import my_headers, username, password
from requests.auth import HTTPBasicAuth
import requests


def nexus_get_vlan_lists(ip):
    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "show vlan brief", "version": 1}, "id": 1}
    ]
    request_url = "https://" + ip + "/ins"

    r = requests.post(request_url, headers=my_headers, auth=HTTPBasicAuth(username, password), json=payload, verify=False)

    response = r.json()
    vlan_response = response['result']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']

    vlan_list = []

    if isinstance(vlan_response, list):
        for x in vlan_response:
            vlan_list.append(x['vlanshowbr-vlanid-utf'])
        return vlan_list
    else:
        vlan_list.append(vlan_response['vlanshowbr-vlanid-utf'])
        return vlan_list


if __name__ == "__main__":
    print(nexus_get_vlan_lists('192.168.1.101'))

