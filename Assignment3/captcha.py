#Write a program to prompt user to enter userid and password. After verifyinguserid and password  display 
# a 4 digit random number and ask user to enter thesame. If user enters the same number then show him
#  success message otherwisefailed. (Something like captcha)

import random
user=input("Enter user id: ")
passw=input("Enter password: ")
user_id="admin"
password="shru@123"
if(user==user_id and passw==password):
    captcha=random.randint(1000,9999)
    print("Captcha: ",captcha)
    input=int(input("Enter captcha: "))
    
    if(input==captcha):
         print("Login is successful")
     
    elif(input!=captcha):
         print("the captcha is wrong")
        
else:
     print("The credentials are wrong unsuccessful login")

