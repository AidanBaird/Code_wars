def bmi(weight, height):
    body_mass_index = weight / (height ** 2)
    if body_mass_index <= 18.5:
        return "Underweight"
    elif body_mass_index <= 25:
        return "Normal"
    elif body_mass_index <= 30:
        return "Overweight"
    elif body_mass_index > 30:
        return "Obese"
    else:
        return "Error"

print(bmi(50, 1.80))
print(bmi(80, 1.80))
print(bmi(90, 1.80))
print(bmi(110, 1.80))
print(bmi(50, 1.50))