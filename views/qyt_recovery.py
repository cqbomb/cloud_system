#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cloud_system.modules.vSphere.vsphere_0_login_info import vcip
from cloud_system.modules.Cloud_AUTO.Recovery_Factory_Default import recovery
from qytcloud.models import Vmdb


# 恢复试验台页面,访问此页面需要认证
@login_required()
def recovery_cloud(request):
    # 如果客户使用POST访问
    if request.method == 'POST':
        # 删除所有虚拟机和端口组
        recovery(vcip)
        # 删除Vmdb数据库内的所有虚拟机
        Vmdb.objects.all().delete()
        return render(request, 'recovery.html')
    else:  # 如果使用GET访问,给客户展示recovery.html
        return render(request, 'recovery.html')


