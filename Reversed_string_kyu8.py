# # A function that takes a string and returns it in reverse
# Reverse the string and use a for loop to add the reversed letters to another string

def solution(string):
    rev = reversed(string)
    string_1 = ""
    for letter in rev:
        string_1 += letter
    return string_1