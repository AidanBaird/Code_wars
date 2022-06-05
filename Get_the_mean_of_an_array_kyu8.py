# Find the mean of an array rounded down

import math


def get_average(marks):
    total = 0
    for number in marks:
        total += number
    return math.floor(total / len(marks))

