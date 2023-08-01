#function calculate area of Polygon
from math import tan, pi
num = int(input("enter number of sides: "))
s = float(input("enter the sides: "))

def areaPolygon(n,side):
    area = n*(side**2)/(4*tan(pi/n))
    return(area)

print(areaPolygon(num,s))
