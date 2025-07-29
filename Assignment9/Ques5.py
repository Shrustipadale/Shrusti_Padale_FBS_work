def factorial(n):
    # Base case: 0! and 1! are both 1
    return 1 if n <= 1 else n * factorial(n - 1)

# Read input and compute directly
num = int(input("Enter number: "))
print(f"{num}! =", factorial(num))
