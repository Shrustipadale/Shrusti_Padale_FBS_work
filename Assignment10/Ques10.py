#Write a program to remove all occurrences of a given element in the list.# Read list elements from the user
lst = []
n = int(input("How many elements in the list? "))
for i in range(n):
    lst += [int(input("Enter element: "))]
ele = int(input("Enter element to remove: "))
result = []
for x in lst:
    if x != ele:
        result += [x]   
print(result)
