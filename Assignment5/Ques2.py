students=int(input("Enter number of students:  "))
i=1
total=0
while(i<=students):
    print("Students",i)
    j=1
    tm=0
    while(j<=5):
        marks=float(input("Enter the marks of subject:{j} "))
        tm+=marks
        j+=1
    percent=tm/5
    print("Enter percentage of students:",percent)
    total+=percent
    i+=1
avg=total/students
print("Average percentage of all students: ",avg)

