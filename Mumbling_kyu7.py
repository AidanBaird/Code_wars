# Turn a single string into a string where each letter is repeated as many times as it in the string and seperated by dashes

def accum(s):
    loop = 1
    list = []
    string = ""
    for letter in s:
        list.append(letter * loop)
        loop += 1
    string = '-'.join(list)
    return string.title()

