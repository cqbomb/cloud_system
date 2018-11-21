#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from nexus_0_login_info import get_session, my_headers


def create_svi(vlanid, ip):
    session = get_session(ip)
    nxos_api_url = "https://" + ip + "/api/node/mo/sys/intf/svi-[vlan" + str(vlanid) + "].json"

    payload = {
        "sviIf": {
            "attributes": {
                "id": "vlan" + str(vlanid),
                "adminSt": "up"
            }
        }
    }

    session.post(nxos_api_url, headers=my_headers, json=payload, verify=False)


def config_svi_ip_address(vlanid, ip):
    session = get_session(ip)
    nxos_api_url = "https://" + ip + "/api/mo/sys.json"

    payload = {
        "topSystem": {
            "children": [{
                "ipv4Entity": {
                    "children": [{
                        "ipv4Inst": {
                            "children": [{
                                "ipv4Dom": {
                                    "attributes": {
                                        "name": "vxlan-100" + str(vlanid)
                                    },
                                    "children": [{
                                        "ipv4If": {
                                            "attributes": {
                                                "id": "vlan" + str(vlanid)
                                            },
                                            "children": [{
                                                "ipv4Addr": {
                                                    "attributes": {
                                                        "addr": "172.16." + str(vlanid) + ".1/24"
                                                    }
                                                }
                                            }]
                                        }
                                    }]
                                }
                            }]
                        }
                    }]
                }
            }]
        }
    }

    session.post(nxos_api_url, headers=my_headers, json=payload, verify=False)


if __name__ == "__main__":
    # create_svi(40, '192.168.1.103')
    config_svi_ip_address(40, '192.168.1.103')

