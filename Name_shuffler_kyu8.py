# Rearrange the name sur name first and forename last
# Split the name the rejoin it backwards

def name_shuffler(str_):
    split = str_.split()
    return " ".join(split[::-1])