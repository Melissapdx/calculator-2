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
        print "{:.2f}".format(my_reduce(add, make_list_into_float(tokens[1:])))
    elif tokens[0] == "-":
        print "{:.2f}".format(my_reduce(subtract, make_list_into_float(tokens[1:])))
    elif tokens[0] == "*":
        print "{:.2f}".format(my_reduce(multiply, make_list_into_float(tokens[1:])))
    elif tokens[0] == "/":
        print "{:.2f}".format(my_reduce(divide, make_list_into_float(tokens[1:])))
    elif tokens[0] == "square":
        print "{:.2f}".format(square(float(tokens[1])))
    elif tokens[0] == "cube":
        print "{:.2f}".format(cube(float(tokens[1])))
    elif tokens[0] == "pow":
        print "{:.2f}".format(my_reduce(power, make_list_into_float(tokens[1:])))
    elif tokens[0] == "mod":
        print "{:.2f}".format(my_reduce(mod, make_list_into_float(tokens[1:])))
    else:
        print "not a valid option"
