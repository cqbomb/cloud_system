#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from qytcloud.models import Vmdb
from django.http import HttpResponseRedirect
from django.shortcuts import render
from qytcloud.forms import VmForm
from django.contrib.auth.decorators import permission_required


def subscribevm(request):
    if request.method == 'POST':
        form = VmForm(request.POST)
        # 如果请求为POST,并且Form校验通过,把新添加的学员信息写入数据库
        if form.is_valid():
            s1 = Vmdb(vm_cpu_cores=request.POST.get('cpu_cores'),
                      vm_mem_G=request.POST.get('mem_G'),
                      vm_disk_space_G=request.POST.get('disk_space_G'),
                      vm_nics=request.POST.get('nics'),
                      vm_nics_speed_M=request.POST.get('nics_speed_M'),)
            s1.save()
            # 写入成功后,重定向返回展示所有学员信息的页面
            return HttpResponseRedirect('/myvms/')
        else:  # 如果Form校验失败,返回客户在Form中输入的内容和报错信息
            # 如果检查到错误,会添加错误内容到form内,例如:<ul class="errorlist"><li>QQ号码已经存在</li></ul>
            return render(request, 'subscribevm.html', {'form': form})
    else:  # 如果不是POST,就是GET,表示为初始访问, 显示表单内容给客户
        form = VmForm()
        return render(request, 'subscribevm.html', {'form': form})


def myvms(request):
    # 查询整个数据库的信息 object.all()
    result = Vmdb.objects.all()
    # 最终得到学员清单students_list,清单内部是每一个学员信息的字典
    vms_list = []
    for x in result:
        # 产生学员信息的字典
        vms_dict = {}

        vms_dict['name'] = x.vm_name
        vms_dict['cpu_cores'] = x.vm_cpu_cores
        vms_dict['mem_G'] = x.vm_mem_G
        vms_dict['disk_space_G'] = x.vm_disk_space_G
        vms_dict['nics'] = x.vm_nics
        vms_dict['nics_speed_M'] = x.vm_nics_speed_M
        vms_dict['owner'] = x.vm_owner
        vms_dict['summary'] = x.vm_summary
        vms_dict['global_ip'] = x.vm_global_ip
        vms_dict['ip'] = x.vm_ip
        vms_dict['status'] = x.vm_status
        vms_dict['webconsole_url'] = x.vm_webconsole_url
        vms_list.append(vms_dict)
    return render(request, 'myvms.html', {'vms_list': vms_list})
