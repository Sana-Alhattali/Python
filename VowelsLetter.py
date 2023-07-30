#print the number of vaul letter
s= "hello python"
count = 0
vl = ("a","e","u","i","o")
for i in s:
    if (i in vl):
        count+=1
print(s)
print("number of vaul letter: " ,count)