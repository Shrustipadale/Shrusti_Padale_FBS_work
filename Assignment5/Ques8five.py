x=int(input("Enter number: "))
n=int(input("Enter number: "))
sum=0
for i in range(1,n+1):
    term=(x**i)/(2*x)-1
    if(i%2==0):
        sum-=term
    else:
        sum+=term
print(sum)