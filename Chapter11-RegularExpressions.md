# Regular Expressions
- also called as regex or regexp
- provides a concise and flexible means for matching strings of text, such as perticular characters, words, patterns of characters.
- a regular expression is written in a formal language that can be interpreted by **regular expression processor**

**Python Regular Expression Quick Guide**

- ^        Matches the beginning of a line
- $        Matches the end of the line
- .        Matches any character
- \s       Matches whitespace
- \S       Matches any non-whitespace character
- '*'        Repeats a character zero or more times
- *?       Repeats a character zero or more times 
         (non-greedy)
- '+'        Repeats a character one or more times
- +?       Repeats a character one or more times 
         (non-greedy)
- [aeiou]  Matches a single character in the listed set
- [^XYZ]   Matches a single character not in the listed set
- [a-z0-9] The set of characters can include a range
- (        Indicates where string extraction is to start
- )        Indicates where string extraction is to end

- https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt
- https://docs.python.org/3/howto/regex.html

**The Regular Expression Module**
- before you can use regular expressions in your program, you must import library using **"import re"**
- **re.search()** - to see if string matches regular expression, similar to using find() method for strings.
- **re.findall()** - to extract portions of string that match your regular expression, similar to a combination of find() and slicing

**using re.search() similar to find()**
```
    hand = open('8.2.mbox-short.txt')

    for line in hand:
        line = line.rstrip()
        if line.find('From:') >= 0:
            print(line)
```
is same as 
```
    import re
    hand = open('8.2.mbox-short.txt')
    for line in hand:
        line = line.rstrip()
        if re.search('From:',line):
            print(line)
```

**using re.search() line startswith()**

```
    hand = open('8.2.mbox-short.txt')
    for line in hand:
        line = line.rstrip()
        if line.startswith('From:'):
            print(line)
```
is similar to
```
    import re
    hand = open('8.2.mbox-short.txt')
    for line in hand:
        line = line.rstrip()
        if re.search('^From:',line):
            print(line)
```

**Wild card character - dot**
- the **dot** character matches any character
- if you add **asteric** character, the character is "any number of times"
- eg. **^X.*:** means line starting with X and have any character, any number of times and then :
- this will match with **X-Sieve: CMU 2.3**

**matching and Extracting data**
- re.search returns a true/false depeneding on whether the string matches the regular expression
- If we actually want the matching strings to be extracted, we use re.findall()
- [0-9]+ means one or more digits
- re.findall() returns a list of matched strings.

```
    import re
    x = 'my 2 fav numbers are 25 and 10'
    y = re.findall('[0-9]+',x)
    print(y)
    z = re.findall('[aeiou]+',x)
    print(z)

    output:
    ['2', '25', '10']
    ['a', 'u', 'e', 'a', 'e', 'a']
```

**Greedy Matching**
- the repeat characters * and + push outword in both directions(greedy) to **match the largest possible string**
```
    import re
    x = 'From: uses : character in it'
    y = re.findall('^F.+:',x)
    print(y)

    Output:
    ['From: uses :']  # not ['From:']
```

**Non Greedy Matching**
- add **?** character
```
    import re
    x = 'From: uses : character in it'
    y = re.findall('^F.+?:',x)
    print(y)

    output:
    ['From:']
```

**non whitespace character using \S**
```
    import re
    x = 'From: vidyasonawane20@gmail.com Sat Jan 25'
    y = re.findall('\S+@\S+',x)
    print(y) ....['vidyasonawane20@gmail.com']
```

```
    import re
    x = 'From: vidyasonawane20@gmail.com Sat Jan 25'
    y = re.findall('\S+@\S+?',x)
    print(y) .... ['vidyasonawane20@g']
```

**Parenthesis ()**
- parenthesis are not part of match - butr they tell where to start and stop, what string to extract
- in below eg., it will match the string starting with From: but extract only the matching string written in ()

```
    import re
    x = 'From: vidyasonawane20@gmail.com Sat Jan 25'
    y = re.findall('From: (\S+@\S+)',x)
    print(y) ....['vidyasonawane20@gmail.com']
```

```
    import re
    x = 'From: vidyasonawane20@gmail.com Sat Jan 25'
    y = re.findall('@(\S*)',x)
    print(y) .... ['gmail.com']
```

**Escape Charater - backslash**
- when you want regular expression character to behave normally, you prefix it with '\'
```
    import re
    x = 'I received $10.5 for cookies'
    y = re.findall('\$[0-9.]+',x)
    print(y) .... ['$10.5']
```

