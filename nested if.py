gender = input(" enter gender Male r Femail: ")

age = int(input("enter your age: "))

if ( gender == 'Male'):
    if ( 24 >= age <=30 ):
        print("accepted")
    else:
        print("rejcted")
else:
    print("rejcted, you are female")
