# Work out the price of a rental car that costs £40 a day, you get 20 off if you hire for three or more days and 50 off if you hire for 7 or more
# Find the overall cost without reductions by timsing days by 40
# Subtract reductions based on length of days

def rental_car_cost(d):
    cost = (d * 40)
    if d >= 3:
        cost -= 20
    if d >= 7:
        cost -= 30
    return cost