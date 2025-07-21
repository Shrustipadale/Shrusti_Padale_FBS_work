def Prime(n):
 sum=0

 for num in range(2,n+1):
    
       for i in range(2, num):
         if(num%i==0):
            break
       else:
            sum+=num
    
 return sum

n=int(input("Enter number: "))
result=Prime(n)
print("Sum of all prime numbers from 1 to",n,"is:",result)
