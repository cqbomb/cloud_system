#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from cloud_system.modules.Nexus.nexus_0_login_info import get_session, my_headers


# 使用REST API创建VLAN
def add_vlan(vlanid, ip):
    nxos_api_url = "https://" + ip + "/api/mo/sys/bd.json"

    payload = {
        "bdEntity": {
            "children": [{
                "l2BD": {
                    "attributes": {
                        "fabEncap": "vlan-" + str(vlanid),
                        "pcTag": "1"
                        }
                    }
                }
            ]
        }
    }
    session = get_session(ip)
    session.post(nxos_api_url, headers=my_headers, json=payload, verify=False)


if __name__ == "__main__":
    add_vlan(124, '192.168.1.101')

