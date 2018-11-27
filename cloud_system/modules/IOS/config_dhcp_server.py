#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import paramiko
import time

# 登录用户名和密码
username = 'admin'
password = 'Cisc0123'
# IOS设备的IP地址
dhcp_server_ip = "192.168.1.105"


# 配置DHCP POOL
def config_server(vid, ip):
    vlanid = str(vid)
    # 使用VLANID产生子网
    network_sub = "172.16." + vlanid + "."
    # 下面是DHCP的具体CLI命令的列表
    dhcp_pool_command = ["configure terminal",
                         "ip dhcp pool Vlan" + vlanid,
                         "network " + network_sub + "0 /24",
                         "default-router " + network_sub + "1",
                         "dns-server 8.8.8.8",
                         "exit",
                         "ip dhcp excluded-address " + network_sub + "1 " + network_sub + "99",
                         "ip dhcp excluded-address " + network_sub + "101 " + network_sub + "254",
                         "exit"]
    # 使用paramiko建立SSH会话
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=username, password=password,
                look_for_keys=False, allow_agent=False)
    ssh_conn = ssh.invoke_shell()
    # For循环迭代命令列表逐个执行命令
    for x in dhcp_pool_command:
        ssh_command = x + "\n"
        ssh_conn.send(ssh_command)
        time.sleep(.5)

    print('=' * 100)
    print("DHCP Service for CentOS_" + vlanid + " is all ready")
    ssh.close()


if __name__ == "__main__":
    config_server(99, dhcp_server_ip)

