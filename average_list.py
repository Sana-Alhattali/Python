#print the average of score
score=[50,40,70,60,90]

def calAvrage(n):
    
    sum=0
    for i in range(len(n)):
        sum+=n[i]
        
    return sum/len(n)
print(calAvrage(score))
        
        
    
    