def Factors(num):
    print("Factors of num is:",num)
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
num=int(input("Enter number: "))
Factors(num)

