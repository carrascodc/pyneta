from __future__ import unicode_literals, print_function
import xmltodict
import ipdb
from pprint import pprint


def file_to_xmldict (file):
    with open (file) as data:
        xmldict = xmltodict.parse(data.read().strip())
    data.close()
    return(xmldict)


if __name__ == "__main__":

    zone_file = 'show_security_zones.xml'
    trust_file = 'show_security_zones_trust.xml'

    xml_zones = file_to_xmldict(zone_file)
    trust_zones = file_to_xmldict(trust_file)


