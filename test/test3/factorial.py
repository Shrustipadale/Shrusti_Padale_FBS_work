n = int(input("Enter n: "))
sum_fact = 0

for i in range(1, n + 1):
    fact=1
    for j in range(1,i+1):
     fact *= j
    sum_fact=sum_fact+i* fact

print("Sum of series: ",sum_fact)
