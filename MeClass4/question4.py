#!/usr/bin/env python

import json
from pprint import pprint

filename = "question4.json"
with open(filename) as f:
    json_dict = json.load(f)

arp_dict = {}

arp_entries = json_dict['ipV4Neighbors']

#for entry in arp_entries:
#    arp_dict.update({entry['address']:entry['hwAddress']})


for entry in arp_entries:
    ip_addr = entry["address"]
    mac_addr = entry["hwAddress"]
    arp_dict[ip_addr] = mac_addr

print(arp_dict)
