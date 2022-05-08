# A function that finds the sum of an array and returns whether its total is odd or even

def odd_or_even(arr):
    total = 0
    for num in arr:
        total += num
    if total % 2 == 1:
        return "odd"
    else:
        return "even"