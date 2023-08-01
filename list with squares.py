#This loop creates and fills a list with squares (0, 1, 4, 9, 16, ...)

def squer(n):
    new_list=[]
    for i in range(n):
        new_list.append(i**2)
    return new_list
print(squer(10))