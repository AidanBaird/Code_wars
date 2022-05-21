# # A function that either returns a number timesed by 50 add 6 or an error if it is a string

def problem(a):
    string = ""
    integer = 0
    float = 0.0
    if type(a) == type(integer) or type(a) == type(float):
        return (a * 50) + 6
    if type(a) == type(string):
        return "Error"