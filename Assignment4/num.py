#WAP to print all numbers in a range divisible by a given number.
start=int(input("Enter number: "))
stop=int(input("Enter number: "))
div=int(input("Enter divisor: "))
for x in range(start,stop+1):
    if(x%div==0):
        print(x) 
    