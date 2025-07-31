lst = []
n = int(input("Enter number of elements: "))
print("Enter the elements :")
for _ in range(n):
    num = int(input())
    lst += [num]   
result = []
for x in lst:
    if x % 2 != 0:
        result += [x] 
print("List after removing even numbers:", result)
