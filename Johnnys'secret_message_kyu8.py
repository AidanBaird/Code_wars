# Return a greeting and if the username is Johnny return something unique for him

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)