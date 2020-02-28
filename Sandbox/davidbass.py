#!/usr/bin/env python
from __future__ import print_function, unicode_literals

from netmiko import ConnectHandler
from netmiko import Netmiko
from datetime import date
from getpass import getpass

__version__ = '1.0'
__author__ = 'David Carrasco'

username = input("Username: ")
password = getpass()


def get_sessionlog(device, stage):
#    return '/' + stage + '_'+ device +'_'+str(date.today()) + '.txt'
    return stage + '_'+ device +'_'+str(date.today()) + '.txt'

def ssh_session(device, configs, stage):
    Node = {
    'host': device,
    'username': username,
    'password': password,
    'device_type': 'cisco_nxos',
    'session_log': get_sessionlog(device, stage)
    }
    net_connect = ConnectHandler(**Node)
    net_connect.enable(),
    net_connect.send_config_set(configs),
    net_connect.disconnect()


if __name__ == "__main__":

    devices = ['nxos1.lasthop.io', 'nxos2.lasthop.io']

    pre_configs = ['show run', 'show cdp neigh', 'show ip bgp sum']
    imp_configs = ['router bgp 65000', 'neighbor 192.168.10.10', 'shutdown']
    post_configs = ['show run', 'show cdp neigh', 'show ip bgp sum']

    for device in devices:
        '''
        This for loop will include the pre, imp, and post sections.
        Each stage will leverage the ssh_session() function with 3 arguments
            Args:
                device (list): List all the devices you want to include
                configs (list): List all the configs you want to execute
                stage (str): Defines the pre, imp, or post stage

        The ssh_session() function will also use the get_sessionlog() function
        to log the output of each of the devices. This function will include
        the path ('/'), stage ('pre',)
        '''
        ### Pre script
        ssh_session(device, pre_configs, 'pre')

        ### Imp script
        ssh_session(device, imp_configs, 'imp')

        ### Post script
        ssh_session(device, post_configs, 'post')

