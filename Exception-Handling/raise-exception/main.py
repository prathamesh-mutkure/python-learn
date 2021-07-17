
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilos: "))

try:
    if height > 3:
        raise ValueError("Human Height cannot be over 3 meters")
except ValueError as error_message:
    print(error_message)
else:
    bmi = weight / height ** 2
    print(f"Your BMI is: {bmi}")
