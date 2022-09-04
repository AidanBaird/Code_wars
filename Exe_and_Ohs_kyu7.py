# Checking if there are the same amount of exes and ohs in a string

def xo(s):
    s = s.lower()
    countx = 0
    counto = 0
    for element in s:
        if element is "x":
            countx += 1
    for element in s:
        if element is "o":
            counto += 1
    if countx == counto:
        return True
    else:
        return False