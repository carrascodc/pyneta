#!/usr/bin/env python
from pprint import pprint
from napalm import get_network_driver
from my_devices import cisco3, nxos1, arista1
from my_functions import open_napalm_connection, create_backup
import ipdb

# Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


if __name__ == "__main__":

    spacer = ('-'*80)
    devices = [cisco3, arista1]
    conn_obj_list = list()

    cisco3_device = open_napalm_connection(cisco3)
    arista1_conn = open_napalm_connection(arista1)

    print(">>>Load config change (merge) - no commit")
    cisco3_device.load_merge_candidate(filename="cisco3.lasthop.io-loopbacks")
    print(cisco3_device.compare_config())

    print(cisco3_device.discard_config())

