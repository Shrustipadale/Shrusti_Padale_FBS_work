def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def reverse_number(n):
    if n == 0:
        return 0
    power = count_digits(n) - 1
    return (n % 10) * (10 ** power) + reverse_number(n // 10)


num = int(input("Enter number: "))
reversed_num = reverse_number(num)
print(f"Reverse of {num} is {reversed_num}")

