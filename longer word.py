n=int(input("number of length: "))
str=input("enter the text: ")
newlist = []
text = str.split(" ")
for i in text:
    if len(i) > n:
        newlist.append(i)
print(newlist)