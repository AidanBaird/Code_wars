# # A function that works out if any given number is a square number
# Various previous attempts
# Import math
# If statement that ensures we're only working with positive numbers
# Variable that temporarily stores the square root of n
# Forces the square root to be an int and times is by itself to work out if n is a square number

import math


def is_square(n):
    # squares = []
    # ranges = range(0,999)
    # for number in ranges:
    # squares += ([number * number])
    # print(n)
    # if n in squares:
    # return True
    # elif n < 0:
    # return False
    # else:
    # return False

    # if n < 0:
    # return False
    # if n >= 0:
    # root = math.sqrt(n)
    # root_type =  type(root)
    # print(root)
    # print(root_type)
    # if root_type is int:
    # return True
    # else:
    # return False

    if n < 0:
        return False
    if n >= 0:
        root = math.sqrt(n)
        if int(root) * int(root) == n:
            return True
        else:
            return False