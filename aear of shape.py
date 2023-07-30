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

n = int(input("choose number 1-5: "))

if n==1:
    l= int(input("enter the length: "))
    print(sequareArea(l))
elif n==2:
    r= int(input("enter the radis: "))
    print(circleArea(r))
elif n==3:
    l= int(input("enter the length: "))
    w= int(input("enter the width: "))
    print(RectangleArea(l,w))
elif n==4:
    r= int(input("enter the radis: "))
    h= int(input("enter the hight: "))
    print(cylinderArea(r,h))
elif n==5:
    l= int(input("enter the length: "))
    h= int(input("enter the hight: "))
    print(traingleArea(l,h))



