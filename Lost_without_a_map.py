def maps(a):
    b = []
    index = 0
    for num in a:
        b.append((a[index]) * 2)
        index += 1
    return b

print(maps([1, 2, 3, 4]))