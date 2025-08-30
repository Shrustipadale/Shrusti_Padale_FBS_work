list1 = []
count = int(input("Enter number of elements: "))
print("Enter the elements:")
for i in range(count):
    list1.append(int(input()))
for i in range(len(list1)):
    for j in range(0, len(list1)-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
print("Second Largest Number is:", list1[-2])
