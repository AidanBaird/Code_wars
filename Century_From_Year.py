# Import math to use it later on

import math

# Create a function that takes a year and then returns the century for that given year

def century(year):
    # Round up the year and divide it by 100 to work out the century
    century = math.ceil(year / 100)
    return century