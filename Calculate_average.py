# A function that takes the length of a given list and calculates the mean average

def find_average(numbers):
    total = 0
    length = len(numbers)
    for num in numbers:
        total += num
    average = total / length
    return average