#!/usr/bin/env python

import pyeapi
from getpass import getpass
import ipdb
from pprint import pprint

#ipdb.set_trace()

cfg = ['show ip arp']

arista3 ={
    "transport": "https",
    "host": "arista3.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
    "port": "443"
}

connection = pyeapi.client.connect(**arista3)

### Establish connection
device = pyeapi.client.Node(connection)

### Send configurations
configs = device.config(cfg)

### Narrow down pertinent configs
target = configs[0]['ipV4Neighbors']

### Map IP address to MAC address of each ARP entry
answer = {}
for x in target:
    answer[x['address']] = x['hwAddress']

pprint(answer)

