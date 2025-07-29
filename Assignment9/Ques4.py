def sum_n(n):
    if n <= 0:
        return 0
    else:
     return n + sum_n(n - 1)

def main():
 n = int(input("Enter a positive integer n: "))
 if n < 1:
    print("Please enter n >= 1.")
    return 


 total = sum_n(n)
 print(f"Sum of first {n} natural numbers is: {total}")

