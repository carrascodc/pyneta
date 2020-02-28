#!/usr/bin/env python
from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3, nxos1, arista1
import ipdb

# Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def connectTo (my_device):
    # NAPALM Class Selection/Object Creation
    device_type = my_device.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**my_device)

    # NAPALM Action
    device.open()
    return device


if __name__ == "__main__":

    spacer = ('-'*80)
    # Devices we are testing
    devices = [cisco3, arista1]

    for device in devices:
        #ipdb.set_trace()
        print('\n')
        print(device['hostname'])
        print(spacer)
        napalm_conns = connectTo(device)
        pprint(napalm_conns.get_facts())
        print('\n' + 'Platform: ' + napalm_conns.platform)
        print(spacer + '\n' + spacer)


