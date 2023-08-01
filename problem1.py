#problem: sara and quezis
n = int(input("number of subject: "))
x = int(input("number of needed days: "))
y = int(input("number of days left to first exam: "))

if (n * x <= y):
    print("achieve goal")
else:
    print(" fail")