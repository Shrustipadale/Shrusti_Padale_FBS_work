D=[2000,500,200,100,50,20,10,5]
amount=int(input("Enter the amount: "))
c={}
for note in D:
    if(amount>=note):
        count=amount//note
        amount=amount%note
        c[note]=count
print("Minimum number of notes needed: ")
tn=0
for note,count in c.items():
        print(f'{note}: {count}')
        tn+=count
print("total notes: ",tn)