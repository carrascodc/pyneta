#!/usr/bin/env python
from napalm import get_network_driver

'''
from pprint import pprint
from my_devices import cisco3, nxos1, eos1
import ipdb

# Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
'''

def open_napalm_connection (my_device):
    # NAPALM Class Selection/Object Creation
    device_type = my_device.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**my_device)

    # NAPALM Action
    device.open()
    return device

def create_backup (conn_obj):
    device_name = conn_obj.get_facts()['hostname']
    device_runcfg = conn_obj.get_config()['running']

    backup_file = open(device_name+'.txt', 'a')
    backup_file.write(device_runcfg)

