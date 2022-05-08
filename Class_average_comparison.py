def better_than_average(class_points, your_points):
    class_size = len(class_points)
    class_total = 0
    class_average = 0
    for score in class_points:
        class_total += score
    class_average = class_total / class_size
    if class_average <= your_points:
        return True
    else:
        return False

    better_than_average([2, 3], 5)

    print(better_than_average([2, 3], 5))