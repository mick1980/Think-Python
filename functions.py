# 3 FUNCTIONS

# 3.1 Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display

def right_justify(s):
    rjstr = ' '*(70-len(s)) + s
    print (rjstr)

# right_justify('hello')

# 3.2 A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is a function that takes a function object as an argument and calls it twice:

# def do_twice(f):
#   f()
#   f()

# 3.2.1 Type this example into a script and test it

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')

# do_twice(print_spam)

# 3.2.2 Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.

def do_func_twice(f,a):
    f(a)
    f(a)

# 3.2.3 Copy the definition of print_twice from earlier in this chapter to your script

def print_twice(b):
    print(b)
    print(b)

# 3.2.4 Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument

# do_func_twice(print_twice,'spam')

# 3.2.5 Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.

def do_four(f,a):
    do_func_twice(f,a)
    do_func_twice(f,a)
  

# do_four(print,'spam')

# 3.3 Note: this exercise should be done using only the statements and other features we have learned so far.

# 3.3.1 Write a function that draws a grid like the following:

# + - - - - + - - - - + 
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - + 
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a comma-seperarted sequence of values:
# print('+','-')
# By default, print advances to the next line, but can override that behaviour and put a space at the end, like this:
# print('+', end=' ')
# print(' ')
# The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.

def grid2x2():
    corner = '+'
    hspacer = ' -'
    vspacer = '|'
    boxw = 4
    boxh = 4
    gridw = 2
    gridh = 2
    hsegment = corner + hspacer * boxw + ' '
    hor1 = hsegment * gridw + corner
    hor2 = ((vspacer + '  '*(boxw) + ' ') *gridw) + vspacer
    
    print(hor1)    
    print(hor2)
    print(hor2)
    print(hor2)
    print(hor2)
    print(hor1)    
    print(hor2)
    print(hor2)
    print(hor2)
    print(hor2)
    print(hor1)    

grid2x2()