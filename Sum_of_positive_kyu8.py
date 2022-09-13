# Using onlt the positive numbers from a given array add them all together and return the sum of all positive numbers

def positive_sum(arr):
    sum = 0
    for number in arr:
        if number > 0:
            sum  += number
    return sum