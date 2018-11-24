#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from cloud_system.modules.vSphere.vsphere_0_vc_basic_actions import get_vms, delete_vm, poweroff_vm, get_networks
from cloud_system.modules.vSphere.vsphere_0_login_info import vcip
from cloud_system.modules.vSphere.vsphere_3_create_and_remove_portgroup import remove_pg
from qytcloud.models import Vmdb
import time


def recovery(vcip):
    for vm in get_vms(vcip):
        poweroff_vm(vcip, vm['vm'])
        delete_vm(vcip, vm['vm'])
    for net in get_networks(vcip)['value']:
        remove_pg(net['name'])
        time.sleep(1)


if __name__ == "__main__":
    recovery(vcip)

