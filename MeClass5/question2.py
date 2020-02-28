from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/")

nxos1_vars = {
    "interface": 1, "ip_address": "10.1.100.1", "netmask": 24, "peer_ip": "10.1.100.2"}

nxos2_vars = {
    "interface": 1, "ip_address": "10.1.100.2", "netmask": 24, "peer_ip": "10.1.100.1"}

for j2_vars in (nxos1_vars, nxos2_vars):
    template_file = "question2.j2"
    template = env.get_template(template_file)
    output = template.render(**j2_vars)
    print(output)


