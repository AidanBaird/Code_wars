# Convert the code into morse, anything less than 5 is 0
# Anything 5 or up is a 1

def fake_bin(x):
    morse = []
    for num in x:
        if num < "5":
            morse += "0"
        else:
            morse += "1"
    return (''.join(morse))