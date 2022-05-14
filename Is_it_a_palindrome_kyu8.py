# A function that checks if a given word is a palindrone
# Reserving the string with the use of a slice [::-1] to start the word from back to front
# Ensuring both variables are lower case
# Then returning a bolean


def is_palindrome(s):
    reversed = s[::-1]
    if s.lower() == reversed.lower():
        return True
    else:
        return False
