#WAP to print all integers upto n that aren’t divisible by 2 and 3.

start=int(input("Enter number: "))
stop=int(input("Enter number: "))


for i in range(start,stop+1):
    if(i % 2 !=0):
        if(i %3!=0):
            print(i)