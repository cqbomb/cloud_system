#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from django import forms
from django.core.validators import RegexValidator
from qytcloud.models import Vmdb


class VmForm(forms.Form):
    required_css_class = 'required'
    cpu_cores_choices = ((1, 1), (2, 2))
    cpu_cores = forms.IntegerField(
                                  label='CPU核心数',
                                  required=True,
                                  widget=forms.Select(choices=cpu_cores_choices,
                                                      attrs={"class": "form-control"}))
    mem_G_choices = ((1, 1), (2, 2))
    mem_G = forms.IntegerField(
                              label='内存容量（单位G）',
                              required=True,
                              widget=forms.Select(choices=mem_G_choices,
                                                  attrs={"class": "form-control"}))
    disk_space_G_choices = ((16, 16),)
    disk_space_G = forms.IntegerField(
                                     label='硬盘空间（单位G）',
                                     required=True,
                                     widget=forms.Select(choices=disk_space_G_choices,
                                                         attrs={"class": "form-control"}))
    nics_choices = ((1, 1),)
    nics = forms.IntegerField(
                             label='网卡数量',
                             required=True,
                             widget=forms.Select(choices=nics_choices,
                                                 attrs={"class": "form-control"}))
    nics_speed_M_choices = ((100, 100),)
    nics_speed_M = forms.IntegerField(
                                     label='网卡速率（单位M）',
                                     required=True,
                                     widget=forms.Select(choices=nics_speed_M_choices,
                                                         attrs={"class": "form-control"}))


class UserForm(forms.Form):
    username = forms.CharField(label='用户名',
                               max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"})
                               )
    password = forms.CharField(label='密码',
                               max_length=100,
                               required=True,
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"})
                               )