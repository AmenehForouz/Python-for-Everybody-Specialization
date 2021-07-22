## Programming for Everybody (Getting Started with Python)

www.py4e.com
book: https://www.py4e.com/book
podcast: https://podcasts.apple.com/us/podcast/python-for-everybody-audio-py4e/id1214665693

The print statement in python2 has become the print function in python 3
the line in Python 2: print "hello world"
is as follows in Python 3: print("hello world")

The raw_input function has also changed to input,
raw_input('What is your name?') in python 2
input('What is your name?') in python 3

python2  http://www.pythonlearn.com/.

Logged in as: c8983fb95659981ce279dd9c5ed42b60 vidyasonawane20@gmail.com Vidya Sonawane.

1.1 Why program:
as a programmer is to intermediate between the hardware and the end user.
Sakai, which millions of people use around the world, teaching and learning. 
And so as a programmer, you're going to write code and that code is going to use data, networks, and CPUs, and memory, and then do something for the user. 
a program is like a sequence of stored instructions. And the idea is that the computer itself at the lowest level in the hardware is just not that smart. But it has a lot of flexibility in that if we give it the right instructions, it can do amazing things.

1.2 Hardware Overview
 input/output devices. They are the way that this computer accesses the outside world. So things like the mouse, the keyboard, right, I got a keyboard here,  humans in the outside world interact.
 the closest thing that a computer has to intelligence is this. Central processing unit, CPU is what we call them. And if you look at the back side of this CPU it is actually a circuit. It's a highly sophisticated circuit with millions of transistors on it, and you've probably heard that, millions of transistors. It runs maybe three billion instructions per second. What does that mean? Well that means that an instruction is a set of electrical pulses, maybe 32 little wires or 64 little wires. And at three billion times a second, this is programmed to ask what's next. And it pulls what's next in these little electric wires. Well, where does it get the answer to what's next? It gets the answer to what's next out of the memory. And so your program, when you write a program, let me draw this, when you write a program, you create a file on the secondary memory, like a Python file, and then at some point that is loaded into the main memory, translated, and then your program is here. And then when the CPU says what next, your program feeds its first instruction. And then when that's done, the CPU says what's next? It feeds the second instruction, third instruction, fourth instruction. It's called the fetch-execute cycle. And these two parts, the CPU and the main memory, are what participate.
 the .py file is kind of loaded and translated into the main memory. And then when the computer shuts off, all this data goes away. Secondary memory is permanent. This does not get shut off
  compiler
  an interpreter
  
1.3 Python as a programming language.
Guido van Rossum, over 20 years ago, invented this Python language
Python was not named for a snake even though we use the snake motif all the time. It turns out that what Python was named for was Monty Python's Flying Circus. And the reason was is that Guido was trying to capture an air of play. Most programming languages in the 80s when Python started were very, very serious, and very complex and you had to be really serious to figure them out, a lot of math geniuses. And Guido thought, I could probably write a programming language that wouldn't be that hard, would be fun actually, would be enjoyable to use, but let's not make it bad. Let's not make it weak, let's make it both powerful and enjoyable.

1.4 Writing paragraphs of code
assignment statement is something that often confuses people when they move from math to programming. An equal sign sort of has a direction to it; it's an arrow. It really is saying "Dear Python, you've got a lot of memory - you've got a lot of memory. Take a little tiny piece of that memory and remember it and name it x. I might use that - I'm going to use that later - and stick a 1 in it." So this is sort of like stick 1 in a spare place in memory and name it x. print (x) says, go take whatever that spare bit of memory was and bring it back out and tell me what I put in it.

reserved words: Now, what do we mean by reserved words? Well, these are words that if we use these words, we must use them to mean the thing that Python expects them to mean. Another way to put that is we can't use them elsewhere. We can't make up a variable named import. We can't make a variable named assert; because if Python sees assert, it means something very specific to Python. If it sees if, it means something. 

Sentences are lines. And so when we write a program, we're writing a text file and we put a line and another line and another line. Each one of these is like a separate line and we've got to get them right. And then we construct a paragraph out of a series of lines. 

scripts are stored sets of instruction in text files that you can then hand to Python to run them
Scripts is a series of steps. Now there are a couple of basic patterns that we use and we compose them. 
The most basic pattern is what's called **sequential**. We do one thing, then we do the next thing, then we do the next thing. 
**Conditional** is sort of intelligent where you're doing something and then may or may not be doing something.you have this "if". If this is true, do this statement; if it's false, do some other statement. Those are called conditional steps 
when we have a series of steps that need to be **repeated**. while and for loop using iterative variables.
And then the fourth pattern is the **store and retrieve** pattern, 


Quiz:
When Python is running in the interactive mode and displaying the chevron prompt (>>>) - what question is Python asking you?
- What Python script would you like me to run? 

What is the proper way to say “good-bye” to Python? - quit()

What is the best way to think about a "Syntax Error" while programming?
- The computer did not understand the statement that you entered

