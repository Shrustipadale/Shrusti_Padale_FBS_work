num=int(input("Enter original number of coins: "))
coins=list(map(int,input("Enter number of coins:").split()))
for num in coins:
    if coins.count(num)%2!=0:
        print("Missing coin number is: ",num)
        break
