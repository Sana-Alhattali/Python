#choose number and show the aear of the shape
from math import pi

def sequareArea(length):
    sArea = length*length
    return sArea

def circleArea(radis):
    cArea = pi * radis**2
    return cArea

def RectangleArea(length, width):
    rArea = length * width
    return rArea

def cylinderArea(radis, hight):
    cylArea = (2*pi * radis * hight) + (2*pi * radis**2)
    return cylArea
    
def traingleArea(length, hight):
    tArea = 0.5 * length *hight
    return tArea

n = 1
while(n<=5):
    x = int(input("choose number 1-5: ")) 
    if x==1:
        l= int(input("enter the length: "))
        print(sequareArea(l))
    elif x==2:
        r= int(input("enter the radis: "))
        print(circleArea(r))
    elif x==3:
        l= int(input("enter the length: "))
        w= int(input("enter the width: "))
        print(RectangleArea(l,w))
    elif x==4:
        r= int(input("enter the radis: "))
        h= int(input("enter the hight: "))
        print(cylinderArea(r,h))
    elif x==5:
        l= int(input("enter the length: "))
        h= int(input("enter the hight: "))
        print(traingleArea(l,h))
    else:
        print("more than range")


