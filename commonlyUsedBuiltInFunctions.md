- print()
- input() - ti accept input from user
- open() - to open file and returns file handle - filehandle = open('filename','r') 
- len() - to get the length of string or lists - len('stringOrList')
- type() - to get the type of variable - var.type()
- dir() - to get the list of functions which are applicable on input string - dir('string')
- range() - range function returns a list of numbers that range from zero to one less than the parameter
- print(range(4)) .... [ 0,1,2,3], we can also use range() in for loop.
- sorted() - returns a sorted list of the specified string, list, tuple or dictionary - it works for all data structures. 
    - x = [1,2,3,8,5,3] >>> print(sorted(x)) ....[1, 2, 3, 3, 5, 8]
    - x = (1,2,3,8,5,3) >>> print(sorted(x)) ....[1, 2, 3, 3, 5, 8]
    - x = {1:'as',5:'tyu',3:'yui'} >>> print(sorted(x)) ....[1, 3, 5]
    - x = 'vidyasonawane' >>> print(sorted(x)) ....['a', 'a', 'a', 'd', 'e', 'i', 'n', 'n', 'o', 's', 'v', 'w', 'y']
- ord() - to get the ascii value of character. print(ord('H)) - 72




- **Functions applicable on strings**
    - **'capitalize'**, 'casefold', 'center', **'count'**, **'encode'**, **'endswith'**, 'expandtabs', **'find'**, 'format', 'format_map', **'index'**, 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', **'lower'**, **'lstrip'**, 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', **'rstrip'**, **'split'**, 'splitlines', **'startswith'**, 'strip', 'swapcase', 'title', 'translate', **'upper'**, 'zfill'
    - these methods can be used as string.function(), eg. data.find('@')... return the index number of @ in the data string, str.split() returns a list of words in string using space as delimeter.

**Functions applicable to lists**
    - **append()**, clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), **sort()** - lst.appent('element')

**Functions applicable to dictionaries**
    - 'clear', 'copy', 'fromkeys', **'get'**, **'items'**, **'keys'**, 'pop', 'popitem', 'setdefault', 'update', **'values'**
    - get() - dict.get('key',defaultvalue) - if key present it will return a value otherwise will return a default value.
    - dic.keys() - return the list of keys
    - dic.values() - return the list of values
    - dic.items() - return the list of tuples containing (key,value), we can use 2 iteration variables on di.items()

**Functions applicable to tuples**
    - 'count', 'index'



**Modules or libraries - use import keyword to use them in program**
- **re** - regular expression library
    - re.search() - to see if string matches regular expression - re.search('^From:',line):
    - re.findall() - to extract portions of string that match your regular expression, similar to a combination of find() and slicing - returns a list of matched strings. - findall('[aeiou]+','vidya') ....[ 'i','a']

- **socket**
    - mysocket = socket.**socket**(socket.AF_INET, socket.SOCK_STREAM)   
    - mysocket.**connect**(('host-name',port-no.))  # host and port must be tuple.
    - mysocket.**send**('reguest url'.encode()) #the argument should be in byte format, encode() is a string method.
    - bytedata.**decode()** - decode method belongs to byte class
    - mysocket.**close()**

- **urllib** - import urllib.request, urllib.parse, urllib.error
    - does all the socket work for us and makes web pages looks like a file.
    - fhand = **urllib.request.urlopen**('http://data.pr4e.org/intro-short.txt')

- **BeautifulSoup** - from bs4 import BeautifulSoup
    - Python library that is used for web scraping purposes to pull the data out of HTML and XML files.
    - htmlpage = urllib.request.urlopen(url).**read()** # if we add read() method, it will return a webpage.
    - s = BeautifulSoup(htmlpage, 'html.parser') #accepts the page and parser.

- **xml** -import xml.etree.ElementTree as ET
    - tree = ET.**fromstring**(xmldata)
    - print('Name:',tree.find('name').text) #find is string method
    - print('Attribute',tree.find('email').get('hide')) # get is dictionary method, here hide is the key and 'yes' is the value - refer the example to chapter14-xml
    - tree = ET.fromstring(xmldata)
    - lst = tree.**findall**('person') # return list of person

- **json** - import json
    - info = json.**loads**(jsondata) - returns a dictionary or list of dictionaries