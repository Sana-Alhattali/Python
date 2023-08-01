#CHECK THE VALID CARD NUMBER
string =input("enter number in formate xxxx 3digit: ")
position=0
valid = len(string)==8
print(valid)
if valid and string[0:4]=='XXXX' and string[4]==" " and string[5:].isdigit():
    print(string ,"is valid")
else:
   print(string ,"is not valid")

