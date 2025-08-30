#Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to
#  the first and vice versa. Use the Python set.
def Missing(set1,set2):
    return set1-set2 ,set2-set1

set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 4, 5, 6, 7, 8}
missing_set2,missing_set1=Missing(set1,set2)
print("Missing in second set compared to first:", missing_set2)
print("Missing in first set compared to second:", missing_set1)