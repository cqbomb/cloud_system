#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from cloud_system.modules.vSphere.vsphere_0_sshclient import sshclient_execmd


# 使用paramiko SSH登录到ESXi创建标准交换机端口组
def create_pg(vlan_no):
    hostname = "172.16.1.201"
    port = 22
    username = "root"
    password = "Cisc0123"
    execmd = "esxcli network vswitch standard portgroup add -p VLAN"+str(vlan_no)+" -v vSwitch1"

    sshclient_execmd(hostname, port, username, password, execmd)


# 使用paramiko SSH登录到ESXi删除标准交换机端口组
def remove_pg(name):
    hostname = "172.16.1.201"
    port = 22
    username = "root"
    password = "Cisc0123"
    execmd = "esxcli network vswitch standard portgroup remove -p " + name + " -v vSwitch1"

    sshclient_execmd(hostname, port, username, password, execmd)


if __name__ == "__main__":
    # create_pg(178)
    remove_pg('VLAN27')


