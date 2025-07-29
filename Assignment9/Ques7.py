def sum_of_digit(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digit(n // 10)

num = int(input("Enter a non-negative integer: "))
print("Sum of digits of", num, "is", sum_of_digit(num))
