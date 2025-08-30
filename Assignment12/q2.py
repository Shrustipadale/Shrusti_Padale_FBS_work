str1 = input("Enter a string: ")
str2 = str1
index = int(input("Enter the index: "))

if 0 <= index < len(str2):
    ch = str2[index]
    modified = str2.replace(ch, "", 1)
    print("Modified string (first match removed):", modified)
else:
    print("Invalid index.")
