def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def sum_of_powers(n, power):
    if n == 0:
        return 0
    return (n % 10) ** power + sum_of_powers(n // 10, power)

def is_armstrong(n):
    # Handle zero separately, since count_digits(0) returns 0
    power = count_digits(n) or 1
    total = sum_of_powers(n, power)
    return total == n


num = int(input("Enter number: "))
if is_armstrong(num):
 print(f"{num} is an Armstrong number")
else:
        print(f"{num} is not an Armstrong number")

