#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from cloud_system.modules.vSphere.vsphere_0_login_info import vcip
from cloud_system.modules.vSphere.vsphere_0_vc_basic_actions import get_vms, poweron_vm


def poweron_vm_by_vlanid(VLANID):
    vm_list = get_vms(vcip)
    for vm in vm_list:
        if vm['name'] == 'CentOS_' + str(VLANID):
            vmid = vm['vm']

    poweron_vm(vcip, vmid)


if __name__ == "__main__":
    poweron_vm_by_vlanid(58)

