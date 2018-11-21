#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from nexus_1_get_vlan_list import nexus_get_vlan_lists
from nexus_2_create_vlan import add_vlan
from nexus_3_create_config_vxlan import create_vxlan, config_vxlan_nve
from nexus_4_config_dhcp_relay import config_dhcp_relay_server
from nexus_5_config_svi import create_svi, config_svi_ip_address
nxos1_ip = '192.168.1.101'
nxos3_ip = '192.168.1.103'
dhcp_ip_address = "172.16.254.254"


def nexus_all_auto(vid):
    vlanid = str(vid)
    print('='*100)
    print('Start to Edit Nexus:')
    vxlanid = '100' + vlanid
    svi_ip = '172.16.' + vlanid + '.1'

    print('NXOS-1 vlan lists Befor: ' + str(nexus_get_vlan_lists(nxos1_ip)))
    print('NXOS-3 vlan lists Befor: ' + str(nexus_get_vlan_lists(nxos3_ip)))

    print('Create Vlan \'' + vlanid + '\' on NXOS-1 adn NXOS-3')

    add_vlan(vlanid, nxos1_ip)
    add_vlan(vlanid, nxos3_ip)

    print('NXOS-1 vlan lists Now: ' + str(nexus_get_vlan_lists(nxos1_ip)))
    print('NXOS-3 vlan lists Now: ' + str(nexus_get_vlan_lists(nxos3_ip)))

    print('Create vxlan on NXOS-1 adn NXOS-3: ' + vxlanid)
    create_vxlan(vlanid, nxos1_ip)
    config_vxlan_nve(vlanid, nxos1_ip)
    create_vxlan(vlanid, nxos3_ip)
    config_vxlan_nve(vlanid, nxos3_ip)

    print('Edit DHCP Realy for Vlan' + vlanid)
    config_dhcp_relay_server(vlanid, nxos3_ip, dhcp_ip_address)

    print('Create Vlan' + vlanid + ' SVI address' + ' on NXOS-3: ' + svi_ip)
    create_svi(vlanid, nxos3_ip)
    config_svi_ip_address(vlanid, nxos3_ip)


if __name__ == "__main__":
    nexus_all_auto(198)

