# A function that takes an array, uses a for loop to seperate each number from the array and then adds the number to the "total" each loop


def sum_array(a):
    total = 0.0
    for number in a:
        total += number
    return total