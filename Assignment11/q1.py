numbers = []
even = []
odd = []
n = int(input("Enter number of elements: "))
for i in range(n):
    numbers.append(int(input()))
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even list:", even)
print("Odd list:", odd)
