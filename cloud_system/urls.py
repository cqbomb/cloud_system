# coding=utf-8
"""cloud_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import index, qyt_forms, qyt_webconsole, qyt_login, qyt_vm_power_control, qyt_delete_vm, qyt_recovery

urlpatterns = [
    path('admin/', admin.site.urls),  # 登录管理
    path('subscribevm/', qyt_forms.subscribevm),  # 定于虚拟机
    path('accounts/login/', qyt_login.qyt_login),  # 登录
    path('accounts/logout/', qyt_login.qyt_logout),  # 登出
    path('webconsole/<str:name>/', qyt_webconsole.webconsole),  # 访问webconsole
    path('myvms/', qyt_forms.myvms),  # 显示我的虚拟机
    path('poweron/<str:vmname>', qyt_vm_power_control.poweron),  # 打开特定虚拟机电源
    path('poweroff/<str:vmname>', qyt_vm_power_control.poweroff),  # 关闭特定虚拟机电源
    path('delete/<str:vmname>', qyt_delete_vm.delete_vm),  # 删除特定虚拟机
    path('recovery/', qyt_recovery.recovery_cloud),  # 重置实验环境
    path('', index.index)  # 显示主页
]
