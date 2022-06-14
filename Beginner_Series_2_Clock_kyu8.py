# Using hours minutes and second return the miliseconds since midnight

def past(h, m, s):
    result_s = (s * 1000)
    result_m = (m * 60000) + result_s
    result_h = (h * 3600000) +  + result_m
    return result_h