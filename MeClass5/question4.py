from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./templates/")

vrf_blue = {
    'vrf_name': 'blue',
    'rd_number': '100',
    'ipv4_enabled': True,
    'ipv6_enabled': True
    }

vrf_red = {
    'vrf_name': 'red',
    'rd_number': '200',
    'ipv4_enabled': True,
    'ipv6_enabled': True
    }

vrf_yellow = {
    'vrf_name': 'yellow',
    'rd_number': '300',
    'ipv4_enabled': True,
    'ipv6_enabled': True
    }

vrf_green = {
    'vrf_name': 'green',
    'rd_number': '400',
    'ipv4_enabled': True,
    'ipv6_enabled': True
    }

vrf_orange = {
    'vrf_name': 'orange',
    'rd_number': '500',
    'ipv4_enabled': True,
    'ipv6_enabled': True
    }

vrfs = [vrf_blue, vrf_red, vrf_yellow, vrf_green, vrf_orange]

template_file = "question4.j2"
template = env.get_template(template_file)

for instance in vrfs:
    output = template.render(**instance)
    print(output)

