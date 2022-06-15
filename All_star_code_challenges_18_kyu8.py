# For loop to go through the letters whilst an if loop adds to the count if the letter is the specifies code letter

def str_count(strng, letter):
    count = 0
    for let in strng:
        if let == letter:
            count += 1
    return count