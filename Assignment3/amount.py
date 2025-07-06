# Accept age of five people and also per person ticket amount and then calculate totalamount to ticket #
# to travel for all of them based on following condition :a. Children below 12 = 30% discount #
# b. Senior citizen (above 59) = 50% discountc. Others need to pay full.

a1=int(input("Enter age of 1st person: "))
a2=int(input("Enter age of 2nd person: "))
a3=int(input("Enter age of 3rd person: "))
a4=int(input("Enter age of 4th person: "))
a5=int(input("Enter age of 5th person: "))
amt=int(input("Enter the amount: "))
tm=0

if(a1<12):
    tm+=amt-(amt*0.3)
elif(a1>59):
    tm+=amt-(amt*0.5)
else:
    tm+=amt

if(a2<12):
    tm+=amt-(amt*0.3)
elif(a2>59):
    tm+=amt-(amt*0.5)
else:
    tm+=amt

if(a3<12):
    tm+=amt-(amt*0.3)
elif(a3>59):
    tm+=amt-(amt*0.5)
else:
    tm+=amt

if(a4<12):
    tm+=amt-(amt*0.3)
elif(a4>59):
    tm+=amt-(amt*0.5)
else:
    tm+=amt

if(a5<12):
    tm+=amt-(amt*0.3)
elif(a5>59):
    tm+=amt-(amt*0.5)
else:
    tm+=amt
    
print("Total cost price for 5 people: ",tm)