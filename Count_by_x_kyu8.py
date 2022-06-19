# Count up by x for n number of times
# Create various variables
# Use a while loop the doesn't go over n
# Linearly add x to a number and append it to a list
# Add one to the count so the while loop knows when to stop
# Return the finished list

def count_by(x, n):
    count = 0
    z = 0
    list = []
    while count < n:
        z += x
        list.append(z)
        count += 1
    return list
