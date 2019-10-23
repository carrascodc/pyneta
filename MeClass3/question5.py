#!/usr/bin/env python

import yaml
from netmiko import ConnectHandler
from netmiko import Netmiko
from pprint import pprint

filename = "/home/dcarrasco/.netmiko.yml"
with open(filename) as f:
    yaml_dict = yaml.load(f)

cisco3 = yaml_dict['cisco3']

Node = {
"host": cisco3['host'],
"username": cisco3['username'],
"password": cisco3['password'],
"device_type": cisco3['device_type']
}
net_connect = ConnectHandler(**Node)
print(net_connect.find_prompt())
net_connect.disconnect()


