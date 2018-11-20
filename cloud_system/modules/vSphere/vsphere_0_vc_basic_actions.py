#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

from vsphere_0_login_info import vc_session, vcip


def get_vms(vcip):
    url = 'https://' + vcip + '/rest/vcenter/vm'
    r = vc_session.get(url)
    return r.json()['value']


def get_vm_power_status(vcip, vmid):
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/power'
    r = vc_session.get(url)
    return r.json()['value']


def poweron_vm(vcip, vmid):
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/power/start'
    r = vc_session.post(url)
    try:
        return r.json()
    except Exception:
        return 'vm has power on'


def poweroff_vm(vcip, vmid):
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/power/stop'
    r = vc_session.post(url)
    try:
        return r.json()
    except Exception:
        return 'vm has power off'


def get_vm_nics(vcip, vmid):
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet'
    r = vc_session.get(url)
    return r.json()


def get_vm_nic_detail(vcip, vmid, nic):
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet/' + nic
    r = vc_session.get(url,)
    return r.json()


def get_networks(vcip):
    url = 'https://' + vcip + '/rest/vcenter/network'
    r = vc_session.get(url)
    return r.json()


def update_vm_nic(vcip, vmid, nic, network_name):
    network_nic_json = {
        "spec": {
            "backing": {
                "type": "STANDARD_PORTGROUP",
                "network": network_name
            },
        }
    }
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet/' + nic
    r = vc_session.patch(url, json=network_nic_json)
    return r.text


def get_hosts(vcip):
    url = 'https://' + vcip + '/rest/vcenter/host'
    r = vc_session.get(url)
    return r.json()


def get_datastores(vcip):
    url = 'https://' + vcip + '/rest/vcenter/datastore'
    r = vc_session.get(url)
    return r.json()


def get_folders(vcip):
    url = 'https://' + vcip + '/rest/vcenter/folder'
    r = vc_session.get(url)
    return r.json()


def create_vm(vcip, vmname):
    vm_json = {
        "spec": {
            "placement": {
                "folder": "group-v65",
                "host": "host-28",
                "datastore": "datastore-29"
            },
            "name": vmname,
            "guest_OS": "RHEL_7_64",
            "memory": {
                "hot_add_enabled": True,
                "size_MiB": 1024
            },
            "cpu": {
                "count": 1,
                "hot_add_enabled": True,
                "hot_remove_enabled": True,
                "cores_per_socket": 1
            }
        }
    }
    url = 'https://' + vcip + '/rest/vcenter/vm/'
    r = vc_session.post(url, json=vm_json)
    return r.json()


def delete_vm(vcip, vmid):
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid
    r = vc_session.delete(url)
    return r.text


def add_vm_nic(vcip, vmid, network_name):
    add_nic_json = {
        "spec": {
            "backing": {
                "type": "STANDARD_PORTGROUP",
                "network": network_name
            },
            "allow_guest_control": True,
            "mac_type": "ASSIGNED",
            "wake_on_lan_enabled": True,
            "start_connected": True,
            "type": "VMXNET3"
        }
    }
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet'
    r = vc_session.post(url, json=add_nic_json)
    return r.text


if __name__ == '__main__':
    print(get_vms(vcip))
    print(get_vm_power_status(vcip, 'vm-427'))
    print(poweron_vm(vcip, 'vm-427'))
    print(poweroff_vm(vcip, 'vm-427'))
    print(get_networks(vcip))
    print(get_vm_nics(vcip, 'vm-427'))
    print(get_vm_nic_detail(vcip, 'vm-427', '4000'))
    print(update_vm_nic(vcip, 'vm-427', '4000', 'network-414'))
    print(get_hosts(vcip))
    print(get_datastores(vcip))
    print(get_folders(vcip))
    # print(create_vm(vcip, 'qytang_newvm'))
    # print(delete_vm(vcip, "vm-433"))
    print(add_vm_nic(vcip, 'vm-434', 'network-414'))
