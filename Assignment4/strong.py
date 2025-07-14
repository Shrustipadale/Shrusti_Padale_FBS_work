# WAP to check if the gien number is a strong number
num = int(input("Enter number: "))
temp=num
sum=0
while(num>0):
    a=num%10
    num//=10
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    sum=sum+fact
if(sum==temp):
        print("It is a strong number")

else:
        print("It is not a strong number")

