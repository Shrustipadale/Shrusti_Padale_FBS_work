n = int(input("Enter num of ele:"))                     
a = []
for i in range(n):
    a.append(input())

for i in range(n):
    for j in range(n - i - 1):
        if len(a[j]) > len(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]  

print(a)
