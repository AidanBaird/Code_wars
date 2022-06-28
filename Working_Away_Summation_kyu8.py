# # # Going away for the summer to work so wont be uploading frequently
# # A function that adds up a number as it is increased by one
# Seperate variables for the individual growing number and total that is will be added into
# A while loop that adds ones to the number and adds it into the total

def summation(num):
    number = 0
    total = 0
    while number < num:
        number += 1
        total += number
    return total