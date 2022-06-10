# if statement the checks if the remainder of n divided by x and n divided by y is zero and returns True if so

def is_divisible(n,x,y):
    if n % x == 0 and n % y == 0:
        return True
    else:
        return False