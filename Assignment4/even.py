#WAP to print all even numbers until n.

start=int(input("Enter number: "))
stop=int(input("Enter number: "))
i=start

for i in range(start,stop):
    if(i%2==0):
        print(i)