"""Write Python code that go throw all numbers from 1 to 30 and print True
if the number is prime and False if not.The output format should be like the following:"""
print("Number | Prime status")
print("-----------------------")
for i in range (1,30+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                print(i,"  |  ","false")
                break
        else:
           print(i,"  |  ","true")
    else:
        print(i,"  |  ","false")
    