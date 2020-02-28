#!/usr/bin/env python

import pyeapi
from getpass import getpass
import ipdb
import yaml
from pprint import pprint

def main():
    with open(filename) as info:
        parms = yaml.safe_load(info)['eapi']

    eapi ={
        "transport": "https",
    #    "host": "arista3.lasthop.io",
        "username": "pyclass",
        "password": "88newclass",
        "port": "443"
    }

    for device in device_list:
        global answer
        answer = {}
        eapi['host'] = device
        print('\n')
        print(eapi['host'])
        pprint(connectto(eapi))
        print('\n'+'#'*80)
        

def connectto(eapi):
    connection = pyeapi.client.connect(**eapi)

    ### Establish connection
    device = pyeapi.client.Node(connection)

    ### Send configurations
    configs = device.config(cfg)

    ### Narrow down pertinent configs
    target = configs[0]['ipV4Neighbors']

    ### Map IP address to MAC address of each ARP entry
    for x in target:
        answer[x['address']] = x['hwAddress']

    return(answer)


if __name__ == "__main__":

    filename = 'devices3.yml'
    device_list = ['arista3.lasthop.io', 'arista4.lasthop.io']
    cfg = ['show ip arp']
    answer = {}
    main()


