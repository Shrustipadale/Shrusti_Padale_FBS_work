#Write a program to calculate profit or loss.
cp=int(input("Enter the cost price: "))
sp=int(input("Enter the selling price: "))

if(sp>cp):
    profit=sp-cp
    print("Profit: ",profit)

else:
    loss=cp-sp
    print("Loss: ",loss)