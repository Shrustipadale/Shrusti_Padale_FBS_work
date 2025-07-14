#Write a program to print first n prime numbers.
n = int(input("Enter how many primes to print: "))
count = 0

for num in range(2, 10**9):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
        count += 1
        if count == n:
            break

print()