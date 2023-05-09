# BMI calculator

height = float(input("Height (mts): "))
weight = float(input("Weight (kgs): "))

if height > 3:
    raise ValueError("Human height should not be over 3 mts")

bmi = height / (weight**2)
print(f"your BMI is {bmi}")
