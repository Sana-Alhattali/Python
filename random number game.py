import random
num1 = (random.randrange(1,100))
#num1 = print(random.randint(1,100))
while 1:
    num=int(input("enter number: "))
    if num==num1:
       print("correct")
       break
    elif num<num1:
       print("go upper")
    else:
       print("go lower")
    

