def Factorial(n):
    if n==0 or n==1:
        return 1
    else:
         return n*Factorial(n-1)
start=int(input("Enter number: "))
stop=int(input("Enter number: "))
print(f"Factoral or given range:{start},{stop} ")
for i in range(start,stop+1):
 print(f"{i}!={Factorial(i)}")