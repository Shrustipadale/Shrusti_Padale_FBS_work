list1 = []
count = int(input("Enter number of elements: "))
print("Enter the elements:")
for i in range(count):
    list1 += [int(input())]   
max = list1[0]
sec_max = 0
for i in range(1, len(list1)):
    if max < list1[i]:
        sec_max = max
        max = list1[i]
    elif sec_max < list1[i]:
        sec_max = list1[i]

print(sec_max)
