# # Define the suit the card comes from
# If statement that checks the last character on the  string in question and returns the appropriate suit

def define_suit(card):
    if card[-1] == "C":
        return "clubs"
    elif card[-1] == "D":
        return "diamonds"
    elif card[-1] == "H":
        return "hearts"
    elif card[-1] == "S":
        return "spades"
    else:
        return "Error"