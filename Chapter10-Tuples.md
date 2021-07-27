# Tuples
- tuples are another kind of sequence that functions much like a list 
- list are written in [] while tuples are written in ()
- elements are indexed at 0
- tuples are immutables just like strings where lists are mutable.

```
    x = ('vidya','kunal','vicky')
    print(x[2]) ....vicky
    y = (1,9,4) .... 9
    print(max(y))
    for i in y:
        print(i) ....   1   9   4
```

**Things not to do with tuples**
- cannot sort, x.sort() gives err
- cannot append, x.append() gives err
- cannot reverse, x.reverse() gives err 
- the methods which make changes to tuple are not allowed

**Tuples are more efficient**
- since python does  not have to build tiple structures to be modifiable, they are simpler and more efficient in terms of memory use and performance than lists
- when we are using temporary variables we prefer tuples over lists.

**Tuples and assignment**
- we can put tuple on left hand side of assignment statement.
- we can even omit parentheses

```
    (x,y) = (4, 'vidya')
    print(y) .... vidya
    (a,b) = (44,88)
    print(a) .... 44
```

**Tuples and Dictionaries**
- the items() method in dictionaries returns a list of (key,value) tuples

```
    d = {'vidya':22,'kunal':33,'teju':55}
    print(d) .... {'vidya': 22, 'kunal': 33, 'teju': 55} 
    t = d.items()
    print(t) .... dict_items([('vidya', 22), ('kunal', 33), ('teju', 55)])
```

**Tuples are Comparable**
- the comparision operators work with tuples.
- it starts comparing from left hand side, if first number satisfies the condition, it won't go for next.
```
    (0,1,4)<(2,0,1) .... True
    ('vidya','sana') < ('vidya','sam') .... False
```

**Sorting lists of tuples using sorted()function**
- we can take advantage of ability to sort a list of tuples to get a sorted version of dictionary.
- using items() and sorted() functions.
- this sorts according to keys because keys are unique in dictionaries

```
    d = {'a':99,'c':77,'b':55}
    print(d.items())
    print(sorted(d.items()))

    output:
    dict_items([('a', 99), ('c', 77), ('b', 55)])
    [('a', 99), ('b', 55), ('c', 77)]
```

**sort by values instead of key**
- construct a list of tuples of the form (value, key)

```
    d = {'a':33,'c':77,'b':55}

    temp = list()
    for k,v in d.items():
        temp.append((v,k))
    print(temp)
    temp = sorted(temp,reverse=True)
    print(temp)

    output:
    [(33, 'a'), (77, 'c'), (55, 'b')]      
    [(77, 'c'), (55, 'b'), (33, 'a')]
```

**List Comprehension**
- it creates a dynamic list

```
    d = {'a':33,'c':77,'b':55}
    print(sorted([(v,k) for k,v in d.items()]))

    output:
    [(33, 'a'), (55, 'b'), (77, 'c')] 
```

Quiz:
Which of the following methods work both in Python lists and Python tuples? - index()


