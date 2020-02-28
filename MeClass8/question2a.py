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
    # Devices we are testing
    devices = [cisco3, arista1]

    '''
        for device in devices:
            #ipdb.set_trace()
            print('\n')
            print(device['hostname'])
            print(spacer)
            napalm_conns = open_napalm_connection(device)
            pprint(napalm_conns.get_facts())
            print('\n' + 'Platform: ' + napalm_conns.platform)
            print(spacer + '\n' + spacer)
    '''

    conn_obj_list = list()

    for device in devices:
        #ipdb.set_trace()
        conn_obj_list.append(open_napalm_connection(device))

    for obj in conn_obj_list:
        print('\n')
        pprint(obj.get_facts()['hostname'])
        print(spacer)
        pprint(obj.get_arp_table())
        print(spacer + '\n' + spacer)


#    ipdb.set_trace()
