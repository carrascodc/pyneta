#!/usr/bin/env python

import pyeapi
import ipdb
import yaml
from pprint import pprint
from my_funcs import seek

def main():
    seek(filename, device_list, cfg)

if __name__ == "__main__":

    filename = 'devices3.yml'
    device_list = ['arista3.lasthop.io', 'arista4.lasthop.io']
    cfg = ['show ip arp']
    main()


