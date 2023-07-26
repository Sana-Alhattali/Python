#if else statment
num1 = float(input("enter number 1: "))
num2 = float(input("enter number 2: "))
opr = input("entr operator: ")

if (opr == '+'):
     print(num1 + num2)
elif (opr == '-'):
     print(num1 - num2)
elif (opr == '*'):
     print(num1 * num2)
elif (opr == '/'):
     print(num1 / num2)
else:
    print("invalid operator")
    
