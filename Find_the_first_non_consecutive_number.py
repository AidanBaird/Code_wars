def first_non_consecutive(arr):
    count = 0
    for num in arr:
        count += 1
        if count == num:
            continue
        if count != num:
            return num


print(first_non_consecutive(1, 2, 3, 4, 5, 6, 7, 9))