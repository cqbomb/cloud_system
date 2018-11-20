#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from vsphere_0_vc_basic_actions import get_networks
from vsphere_0_login_info import vcip


def get_network_id():
    result = get_networks(vcip)

    vlanid = []

    for x in result['value']:
        if 'VLAN' in x['name']:
            vlanid.append(int(x['name'].replace('VLAN','')))

    return vlanid


if __name__ == "__main__":
    print(get_network_id())

