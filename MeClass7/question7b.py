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

cmds = ["show system uptime", "show system resources"]
output = device.show_list(cmds)

command1 = output[0][0].getchildren()
command2 = output[1][0].getchildren()

print('\n')
print('show system uptime')
print('*'*80)
for x in command1:
    print(x.tag + '\t' + x.text)

print('\n')
print('show system resources')
print('*'*80)
for x in command2:
    print(x.tag + '\t' + x.text)
#print(command2)

