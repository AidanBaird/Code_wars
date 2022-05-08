# A function that has to return a negative number that is either equal to the given negative number or the opposite of the given number

def make_negative( number ):
    if number < 0:
        return number
    else:
        return number - (number * 2)