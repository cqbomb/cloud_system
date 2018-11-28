#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django.shortcuts import render
from qytcloud.forms import UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# 显示客户登录页面
def qyt_login(request):
    if request.method == 'POST':
        # 获取客户提交的Form内容
        form = UserForm(request.POST)
        # 提取用户名和密码
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        # 如果user不是空,并且用户处于激活状态
        if user is not None and user.is_active:
            # 用户登录
            login(request, user)
            # 创建会话变量username,并写入客户的用户名,便于后续页面提取
            request.session['username'] = username
            # 登录成功后显示主页,或者重定向的下一个页面
            next_url = request.GET.get('next', '/')
            return HttpResponseRedirect(next_url)

        else:  # 如果登录失败,给客户报错
            return render(request, 'registration/login.html', {'form': form, 'error': '用户名或密码错误'})
    else:  # 如果客户使用GET访问,并且客户已经认证,重定向他到主页
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')

        else:  # 如果客户使用GET访问, 给他展示登录页面
            form = UserForm()
            return render(request, 'registration/login.html', {'form': form})


# 登出操作,登出成功后,显示登录页面
def qyt_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')



