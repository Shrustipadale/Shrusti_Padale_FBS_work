#Write a program to solve the following series :a. 1! + 2! + 3! + 4! + .....n!
n = int(input("Enter n: "))
sum_fact = 0
fact = 1

for i in range(1, n + 1):
    fact *= i  
    sum_fact += fact

print(sum_fact)
