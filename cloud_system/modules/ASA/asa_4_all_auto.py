#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from asa_0_login_info import ip
from asa_1_create_obj import create_in_obj, create_out_obj
from asa_2_create_nat import create_nat
from asa_3_create_acl import create_acl


def asa_all_auto(vlanid, ip):
    print('Creating ASA Object')
    create_in_obj(vlanid, ip)
    create_out_obj(vlanid, ip)
    print('ASA Object Created!')
    print('Creating ASA NAT')
    create_nat(vlanid, ip)
    print('ASA Nat Created!')
    print('Creating ASA ACL')
    create_acl(vlanid, ip)
    print('ASA ACL Created!')


if __name__ == "__main__":
    asa_all_auto(77, ip)

