# Programming
- **Algorithms** - a set of rules or steps used to solve a problem
- **Data Structures** - A perticular way of organizing data in a computer.

- **What is not a collection?** - most of our variables have one value in them - when we put a new value in the variable, old value is overwritten.

# Lists
- List is a collection, collection allows us to put many values in single variable.
- friends = ['vidya','teju','sharayu']

**List Constants**
- list constants are surrounded by square brackets and elements in the list are separated by commas
- list can be empty, print([]).... []
- A list element can be any python object- even another list, print ([1, [5 ,6], 8])

**Looking inside the lists**
- just like strings, we can get single element in list using index specified in square brackets.
```
    friends = ['vidya','teju','sharayu']
    print(friends[2]) .... teju
```

**Lists are Mutable (Changable)**
- Strings are immutable- we cannot change the contents of a string - we must make new string to make any change.
- Lists are mutable = we can change an element of list using the index operator.
```
    al = [1,2,3,4,5]
    print(al) .... [1,2,3,4,5]
    al[2] = 9
    print(al) .... [1,2,9,4,5]
```

**len() function**
- just like strings, we can use len() to measure length of list, it is python built in function
```
    al = [1,2,'bob',4,'jane']
    print(len(al)) .... 5
```

**Using range() function**
- the range function returns a list of numbers that range from zero to one less than the parameter.
- we can construct an index loop using for and integer iterator.

```
    print(range(4)) .... [0,1,2,3]
    friends = ['vidya','teju','sharayu']
    print(len(friends)) .... 3
    print(range(len(friends))) .... [0,1,2]
```

**Two types of for loops**

```
    friends = ['vidya','teju','sharayu']

    for f in friends:
        print('Hey',f)

    
    for i in range(len(friends)):
        f = friends[i]
        print('Hey',f)
```

**Concatenating lists using +**
- we can create a new list by adding two existing lists together, like strings
```
    a = [2,4,6]
    b = [1,3,5]
    c = a+b
    print(c) .... [1,2,3,4,5,6]
    print(a) .... [2,4,6]
```

**Slicing using :**
- we can slice lists just like strings.
```
    a = [1,3,6,9,6,3]
    print(a[1:5]) .... [3,6,9,6]
```

**List Methods**
```
    x = [1,2,3,'bob',5]
    print(type(x)) .... list
    print(dir(x))
```
- Output of dir(x):
- append()
- clear()
- copy()
- count()
- extend()
- index()
- insert()
- pop()
- remove()
- reverse()
- sort()

**Building a List from scratch**
- we can create an empty list and then add elements using the append method.
- list stays in order and new elements are added at the end of list.
```
    x = list()
    x.append('book')
    x.append(78)
    print(x) .... ['book',78]
    x.append('cookie')
    print(x) .... ['book',78,'cookie']
```

**Is something in a list? using 'in'**
```
    a = [1,2,3,4]
    3 in a ....True
    9 in a .... False 
```

**List are in Order**
- list can hold many items and keep those items in the order until we do something to change the order.
- a list can be sorted i.e. change its order
- the sort method (unlike strings) means sort yourself

```
    a = [3,2,7,1]
    a.sort()
    print(a) .... [1,2,3,7]
    print(a[1]) .... 2
```

**Strings and Lists**
- **split()** breaks a string into parts and produces a list of strings, we think of these as words.

```
    abc = 'hello vidya and kunal'
    al = abc.split()
    print(al) .... ['hello','vidya','and','kunal']
    print(len(al)) .... 4
    print(al[0]) .... 'hello'
```
- by default, split() uses space as a delimeter.
- when you do not specify delimeter, multiple spaces are treated like one delimeter.
- you can specify which delimiter character to use in splitting. eg. split(':')


