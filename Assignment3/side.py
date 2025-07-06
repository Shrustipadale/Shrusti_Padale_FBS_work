 #Write a program to input all sides of a triangle and check whether triangle is valid or not.

side1=int(input("Enter side1: "))
side2=int(input("Enter side2: "))
side3=int(input("Enter side3: "))

if(side1+side2>side3 and side1+side3>side2 and side2+side3>side1):
    print("The triangle is valid")

else:
    print("The triangle is not valid")