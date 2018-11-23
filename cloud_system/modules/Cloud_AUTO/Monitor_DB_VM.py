#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import sqlite3
import sys
sys.path.append('/cloud')
from cloud_system.modules.vSphere.vsphere_0_vc_basic_actions import get_vms
from cloud_system.modules.vSphere.vsphere_0_login_info import vcip


def monitor_db_vm():
    conn = sqlite3.connect('/cloud/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("select vm_name from qytcloud_vmdb")
    results = cursor.fetchall()
    vm_now_state = {x['name']: x['power_state'] for x in get_vms(vcip)}
    write_db_state = {vm[0]: vm_now_state.get(vm[0], 'UNKOWN') for vm in results}
    # print(write_db_state)
    for vm, state in write_db_state.items():
        cursor.execute("update qytcloud_vmdb set vm_status = '%s' WHERE vm_name = '%s'" % (state, vm))
    conn.commit()


if __name__ == "__main__":
    monitor_db_vm()

