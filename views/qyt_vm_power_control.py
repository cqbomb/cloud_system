#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django.http import HttpResponseRedirect
from cloud_system.modules.vSphere.vsphere_0_vc_basic_actions import poweroff_vm_by_name, poweron_vm_by_name
from cloud_system.modules.vSphere.vsphere_0_login_info import vcip
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required


# 关闭特定虚拟机电源,访问此页面需要认证
@login_required()
def poweroff(request, vmname):
    # 关闭特定虚拟机电源
    poweroff_vm_by_name(vcip, vmname)
    # 执行成功后,重定向到我的虚拟机页面
    return HttpResponseRedirect('/myvms/')


# 打开特定虚拟机电源,访问此页面需要认证
@login_required()
def poweron(request, vmname):
    # 打开特定虚拟机电源
    poweron_vm_by_name(vcip, vmname)
    # 执行成功后,重定向到我的虚拟机页面
    return HttpResponseRedirect('/myvms/')