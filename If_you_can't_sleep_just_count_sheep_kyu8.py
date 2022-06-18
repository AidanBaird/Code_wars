# # that counts "n" amount of sheeps
# various variables for later use
# While loop that appends (str(amount) + " sheep...") to the list sheep
# Adding to count and amount
# Returning the list in a joined string state

def count_sheep(n):
    count = 0
    amount = 1
    sheep = []
    while count < n:
        sheep.append(str(amount) + " sheep...")
        count += 1
        amount += 1
    return ''.join(sheep)