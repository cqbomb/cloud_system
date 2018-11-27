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


# 周期性(使用crontab调度,每10秒执行一次)更新数据库中虚拟机的电源状态
# vim /etc/crontab

#   Example of job definition:
#   .---------------- minute (0 - 59)
#   |  .------------- hour (0 - 23)
#   |  |  .---------- day of month (1 - 31)
#   |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
#   |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
#   |  |  |  |  |
#   *  *  *  *  * user-name  command to be executed
#   *  *  *  *  * root /usr/local/bin/python3 /cloud/cloud_system/modules/Cloud_AUTO/Monitor_DB_VM.py
#   *  *  *  *  * root sleep 10; /usr/local/bin/python3 /cloud/cloud_system/modules/Cloud_AUTO/Monitor_DB_VM.py
#   *  *  *  *  * root sleep 20; /usr/local/bin/python3 /cloud/cloud_system/modules/Cloud_AUTO/Monitor_DB_VM.py
#   *  *  *  *  * root sleep 30; /usr/local/bin/python3 /cloud/cloud_system/modules/Cloud_AUTO/Monitor_DB_VM.py
#   *  *  *  *  * root sleep 40; /usr/local/bin/python3 /cloud/cloud_system/modules/Cloud_AUTO/Monitor_DB_VM.py
#   *  *  *  *  * root sleep 50; /usr/local/bin/python3 /cloud/cloud_system/modules/Cloud_AUTO/Monitor_DB_VM.py
def monitor_db_vm():
    # 连接SQLite3的数据库
    conn = sqlite3.connect('/cloud/db.sqlite3')
    cursor = conn.cursor()
    # 在虚拟机数据库中找到所有虚拟机的名字
    cursor.execute("select vm_name from qytcloud_vmdb")
    results = cursor.fetchall()
    # 获取虚拟机当前的电源状态
    vm_now_state = {x['name']: x['power_state'] for x in get_vms(vcip)}
    # 把虚拟机当前的电源状态写入到数据库
    write_db_state = {vm[0]: vm_now_state.get(vm[0], 'UNKOWN') for vm in results}

    for vm, state in write_db_state.items():
        cursor.execute("update qytcloud_vmdb set vm_status = '%s' WHERE vm_name = '%s'" % (state, vm))
    conn.commit()


if __name__ == "__main__":
    monitor_db_vm()

