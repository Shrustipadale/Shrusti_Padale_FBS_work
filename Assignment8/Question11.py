def Count(num):
    c=0
    while(num!=0):
        num//=10
        c=c+1
    return c

def Armstrong(num):
    dc=Count(num)
    sum=0
    while(num!=0):
        a=num%10
        num//=10
        sum+=(a**dc)
    return sum

num=int(input("Enter number: "))
ans=Armstrong(num)
if(ans==num):
    print("Yes,it is armstrong")
else:
    print("No, it is not armstrong")