#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django.shortcuts import render
from cloud_system.modules.vSphere.vsphere_9_get_token import get_token_url


def webconsole(request, name):
    try:
        token_result = get_token_url(name)
        return render(request, 'vsphere_web_console.html', {'text': token_result})
    except:
        return render(request, "wait_1_min.html")

