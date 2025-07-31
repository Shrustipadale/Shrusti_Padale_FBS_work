n=int(input("Enter number of elements: "))
list1=[]
for i in range(n):
    element=int(input("Enter element : "))
    list1.append(element)
max=list1[0]
min=list1[0]
for i in range(1,n):
        if list1[i]>max:
            max=list1[i]
        if list1[i]<min:
            min=list1[i]
print("Maximum element is : ",max)
print("Minimum element is : ",min)