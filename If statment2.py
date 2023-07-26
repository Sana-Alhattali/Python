state = input("enter Y or N: ")
age = int(input("enter your age: "))

if ( age >= 18):
    if(state == "Y"):
       print("graduated and 18 or above year old")
    else:
       print("Not graduated and 18 or above year old")
else:
    print("under 18 year")
