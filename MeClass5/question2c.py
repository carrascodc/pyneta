from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from netmiko import ConnectHandler
from mydevices import nxos1, nxos2
from pprint import pprint
import textfsm
import time
import re
from colorama import Fore, Back, Style

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/")

template_file = "question2.j2"
interface = "1"

nxos1_vars = {
    "device_name": "nxos1",
    "local_as": 22,
    "interface": interface,
    "ip_address": "10.1.100.1",
    "netmask": "24"
}

nxos2_vars = {
    "device_name": "nxos2",
    "local_as": 22,
    "interface": interface,
    "ip_address": "10.1.100.2",
    "netmask": "24"
}

nxos1_vars["peer_ip"] = nxos2_vars["ip_address"]
nxos2_vars["peer_ip"] = nxos1_vars["ip_address"]

# Add Jinja2 vars to be included in the Netmiko device dictionary
nxos1["j2_vars"] = nxos1_vars
nxos2["j2_vars"] = nxos2_vars

template = env.get_template(template_file)

def config():
    for device in [nxos1,nxos2]:
        ### Pop the device dict 'j2_vars' to 'device_var',
        ### leaving 'device' with just the netmiko parameters
        device_var = device.pop('j2_vars')
        cfg = template.render(**device_var)

        Node = {
        "host": device['host'],
        "username": device['username'],
        "password": device['password'],
        "device_type": device['device_type']
        }
        net_connect = ConnectHandler(**Node)
        print(f"Updating {device['host']} ".center(80, "#"))
        output = net_connect.send_config_set(cfg)
        print('Completed' + '\n')

def verify():
    for device in [nxos1,nxos2]:
        Node = {
        "host": device['host'],
        "username": device['username'],
        "password": device['password'],
        "device_type": device['device_type']
        }
        net_connect = ConnectHandler(**Node)
        raw_text_data = net_connect.send_command('show ip bgp sum')
        net_connect.disconnect()

        textfsm_file = "templates/question3.template"
        textfsm_template = open(textfsm_file)

    #    with open("show_ip_bgp_sum.txt") as f:
    #        raw_text_data = f.read()

        # The argument 'template' is a file handle and 'raw_text_data' is a string.
        re_table = textfsm.TextFSM(textfsm_template)
        bgp_status = re_table.ParseText(raw_text_data)[0][0]
        bgp_state = re_table.ParseText(raw_text_data)[0][1]
        textfsm_template.close()

        ### Regular expressions to match the bgp variables above
        regex_status = re.compile(r'[0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}')
        regex_state = re.compile(r'\d+')

        if regex_status.match(bgp_status) and regex_state.match(bgp_state):
            ''' These two conditions are to match
                - Whether or not there is an time counter
                - Whether or not the bgp state is a number, and NOT a building bgp state
            '''
            print(f"BGP has been established on: {device['host']}")
        else:
            print(f"The current BGP State of {device['host']} is: {bgp_state}. Please review")

def run():
    config()
    time.sleep(15)
    verify()

if __name__ == "__main__":

    run()
    
