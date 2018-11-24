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
    path('admin/', admin.site.urls),
    path('subscribevm/', qyt_forms.subscribevm),
    path('accounts/login/', qyt_login.qyt_login),
    path('accounts/logout/', qyt_login.qyt_logout),
    path('webconsole/<str:name>/', qyt_webconsole.webconsole),
    path('myvms/', qyt_forms.myvms),
    path('poweron/<str:vmname>', qyt_vm_power_control.poweron),
    path('poweroff/<str:vmname>', qyt_vm_power_control.poweroff),
    path('delete/<str:vmname>', qyt_delete_vm.delete_vm),
    path('recovery/', qyt_recovery.recovery_cloud),
    path('', index.index)
]
