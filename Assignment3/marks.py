#Input 5 subject marks from user and display grade(eg.First class,Second class ..)

s1=float(input("Enter marks of subject 1: "))
s2=float(input("Enter marks of subject 2: "))
s3=float(input("Enter marks of subject 3: "))
s4=float(input("Enter marks of subject 4: "))
s5=float(input("Enter marks of subject 5: "))
tm=(s1+s2+s3+s4+s5)/5

if(tm>=75):
    print("First Class with distinction ")

elif(tm>=60 and tm<70):
    print("First class")

elif(tm>=50 and tm<60):
    print("Second class")

elif(tm>=40 and tm<50):
    print("Pass")

else:
    print("Fail")



