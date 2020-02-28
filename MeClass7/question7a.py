import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint
from nxapi_plumbing import Device

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

device = Device(
    api_format="xml",
    host="nxos1.lasthop.io",
    username="pyclass",
    password="88newclass",
    transport="https",
    port=8443,
    verify=False,
)

cmds = ["show interface Ethernet1/1"]
output = device.show_list(cmds)

#outputdata = output[0].getchildren()[0].getchildren()[0].getchildren()[0].getchildren()
#outputdata = output[0][0][0][0].findall('.//')
data_int = output[0][0][0][0].findall('.//interface')[0].text
data_state = output[0][0][0][0].findall('.//state')[0].text
eth_mtu = output[0][0][0][0].findall('.//state')[0].text

print(f"Interface: {data_int}; "
        f"State: {data_state}; "
        f"MTU: {eth_mtu} "
        )


