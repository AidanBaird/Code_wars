def get_grade(s1, s2, s3):
    average = (s1 + s2 + s3) / 3
    if average <60:
        return "F"
    elif average <70:
        return "D"
    elif average <80:
        return "C"
    elif average <90:
        return "B"
    elif average <= 100:
        return "A"
    else:
        return "Error"