def Year():
 year=int(input("Enter the year: "))
 if(year%4==0 or year%100==0 or year%400==0):
    return"It is a leap year"


 else:
    return"It is not a leap year"
 
print(Year())


