#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django.http import HttpResponseRedirect
from cloud_system.modules.vSphere.vsphere_0_vc_basic_actions import delete_vm_by_name
from cloud_system.modules.vSphere.vsphere_0_login_info import vcip
from qytcloud.models import Vmdb
from django.contrib.auth.decorators import login_required


# 删除虚拟机,访问此页面需要认证
@login_required()
def delete_vm(request, vmname):
    # 删除虚拟机(关机再删除)
    delete_vm_by_name(vcip, vmname)
    # 清空Vmdb数据库
    Vmdb.objects.get(vm_name=vmname).delete()
    return HttpResponseRedirect('/myvms/')


