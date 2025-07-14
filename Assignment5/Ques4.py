num=int(input("Enter the number: "))
temp=num
count=0
while(num>0):
    num//=10
    count+=1

num=temp
sum=0
while(num>0):
    a=num%10
    num//=10
    sum=sum+(a**count)
if(sum==temp):
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")