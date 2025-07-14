user="admin"
password="admin123"

attempt=0
max_attempt=3

while(max_attempt>attempt):
    username=input("Enter username: ")
    passw=input("Enter password: ")
    if(username==user and passw==password):
        print("Login successful")
        break
    else:
        attempt+=1
        print("Invalid creadentials, few attempts left")

if(attempt==max_attempt):
    print("To many fail attempts, Program terminated")