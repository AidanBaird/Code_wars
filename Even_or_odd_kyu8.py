# Return "Even" for every even number and "Odd" for every odd one

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    elif number % 2 == 1:
        return "Odd"
    else:
        return "Error"