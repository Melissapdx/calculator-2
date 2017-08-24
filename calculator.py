"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.

# No setup
repeat forever:
    read input
    tokenize input
    if the first token is "q":
        quit
    else:
        decide which math function to call based on first token
"""

from arithmetic import *

def my_reduce(f, list1):
    """ Function that takes in a function and a list
    and does the same as the python reduce function """
    ans = list1[0]
    for i in list1[1:]:
        ans = f(ans, i)
    return ans

while True:
    user_input = raw_input(">")
    tokens = user_input.split(" ")
    if tokens[0] == "q":
        break
    elif tokens[0] == "+":
        print reduce(add, make_list_into_float(tokens[1:]))
    elif tokens[0] == "-":
        print reduce(subtract, make_list_into_float(tokens[1:]))
    elif tokens[0] == "*":
        print reduce(multiply, make_list_into_float(tokens[1:]))
    elif tokens[0] == "/":
        print reduce(divide, make_list_into_float(tokens[1:]))
    elif tokens[0] == "square":
        print square(float(tokens[1]))
    elif tokens[0] == "cube":
        print cube(float(tokens[1]))
    elif tokens[0] == "pow":
        print reduce(power, make_list_into_float(tokens[1:]))
    elif tokens[0] == "mod":
        print reduce(mod, make_list_into_float(tokens[1:]))
    else:
        print "not a valid option"
