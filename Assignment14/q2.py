#Write a Python program to remove the intersection of a second set with a first set
set1 = {1, 2, 3, 5, 8}
set2 = {3, 8, 20, 70}

for elem in set1 & set2:
    set1.remove(elem)
print("set1:", set1) 
print("set2:", set2)  
