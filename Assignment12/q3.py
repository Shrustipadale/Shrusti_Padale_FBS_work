str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
s1 = str1.replace(" ", "")
s2 = str2.replace(" ", "")
if len(s1) != len(s2):
    print("No, they are not anagrams")
else:
    list1 = list(s1)
    list2 = list(s2)

    for ch in s1:
        if ch in list2:
            list2.remove(ch)
    if not list2:
        print("Yes, they are anagrams")
    else:
        print("No, they are not anagrams")
