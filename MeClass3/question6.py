#!/usr/bin/env python

import yaml
from netmiko import ConnectHandler
from netmiko import Netmiko
from pprint import pprint
from ciscoconfparse import CiscoConfParse

filename = "/home/dcarrasco/.netmiko.yml"
with open(filename) as f:
    yaml_dict = yaml.load(f)

device = yaml_dict['cisco4']

Node = {
"host": device['host'],
"username": device['username'],
"password": device['password'],
"device_type": device['device_type']
}
net_connect = ConnectHandler(**Node)
CONFIG = net_connect.send_command("show run")
net_connect.disconnect()

parse = CiscoConfParse(CONFIG.splitlines())
interfaces = parse.find_objects_w_child(parentspec=r'^interface', childspec=r'ip address [0-9]')

for intf in interfaces:
    print(intf.text)
    ip_list = intf.re_search_children(r"ip address")
    for ip in ip_list:
        print(ip.text)

