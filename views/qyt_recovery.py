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


@login_required()
def recovery_cloud(request):
    if request.method == 'POST':
        recovery(vcip)
        Vmdb.objects.all().delete()
        return render(request, 'recovery.html')
    else:
        return render(request, 'recovery.html')


