# Find the lowest number in the array

def find_smallest_int(arr):
    ordered = sorted(arr)
    print(ordered)
    return ordered[0]