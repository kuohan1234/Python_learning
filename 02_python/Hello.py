#!/usr/bin/python
import re

line = "Cats are smarter than dogs";

# flag: re.m (mutliple-line) ; re.I (ignore-case)
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")
"""   
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print (dict.get("Name"))
print ("dict ['Name']", dict['Name'])
"""

value = eval(input("what is the number you want to duoble"))
print(value*2)
