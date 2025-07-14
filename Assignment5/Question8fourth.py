
#S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a = float(input("Enter a: "))
s = 0.0
for i in range(1, 11):
    term= a**i / i
    s+=term
    print(term)
print("Sum :",s)
