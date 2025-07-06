 #Write a program to check if given 3 digit number is a palindrome or not.

n = int(input("Enter a 3-digit number: "))
original = n


hun = n//100
ten = (n//10)%10
un = n%10
rev=un*100+ten*10+hun

if(rev == original):
    print(original," is a palindrome.")
else:
    print(original," is not a palindrome.")

