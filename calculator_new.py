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

from arithmetic_new import *

while True:
    user_input = raw_input(">")
    tokens = user_input.split(" ")
    if tokens[0] == "q":
        break
    elif check_user_input(tokens[1:]):
        if tokens[0] == "square":
            print square(make_list_into_float(tokens[1:]))
        elif tokens[0] == "cube":
            print cube(make_list_into_float(tokens[1:]))
        elif len(tokens) >= 3:
            if tokens[0] == "+":
                print add(make_list_into_float(tokens[1:]))
            elif tokens[0] == "-":
                print subtract(make_list_into_float(tokens[1:]))
            elif tokens[0] == "*":
                print multiply(make_list_into_float(tokens[1:]))
            elif tokens[0] == "/":
                print divide(make_list_into_float(tokens[1:]))
            elif tokens[0] == "pow":
                print power(make_list_into_float(tokens[1:]))
            elif tokens[0] == "mod":
                print mod(make_list_into_float(tokens[1:]))
            else:
                print "not a valid option"
        else:
            print "Not enough numbers input"
