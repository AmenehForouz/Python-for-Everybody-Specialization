#Problem: https://www.py4e.com/tools/python-data/?PHPSESSID=1138f7139e4422ac08c34efaf7bb34c7
import re
fhand = open('11.1.regex-sum.txt')
y =0 
line = fhand.read()
x = re.findall('[0-9]+',line)
# print(x)
for i in x:
    y = y + int(i)
print(y)
