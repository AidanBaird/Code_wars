# # Working out if you'll have enough gas left to get to the next gas station
# Check if distance to gas pump to pump is greater than the miles per gallon timeds by gallons and if so return True else return false

def zero_fuel(dtp, mpg, fuel_left):
    if dtp <= (mpg * fuel_left):
        return True
    else:
        return False