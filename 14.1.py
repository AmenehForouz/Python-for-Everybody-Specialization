# problem: https://www.py4e.com/tools/python-data/?PHPSESSID=497ef95835911c1d4b890b109b60d17b

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1316162.xml'
xmlpage = urllib.request.urlopen(url).read()
# print(xmlpage)

tree = ET.fromstring(xmlpage)
lst = tree.findall('.//count')
# print(lst)
# print('count', len(lst))
svar =0 
for item in lst:
    # print(item.text)
    svar = svar + int(item.text)
print(svar)


