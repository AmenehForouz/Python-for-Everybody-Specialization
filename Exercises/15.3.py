# problem: https://www.py4e.com/tools/python-data/?PHPSESSID=b127bc81017568e6f4543ae7e241c115
# extracting data from json
import json
import urllib.request
count = 0

url = "http://py4e-data.dr-chuck.net/comments_1316163.json"
print ("retrieving URL")
uh = urllib.request.urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number
print (count)