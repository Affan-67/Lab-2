def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height*height)
    if bmi < 18.5:
        print("BMI is underweight")
    elif bmi >= 18.5 and bmi <25.0:
        print("BMI is normal weight")
    else:
       print("BMI is overweight")

    return bmi

bmi_output = calculate_bmi(weight=55, height=1.60)
print("BMI = " + str(bmi_output))

