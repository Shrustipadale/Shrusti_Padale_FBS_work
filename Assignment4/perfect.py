#WAP to check if given number is Perfect Number.
n=int(input("Enter number: "))
sumofdivisors=0

for i in range(1,n):
    if(n%i==0):
        sumofdivisors+=i
    
if(sumofdivisors==n):
        print("It is a perfect number")
else:
        print("It is not a perfect number")

        