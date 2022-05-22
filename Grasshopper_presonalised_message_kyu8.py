# A function that works out who is logging into the computer and greets them accordingly

def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"