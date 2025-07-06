#Write a program to input electricity unit charges and calculate total electricity billaccording to the #
# given condition:For first 50 units Rs. 0.50/unitFor next 100 units Rs. 0.75/unitFor next 100 units #
# Rs. 1.20/unitFor unit above 250 Rs. 1.50/unitAn additional surcharge of 20% is added to the bill

unit=int(input("Enter the unit: "))

if(unit<=50):
    bill=50*0.50

elif(unit>50 and unit<=150):
    bill=50*0.50
    unit=(unit-50)
    bill+=100*0.75

elif(unit>150 and unit<=250):
    bill=50*0.50
    unit=(unit-50)
    bill+=100*0.75
    init=(unit-100)
    bill+=100*1.20
else:
    bill=50*0.50
    unit=(unit-50)
    bill+=100**0.75
    unit=(unit-100)
    bill+=100*1.20
    unit=(unit-100)
    bill+=100*1.50

bill+=(bill*0.20)
print(bill)
