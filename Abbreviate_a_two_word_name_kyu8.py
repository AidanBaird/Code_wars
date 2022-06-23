# # Abbreviate a two word name
# turn the string into a list by spliting it
# Create a variable N containing only the first letter of the two names and put a "." between
# Return n.title() to ensure that every letter is always capitalised

def abbrev_name(name):
    list = name.split()
    n = str(list[0][0] + "." + list[1][0])
    return n.title()