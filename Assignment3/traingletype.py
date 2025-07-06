#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
side1=int(input("Enter the first side of triangle: "))
side2=int(input("Enter the second side of triangle: "))
side3=int(input("Enter the third side of triangle: "))

if(side1==side2==side3):
    print("It is an euqilateral triangle")

elif(side1==side2 or side1==side3 or side2==side3):
    print("It is an isosceles triangle")

else:
    print("It is a scalene triangle")