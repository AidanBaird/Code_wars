# Checking if there is enough space on a bus
# If statement that works out if the is enough capacity
# returns the lack of capacity using the negative number as an absolute

def enough(cap, on, wait):
    if cap <= ( on + wait):
        return abs(cap - (on + wait))
    else:
        return False