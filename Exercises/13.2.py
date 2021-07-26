# Problem: https://www.py4e.com/tools/python-data/?PHPSESSID=f32666c9b3e5391f8b3dcac976afd705
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1316160.html'
htmlpage = urllib.request.urlopen(url).read()
# print(htmlpage)
s = BeautifulSoup(htmlpage, 'html.parser')
