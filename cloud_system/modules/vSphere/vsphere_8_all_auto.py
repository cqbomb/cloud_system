#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from cloud_system.modules.vSphere.vsphere_3_create_and_remove_portgroup import create_pg
from cloud_system.modules.vSphere.vsphere_4_edit_portgroup_vlanid import edit_pg_vlan_id
from cloud_system.modules.vSphere.vsphere_5_clone_vm import clone_vm_from_no
from cloud_system.modules.vSphere.vsphere_6_add_nic_to_vm import add_nic_to_vm
from cloud_system.modules.vSphere.vsphere_7_poweron_vm import poweron_vm_by_vlanid


# vSphere自动化汇总
def vsphere_all_auto(temp_no, vlanid):
    # 创建特定VLAN的端口组
    print('=' * 100)
    print('Create PortGroup for VLAN' + str(vlanid))
    create_pg(vlanid)

    # 为端口组关联VLAN
    print('Edit PortGroup\'s VLAN ID: ' + str(vlanid))
    edit_pg_vlan_id(vlanid)

    # 克隆产生虚拟机
    print('Start to Create VM : CentOS_' + str(vlanid))
    clone_vm_from_no(vlanid, temp_no)

    # 为虚拟机添加网卡并关联端口组
    print('Create NetworkCard for CentOS_' + str(vlanid) + ', and Link to PortGroup')
    add_nic_to_vm(vlanid)

    # 打开特性VLAN的虚拟机
    print('Power On VM CentOS' + str(vlanid))
    poweron_vm_by_vlanid(vlanid)

    # 返回VLANID
    print('-- vSphere Auto is Fineshed --')
    return vlanid


if __name__ == "__main__":
    vsphere_all_auto(1, 99)

