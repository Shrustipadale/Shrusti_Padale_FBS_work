#n=int(input("Enter number of elements:"))
list1=[10,20,30,40,50]
i=0
j=len(list1)-1
while i<j:
    list1[i], list1[j] = list1[j], list1[i]
   # element=int(input("Enter element : "))
    #list1.append(element)
    i+=1
    j-=1
print("Reversed list: ",list1)