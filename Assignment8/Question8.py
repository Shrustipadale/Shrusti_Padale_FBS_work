def Reverse(num):
    rev=0
    while(num>0):
        a=num%10
        num=num//10
        rev=(rev*10)+a
    return rev

num=int(input("Enter number: "))
print(Reverse(num))