n=int(input("Enter number of emp: "))
total=0
for i in range(1,n+1):
    bs=int(input("Enter basic salary:"))

    if(bs<20000):
        da=bs*53.05/100
        hra=bs*15/100
        ta=0

    else:
        da==bs*15/100
        hra=bs*20/100
        ta=bs*18/100

    tm=bs+da*hra+ta
    print(f"Total salaryy of employee: ",tm)
    total+=tm
print(f"Total salaryy of all employee : ",total)
