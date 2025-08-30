list1 = []
n = int(input("Enter number of sublists: "))
print("Enter the elements of each sublist (2 elements each):")
for i in range(n):
    a = int(input(f"Enter first element of sublist {i+1}: "))
    b = int(input(f"Enter second element of sublist {i+1}: "))
    list1.append([a, b])
for i in range(n):
    for j in range(0, n - i - 1):
        if list1[j][1] > list1[j + 1][1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
print("List sorted by second element in sublist:")
for sublist in list1:
    print(sublist)
