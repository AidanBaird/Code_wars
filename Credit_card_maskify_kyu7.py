# Hiding all but the four last digits of a string

def maskify(cc):
    last_digits = cc[-4:]
    hashtags = "#" * (len(cc) - 4)
    hidden_cc = hashtags + last_digits
    print(last_digits)
    return hidden_cc