days=int(input("Enter the no. of days: "))
years=days//365
days=days%365
weeks=days//7
days=days%7
print("Years:",years,"Weeks:",weeks,"Days:",days)