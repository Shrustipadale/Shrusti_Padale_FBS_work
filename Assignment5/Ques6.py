start=1
stop=100
for x in range(start,stop+1):
    for i in range(2,x):
        if(x%i==0):
            break
    else:
        print(x)
        