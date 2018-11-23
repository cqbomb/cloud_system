#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from cloud_system.modules.vSphere.vsphere_0_login_info import vcip, username, password
from pyVim.connect import SmartConnect, Disconnect, SmartConnectNoSSL
from pyVmomi import vim, vmodl
import sys


def get_token_url(vmname):

    si = SmartConnectNoSSL(host=vcip, user=username, pwd=password)
    # si = SmartConnectNoSSL(host=vcip, user=user1, pwd=pass1)

    content = si.content
    objView = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
    vmList = objView.view
    objView.Destroy()

    vmobj = None
    for vm in vmList:
        if vm.name in vmname:
            vmobj = vm
            break

    if not vmobj:
        return None

    ticket = vmobj.AcquireTicket(ticketType='webmks')
    # print('wss://{0}:{1}/ticket/{2}'.format(ticket.host, ticket.port, ticket.ticket))
    return 'wss://{0}:{1}/ticket/{2}'.format(ticket.host, ticket.port, ticket.ticket)


if __name__ == '__main__':
    print(get_token_url('CentOS_50'))

