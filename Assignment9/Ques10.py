def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + (n % 10))

# Read input and call recursion directly
num = int(input("Enter a non-negative integer: "))
print(f"Reverse of {num} is {reverse_number(num)}")
