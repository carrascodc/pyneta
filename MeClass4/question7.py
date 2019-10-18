#!/usr/bin/env python

import json
from ciscoconfparse import CiscoConfParse

bgp_peers = []

CONFIG = '''
router bgp 44
 bgp router-id 10.220.88.38
 address-family ipv4 unicast
 !
 neighbor 10.220.88.20
  remote-as 42
  description pynet-rtr1
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
  !
 !
 neighbor 10.220.88.32
  remote-as 43
  address-family ipv4 unicast
   route-policy ALLOW in
   route-policy ALLOW out
'''

parse = CiscoConfParse(CONFIG.splitlines())

for obj in parse.find_objects(r'neighbor'):
    neighbor_ip = obj.re_match(r'neighbor\s(\S+)')
    remote_as = obj.children[0].re_match(r'remote-as\s(\S+)')
    bgp_peers.append((neighbor_ip,remote_as))


print(bgp_peers)
