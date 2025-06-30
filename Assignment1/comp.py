p=int (input("Enter principle amount:"))
t=int (input("Enter time:"))
r=float (input("Enter rate of interest:"))
amount=p*(1+r/100)**t
comp=amount-p
print("Compund interest:",comp)