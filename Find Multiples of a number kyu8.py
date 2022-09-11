# Given two numbers return a list of all the multiplication up tothe limit given the first integer

def find_multiples(integer, limit):
    list = []
    multiples = int((limit / integer))
    count = 0
    while count < multiples:
        count +=1
        list.append(integer * count)
    print(multiples)
    return list