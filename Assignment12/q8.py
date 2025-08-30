#Python Program to Remove the Characters of Odd Index Values in a String

str1=input("enter string: ")
result=""
for i in range(len(str1)):
    if(i%2==0):
        result+=str1[i]
print("new string: ",result)