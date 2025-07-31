n = int(input("Enter number of elements: "))
list1 = []

for _ in range(n):
    list1.append(int(input("Enter element: ")))

element = int(input("Enter element to search: "))
count = 0

for x in list1:
    if x == element:
        count += 1

if count > 0:
    print("Yes, present")
    print("Count:", count)
else:
    print("No, not present")
