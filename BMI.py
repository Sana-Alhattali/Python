weight = int(input("enter the weight: "))
height = int(input("enter the height: "))
height = height*100
BMI = weight / height**2
print(BMI)

if ( BMI < 18.5):
    print("Underweight")
elif (18.5 <= BMI <= 25.0 ):
    print("Normal")
elif (25.0 <= BMI <= 30.0 ):
    print("Overweight")
elif (30.0 <= BMI ):
    print("obese")


