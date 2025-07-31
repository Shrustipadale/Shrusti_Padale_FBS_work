#Write a program to find sum of all elements of list
list1=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    list1.append(int(input("Enter element: ")))
    sum=0
    for x in list1:
        sum+=x
print(sum)
