list1=[10,20,30,90]
limit=90
pos=0
found= False
while pos < len(list1) and not found:
    if list1[pos]==limit:
        found = True
    else:
        pos+=1
if found:
    print(pos)
else:
    print("not found")
    
    
    
    