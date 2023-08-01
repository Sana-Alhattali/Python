x = int(input("write number:"))

def total(*args):
    sum = 0
    for i in args:
        sum= sum + i
    return sum

print(total(x))


