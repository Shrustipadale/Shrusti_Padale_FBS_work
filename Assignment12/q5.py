str1=input("Enter string: ")
c=0
for s in str1:
    if s in "aeiou" or s in "AEIOU":
        c+=1
print("Vowels: ",c)
