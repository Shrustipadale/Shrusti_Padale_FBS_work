#Write a program to create three lists of numbers, their squares and cubes
n = int(input("Enter number of elements: "))
numbers = []
print("Enter the elements :")
for i in range(n):
    num = int(input())
    numbers += [num] 
squares = []
cubes = []
for num in numbers:
    squares += [num ** 2]
    cubes   += [num ** 3]
print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:  ", cubes)
