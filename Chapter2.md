# Expressions

**Constants**
- fixed values such as numbers, letters and strings are constants because their value does not change.
- String constants use single or double quotes print('hello world')
- numeric contants are as you expect print(123), print(98.6)

**Reserved Words**
- cannot use as variable names / identifiers

False	def	    if	    raise
None	del	    import  return
True	elif	in	    try
and	    else	is	    while
as	    except	lambda	with
assert	finally	nonlocal	yield
break	for	    not	    class
from	or	    continue 
global	pass

**Variables**
- variable is named plave in the memory where a programmer can store data and later retrive the data using the variable name.
- we can change the content of variable in later statement
- x = 5
- must start with letter or underscore
- case sensitive, vid, Vid, VID are different variables.
-  only use letters, numbers and underscore and cant start with numbers.
- Mnemonic variables means that we choose a variable name that makes sense for what we're using it for

**Sentences or Lines**
x = 2 .... Assignment statement
x = x+2 .... assignment with expression
print(x) .... print statement

**Operators**
- Arithmetic operators: +, - , *, / , ** (power). % (remainder)
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

Operator Precedence Rules :
1. Parenthesis
2. Power
3. Multiplication, division and remainder (left to right)
4. Addition and subtraction (left to right)
5. Left to Right

x = 1 + 2 ** 3 / 4 * 5
print(x) .... 11.0

**What does Type Mean ?**
- Variables, literals and constants have a type
- Python knows the difference between an integer number and string
- eg. + means addition if something is number and concatenate if something is string.
- some operations are prohibited: you cannot add 1 to string
- we cab ask Python what type something is by using **type()** function.
- type(vidya).... < class 'str' >
- type('hello').... < class 'str' >
- type(1).... < class 'int' >
- abc = abc + 1 .... traceback TypeError

**Type Conversions**
- when you put integer and floating point in an expression, integer is implicitely converted to float 
- print(float(99) + 100) ...199.0
- you can control this using built in functions int() and float()

**Integer Division** - different in python2 and python3
Python2:
- print(10/2) .... 5
- print(9/2) .... 4
- print(10.0/2.0) .... 5.0

Python3 (answers in floating point numbers)
- print(10/2) .... 5.0
- print(9/2) .... 4.5
- print(10.0/2.0) .... 5.0

**String Conversions**
- you can also use int() and float() to convert between strings and integers
- you will get an error if string does not contain numeric characters.
- sval = '123'
- print(int(sval) + 1) .... 124
- it sval = 'abc12' then print statement will give an ValueError.

**User input**
- we can instruct python to pause and read data from the user using the **input()** function.
- input function always returns a string. 
- name = input('who are you?') if you give input vidya then
print('welcome',name).... welcome vidya
- age = input('what is your age?') if you give input 24 then
print(type(age)) .... str

**Two type of print in python**
1. print('welcome',name) .... welcome vidya - comma adds space
2. print('welcome '+name) .... welcome vidya - need to give space while using + or concatenation

**Comments in Python**
- anything after # is ignored by python

Quiz:
Question 9
What will be the value of x when the following statement is executed: x = int(98.6) .... 98