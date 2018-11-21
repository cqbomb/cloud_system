#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

def create_in_obj(VLANID):
    username = "admin"
    password = "Cisc0123"
    ip = "192.168.1.104"
    disable_warnings()
    http = PoolManager()

    ipaddress = "172.16."+str(VLANID)+".100"
    object_name = "VLAN_" + str(VLANID) + "_HOST"
    #print('创建ASA内部Object' + object_name)
    headers = {}

    headers['Content-Type'] = 'application/json'

    user_pass_str = username + ':' + password
    user_pass_str_encode = user_pass_str.encode()
    userAndPass = b64encode(user_pass_str_encode).decode("ascii")

    headers["Authorization"] = 'Basic %s' % userAndPass

    json_data = {
                 "host" : {
                          "kind" : "IPv4Address",
                          "value" : ipaddress
                         },
                 "kind" : "object#NetworkObj",
                 "name" : object_name
                 }
    url = 'https://' + ip + '/api/objects/networkobjects'  # 请求的URL
    r = http.request('POST', url, headers=headers, body=json.dumps(json_data))  # 使用POST发起请求,并且使用认证头部
    #print(r.data.decode())

def create_out_obj(VLANID):
    username = "admin"
    password = "Cisc0123"
    ip = "192.168.1.104"

    disable_warnings()
    http = PoolManager()

    outside_ip = "202.100.1."+ str(VLANID)
    object_name = "outside_" + str(VLANID)
    #print('创建ASA外部Object'+object_name)
    headers = {}

    headers['Content-Type'] = 'application/json'

    user_pass_str = username + ':' + password
    user_pass_str_encode = user_pass_str.encode()
    userAndPass = b64encode(user_pass_str_encode).decode("ascii")

    headers["Authorization"] = 'Basic %s' % userAndPass

    json_data = {
                 "host" : {
                          "kind" : "IPv4Address",
                          "value" : outside_ip
                         },
                 "kind" : "object#NetworkObj",
                 "name" : object_name
                 }
    url = 'https://' + ip + '/api/objects/networkobjects'  # 请求的URL
    r = http.request('POST', url, headers=headers, body=json.dumps(json_data))  # 使用POST发起请求,并且使用认证头部
    #print(r.data.decode())

if __name__ == "__main__":
    create_in_obj(6)
    create_out_obj(6)

