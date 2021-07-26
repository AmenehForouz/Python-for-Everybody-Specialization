# Problem: https://www.py4e.com/tools/python-data/?PHPSESSID=8e93963cf2851dd265da4258fed9be35

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1316160.html'
htmlpage = urllib.request.urlopen(url).read()
# print(htmlpage)
s = BeautifulSoup(htmlpage, 'html.parser')

svar = 0
tags = s('span')
for tag in tags:
    # num = tag.text
    svar = svar + int(tag.contents[0])
print(svar)