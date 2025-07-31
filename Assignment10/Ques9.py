numbers = [12, 5, 3, 8, 7, 4, 10]
n = len(numbers)

even_list = [0] * n
odd_list  = [0] * n
e = 0
o = 0

for i in range(n):
    if numbers[i] % 2 == 0:
        even_list[e] = numbers[i]
        e += 1
    else:
        odd_list[o] = numbers[i]
        o += 1

# To view only the filled portions:
even = [even_list[i] for i in range(e)]
odd = [odd_list[i]  for i in range(o)]

print("Even:", even)  # Even: [12, 8, 4, 10]
print("Odd:", odd)    # Odd: [5, 3, 7]
