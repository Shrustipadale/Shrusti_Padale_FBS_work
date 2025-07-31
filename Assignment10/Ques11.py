list=[]
c=int(input("Enter number of elemts: "))
for i in range(c):
    list+=[int(input("Enter elements: "))]
m=int(input("Enter first divisor: "))
n=int(input("Enter second divisor: "))
print(f"Numbers divisible by{m}and{n}: ")
for num in list:
    if num % m == 0 and num % n == 0:
        print(num)