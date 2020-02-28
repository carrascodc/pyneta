from lxml import etree
import xml.etree.ElementTree

file = 'show_security_zones.xml'
xmldata = etree.parse('show_security_zones.xml')

print('\n')
print('Find tag of the first zones-security element')
print('-'*80)
print(xmldata.find('zones-security').tag)
print('\n')

print('Find tag of all child elements of the first zones-security element')
print('-'*80)

for child in xmldata.getroot().getchildren()[0]:
    print(child.tag)

print('\n')
