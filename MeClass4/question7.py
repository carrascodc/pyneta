#!/usr/bin/env python

from pprint import pprint
import textfsm

template_file = "question7.template"
template = open(template_file)

with open("question1.txt") as f:
    raw_text_data = f.read()

# The argument 'template' is a file handle and 'raw_text_data' is a string.
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)
template.close()

print("\nPrint the header row which could be used for dictionary construction")
print(re_table.header)

answer = []
for x in data:
    answer.append({'DUPLEX': x[0], 'PORT_NAME': x[1], 'PORT_TYPE': x[2], 'SPEED': x[3], 'STATUS': x[4], 'VLAN': x[5]})

pprint(answer)

