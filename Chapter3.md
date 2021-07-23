# Conditional Statements

**if statement**
``` x = 5 
    if x < 10:
        print('Smaller')
    if x > 20:
        print('Bigger')
    print('finish')
```
For one liners, we can also write it as 
``` 
if x > 20: print('Bigger') 
```

**Comparison Operators**
- less than - <
- less than or equal to - <=
- equal to - ==
- greater than equal to - >=
- greater than - >
- not equal - !=

- Note: = is assignment and not comparison

**Indentation**
- Most text editors can turn tabs into spaces - make sure to enable this feature
- Python cares a lot about how far a line is indented, If you mix tabs and spaces, you may get indentation err even if everything looks fine.
- best practice is to use 4 spaces than tabs

**Two way decisions: If else**
- we chose between two, either this or that not both at a time
``` x = 4
    if x > 2:
        print('Bigger')
    else:
        print('Smaller')     
```

**Multi-way: if elif else**
- execute only one of the three or more (when we add multiple elif)
``` x = 5
    if x < 2:
        print('Small')
    elif x < 10:
        print('Medium')  
    else:
        print('Large')   
```

**try except block**
- when the conversion fails it just drops into except clause and program continue.
- It won't execute the statements after the failed statements in try block. As soon as err occures it jumps to except block.

```
a = input ('Enter number')
try:
    ival = int(a)
    print(a) # if a is not number, this statement won't work
except:
    print('Entered value is not number')
```
