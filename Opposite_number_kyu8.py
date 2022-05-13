# A function that takes a given number and converts it to the opposite.

def opposite(number):
    if number >= 0:
        return (0 - number)
    elif number < 0:
        return number * -1
    # number.pop([0])
    else:
        return "Error"