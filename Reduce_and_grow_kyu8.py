# Create a variable to return later, making sure it's an int and can be used in the later equation
# A for loop that will go through each number and then times the num in the arr and times them all seperately

def grow(arr):
    number = 1
    for num in arr:
        number = number * num
    return number