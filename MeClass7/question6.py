import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="jsonrpc",
    host="nxos1.lasthop.io",
    username="pyclass",
    password="88newclass",
    transport="https",
    port=8443,
    verify=False,
)

cmds = ["show interface Ethernet1/1"]
output = device.show_list(cmds)
#print(output)

outputdata = output[0]['result']['TABLE_interface']['ROW_interface']

print(f"Interface: {outputdata['interface']}; "
        f"State: {outputdata['admin_state']}; "
        f"MTU: {outputdata['eth_mtu']}")

