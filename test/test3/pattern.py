for i in range(1,5+1):
    for j in range(1,5+1):
        if(i%2==0):
         print((j+1)%2,end="")
        else:
         print((j%2),end="")
    print()