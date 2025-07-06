#Write a program to input angles of a triangle and check whether triangle is valid or not.

ang1=float(input("Enter angle1: "))
ang2=float(input("Enter angle2: "))
ang3=float(input("Enter angle3: "))

if(ang1+ang2+ang3==180):
    print("The triangle is valid")
else:
    print("The triangle is not valid")