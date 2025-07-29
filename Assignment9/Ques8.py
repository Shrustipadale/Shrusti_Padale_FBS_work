def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

n = int(input("Enter a positive integer: "))
if is_prime(n):
    print(f"{n} is a Prime number")
else:
    print(f"{n} is not a Prime number")
