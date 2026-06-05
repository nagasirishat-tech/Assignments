def bodymassindex(weight, height):
    bmi = weight / (height ** 2)
    return bmi
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
print("welcome to the body mass index calculator")
bmi = bodymassindex(weight, height)
if bmi < 18.5:
    print("Your BMI is", bmi, "which means you are underweight.")
elif bmi < 25:
    print("Your BMI is", bmi, "which means you have a normal weight.")
elif bmi < 30:
    print("Your BMI is", bmi, "which means you are overweight.")
else:
    print("Your BMI is", bmi, "which means you are obese.")
