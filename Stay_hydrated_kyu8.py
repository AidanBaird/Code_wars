# # A function to work out how much water to drink if you're going to drink half a litre of water every hour
# imports math for the use of .floor
# Returns hours * 0.5 rounded down

import math

def litres(time):
    return math.floor(time * 0.5)