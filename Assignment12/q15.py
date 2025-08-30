#10.Python Program to Take in Two Strings and Display the Larger Stringwithout Using 
# Built-in Functions

str1=input("Enter string: ")
str2=input("Enter string: ")
c1=0
c2=0
for i in str1:
    c1+=1
for i in str2:
    c2+=1
if c1>c2:
        print("Larger string is: ",str1)
elif c2>c1:
        print("Larger string is:",str2)
else:
        print("Both are equal")