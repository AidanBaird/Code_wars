# Return a string that is a case sensetive doubled version of the given string

def double_char(s):
    string = ""
    for character in s:
        string += character
        string += character
    return string