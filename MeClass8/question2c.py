#!/usr/bin/env python
from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3, nxos1, arista1
from my_functions import open_napalm_connection
import ipdb

# Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


if __name__ == "__main__":

    spacer = ('-'*80)
    devices = [cisco3, arista1]
    conn_obj_list = list()

    for device in devices:
        #ipdb.set_trace()
        conn_obj_list.append(open_napalm_connection(device))

    try:
        for obj in conn_obj_list:
            #ipdb.set_trace()
            print('\n')
            pprint(obj.get_facts()['hostname'])
            print(spacer)
            pprint(obj.get_ntp_peers())
            print(spacer + '\n' + spacer)

    except NotImplementedError:
        print("What the hell is this")

#    ipdb.set_trace()

