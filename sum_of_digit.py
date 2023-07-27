#calculate the sum of the digits 1729
n = int(input("enter a number: "))
total = 0
while(n>0):
     digit = n%10
     total += digit
     n = n//10
print(total)
