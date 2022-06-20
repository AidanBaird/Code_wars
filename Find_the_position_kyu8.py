# Return the letter of the alphabet a given letter is

def position(alphabet):
    count = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter != alphabet:
            count += 1
        elif letter == alphabet:
            count += 1
            return "Position of alphabet: " + str(count)
