# A function that takes a list of True or Falses and returns the number of Trues

def count_sheeps(sheep):
    sheeps = 0
    for element in sheep:
        if element == True:
            sheeps += 1
    else:
        pass
    return sheeps
