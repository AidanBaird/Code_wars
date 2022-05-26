# # A function that takes a single "n" and returns it in a reversed list for 1 to n in a reversed countdown order
# Creating a list range from 1 to n
# Using a for loop to add each individual number to n_list
# Reversing the list and returning it

def reverse_seq(n):
    n_range = range(1,(n+1))
    n_list = []
    for number in n_range:
        n_list += [number]
    n_reversed = reversed(n_list)
    return list(n_reversed)