def area_or_perimeter(length , width):
    area = 0
    perimeter = 0
    if length == width:
        area = (length * width)
        return area
    else:
        perimeter = ((length + width) * 2)
        return perimeter