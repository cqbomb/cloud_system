#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from cloud_system.modules.ASA.asa_0_login_info import ip
from cloud_system.modules.ASA.asa_4_all_auto import asa_all_auto
from cloud_system.modules.IOS.config_dhcp_server import config_server, dhcp_server_ip
from cloud_system.modules.Nexus.nexus_6_all_auto import nexus_all_auto
from cloud_system.modules.vSphere.vsphere_1_get_vm_list import get_vm_id
from cloud_system.modules.vSphere.vsphere_2_get_portgroup_list import get_network_id
from cloud_system.modules.vSphere.vsphere_8_all_auto import vsphere_all_auto


def qyt_cloud_all_auto(cpu_cores, mem):
    if mem == 1 and cpu_cores == 1:
        temp_no = 1
    elif mem == 2 and cpu_cores == 1:
        temp_no = 2
    elif mem == 1 and cpu_cores == 2:
        temp_no = 3
    elif mem == 2 and cpu_cores == 2:
        temp_no = 4

    while True:
        vlanid = randint(10,100)
        vmid_list = get_vm_id()
        netid_list = get_network_id()
        if vlanid in vmid_list:
            continue
        if vlanid in netid_list:
            continue
        break

    vsphere_all_auto(temp_no, vlanid)
    config_server(vlanid, dhcp_server_ip)
    nexus_all_auto(vlanid)
    asa_all_auto(vlanid, ip)


if __name__ == "__main__":
    qyt_cloud_all_auto(1, 1)

