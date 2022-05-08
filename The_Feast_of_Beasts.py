# A function that compares the first and last letter from both beast and dish and if they are both the same returns True

def feast(beast, dish):
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        print("False")
        return False