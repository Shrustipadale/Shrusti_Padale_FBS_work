def Palindrome():
 num=int(input("Enter number: "))
 copy = num
 rev=0
 while(num>0):
  a=num%10
  rev=rev*10+a
  num//=10
 if(rev==copy):
    return "It is a palindrome."
 else:
    return"It is not a palindrome."

print(Palindrome())

