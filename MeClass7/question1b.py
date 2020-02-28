from lxml import etree
import xml.etree.ElementTree
import ipdb
from pprint import pprint

xml_input = '''
<zones-information>
    <zones-security>
        <zones-security-zonename>trust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>1</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>vlan.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>untrust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-screen>untrust-screen</zones-security-screen>
        <zones-security-interfaces-bound>2</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>fe-0/0/0.0</zones-security-interface-name>
            <zones-security-interface-name>pt-1/0/0.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>junos-host</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>0</zones-security-interfaces-bound>
        <zones-security-interfaces>
        </zones-security-interfaces>
    </zones-security>
</zones-information>
    '''


xmldata = etree.fromstring(xml_input)


print(xmldata)
print(type(xmldata))


#ipdb.set_trace()

xmloutput = etree.tostring(xmldata).decode()
pprint(xmloutput)


