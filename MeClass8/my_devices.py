#!/usr/bin/env python
from getpass import getpass
from pprint import pprint
from napalm import get_network_driver

# Supress SSL Certificate Warnings
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

username = 'pyclass'
password = '88newclass'

# Device definitions
cisco3 = dict(
    hostname="cisco3.lasthop.io",
    device_type="ios",
    username=username,
    password=password,
    optional_args={},
)
nxos1 = dict(
    hostname="nxos1.lasthop.io",
    device_type="nxos",
    username=username,
    password=password,
    optional_args={"port": 8443},
)
arista1 = dict(
    hostname="arista1.lasthop.io",
    device_type="eos",
    username=username,
    password=password,
)

