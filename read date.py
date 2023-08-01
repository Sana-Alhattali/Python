def readDate():
    print("enter data: ")
    month= int(input("month:"))
    day= int(input("day:"))
    year= int(input("year:"))
    return (month,day,year)

date=readDate()
print(date)

(month,day,year)=readDate() #can print each one seprate
print(month,day,year)

    