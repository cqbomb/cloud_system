#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from cloud_system.modules.vSphere.vsphere_0_vc_basic_actions import get_vms
from cloud_system.modules.vSphere.vsphere_0_login_info import vcip


# 获取虚拟机对应的VLANID的清单
# [14]
def get_vm_id():
    vm_list = get_vms(vcip)

    vm_ids = []

    for vm in vm_list:
        try:  # 要防止没有虚拟机,或者名字里边没有CentOS的情况
            if 'CentOS_' in vm['name']:
                vm_ids.append(int(vm['name'].replace('CentOS_', '')))
        except Exception:
            pass

    return vm_ids


if __name__ == "__main__":
    print(get_vm_id())

