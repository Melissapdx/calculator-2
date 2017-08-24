"""Math functions for calculator."""
def check_user_input(list1):
    for i in list1:
        if not i.isdigit():
            print "not a valid number please enter a number"
            return False
    return True


def make_list_into_float(list1):
    """ makes list of strings into list into list of floats """
    return [float(num) for num in list1]





def add(list1):
    """Return the sum of the two input integers."""

    return sum(list1)


def subtract(list1):
    """Return the second number subtracted from the first."""

    return list1[0]-sum(list1[1:])


def multiply(list1):
    """Multiply the two inputs together."""
    product = 1

    for i in list1:
        product = i * product
    return product


def divide(list1):
    """Divide the first input by the second, returning a floating point."""

    # Need to turn at least one argument to float for division to
    # not be integer division
    quotient = list1[0]

    for i in list1[1:]:
        quotient = quotient / i
    return quotient



def square(list1):
    """Return the square of the input."""

    # Needs only one argument

    return [num*num for num in list1]


def cube(list1):
    """Return the cube of the input."""

    # Needs only one argument

    return [num * num * num for num in list1]


def power(list1):
    """Raise num1 to the power of num and return the value."""
    ans = list1[0]

    for i in list1[1:]:
        ans = ans ** i

    return ans  # ** = exponent operator


def mod(list1):
    """Return the remainder of num / num2."""
    remainder = list1[0]

    for i in list1[1:]:
        remainder = remainder % i

    return remainder
