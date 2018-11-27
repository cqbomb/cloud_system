#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from cloud_system.modules.vSphere.vsphere_0_vc_basic_actions import get_networks, get_vms, add_vm_nic
from cloud_system.modules.vSphere.vsphere_0_login_info import vcip


# 根据VLANID获取网络的唯一ID
def get_net_id(no):
    result = get_networks(vcip)

    for x in result['value']:
        if x['name'] == 'VLAN'+str(no):
            return x['network']


# 根据VLANID获取虚拟机的唯一ID
def get_vmhost_id(no):
    vm_list = get_vms(vcip)

    for x in vm_list:
        if x['name'] == 'CentOS_' + str(no):
            return x['vm']


# 为虚拟机添加网络
def add_nic_to_vm(no):
    # print('网络唯一ID:' + str(net_id))
    net_id = get_net_id(no)

    # print('虚拟机唯一ID:' + str(vm_id))
    vm_id = get_vmhost_id(no)

    # print('为虚拟机'+str(vm_id)+'关联端口组'+str(net_id))
    add_vm_nic(vcip, vm_id, net_id)


if __name__ == "__main__":
    print(get_net_id(14))
    print(get_vmhost_id(58))
    add_nic_to_vm(58)

