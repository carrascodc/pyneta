from lxml import etree
import xml.etree.ElementTree
from pprint import pprint

file = 'show_version.xml'
xmlfromfile = open(file, 'rb').read().strip()

xmldata = etree.fromstring(xmlfromfile)

print('\n')
print('Example 5a')
print(xmldata.nsmap['nf'])

print('\n')

print('Example 5b')
print(xmldata.find('.//{*}proc_board_id').text)
print('\n')

