#!/usr/bin/env python
from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3, nxos1, eos1

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

    # Device we are testing
    my_device = cisco3

    devices = [cisco3, nxos1]
    napalm_conns = list()

    for device in devices:
        napalm_conns.append(connectTo(device))

    print('\n')
    print('Display list of Napalm connections')
    print('-'*80)
    print(napalm_conns)
    print('\n')

