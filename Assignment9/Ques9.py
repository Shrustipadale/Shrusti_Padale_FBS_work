def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)

# Read input and compute
m = int(input("Enter base (m): "))
n = int(input("Enter exponent (n, non-negative integer): "))
print(f"{m} to the power {n} is {power(m, n)}")
