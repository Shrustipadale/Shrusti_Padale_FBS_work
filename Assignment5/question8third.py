#Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter n: "))
total = 0
power = 1  # will hold the current term, starting at 2^0 = 1

for _ in range(0, n + 1):  # loop from 0 to n inclusive
    total += power         # add current power (1, 2, 4, 8, ...)
    power *= 2             # compute next power by multiplying by 2

print("Sum is:", total)

