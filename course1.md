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

  
