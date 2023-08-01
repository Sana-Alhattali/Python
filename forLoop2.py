
for i in range(1,10,1):
    if(i>=6):
        i-=2
    for j in range(1,i+1):
        if(j>=6):
          j-=1
        print("*", end=" ")
    print(" ")
   