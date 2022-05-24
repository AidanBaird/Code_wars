# # A function that foes arithmetic with two numbers and an operator in string form.
# Works out the correct operator by using ifs then returns

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    else:
        return "Error"