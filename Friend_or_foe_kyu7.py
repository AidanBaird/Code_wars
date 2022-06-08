# People with four letter names are your only friends and this function checks if they are friendly or not

def friend(x):
    friend = []
    for person in x:
        if len(person) == 4:
            friend.append(person)
    return friend
