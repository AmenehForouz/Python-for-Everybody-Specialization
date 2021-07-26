# Programs that Surf the Web

**Unicode characters and strings**
- **ASCII** - American Standard code for Information Interchange (128 characters)
- ASCII originally used seven bits to encode each character. This was later increased to eight with Extended ASCII to address the apparent inadequacy of the original.
- ord() function to get the ascii value of character. print(ord('H)) - 72
- In 1960's and 70's , we just assumed that one byte was one character.


- **unicode**
- major advantage of Unicode is that at its maximum it can accommodate a huge number of characters. Because of this, Unicode currently contains most written languages and still has room for even more.
- ASCII uses an 8-bit encoding while Unicode uses a variable bit encoding like 32, 16, and 8-bit encodings.
- UTF - Unicode transformation format
- UTF-16 - FIXED LENGTH - 2 BYTES
- UTF-32 - fixed length - 4 bytes
- UTF-8 - 1-4 bytes
    - upwards compatible with ascii
    - automatic detection between ascii and utf-8
    - **utf-8 is recommended practice for encoding data to be exchanged between systems.**

**Python2 and Python3 difference**
- In python2, type of unicode string is 'unicode'
- In python3, type of unicode string is 'str' -> in python3, all strings are unicode.

- In python2, type of byte string is 'str'
- In python3, type of byte string is 'bytes'

- **In python2**
```
    ustr = u'ʑʒʓ'
    print(type(ustr)) ...<class 'unicode'>

    bstr = b'csjk'
    print(type(bstr)) .... <class 'str'>
```

- **In python3**
```
    ustr = u'ʑʒʓ'
    print(type(ustr)) ...<class 'str'>

    bstr = b'csjk'
    print(type(bstr)) .... <class 'bytes'>
```

**urllib in Python**
- since HTTP is so common, we have a library that does all the socket work for us and makes web pages looks like a **file.**

```
    import urllib.request, urllib.parse, urllib.error

    fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
    for line in fhand:
        print(line.decode().strip())
```

- counting the words from html file:
```
    import urllib.request, urllib.parse, urllib.error

    fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
    di = dict()

    for line in fhand:
        words = line.decode().split()
        for word in words:
            di[word] = di.get(word, 0) +1
    print(di)
```

**Web Scraping**
- when a program or script pretends to be a browser and retrives web pages, looks at those web pages, extracts information and then looks at more web pages.
- search engines scrape web pages - we call this "spidering the web" or "web crawling"

**beautiful soup**
- Beautiful Soup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files.

```
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup

    url = input('Enter - ')
    htmlpage = urllib.request.urlopen(url).read()
    s = BeautifulSoup(htmlpage, 'html.parser')

    tags = s('a')   # pull out <a> anchot tags
    for tag in tags:
        print(tag.get('href',None))

    output:
    Enter - http://www.dr-chuck.com/page1.html    
    http://www.dr-chuck.com/page2.htm
```

**pip fullform** - python install process
