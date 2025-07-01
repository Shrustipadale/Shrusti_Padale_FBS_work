len=int(input("Enter length:"))
bre=int(input("Enter breadth:"))
rad=int(input("Enter radius:"))
area_rectangle=len*bre
area_circle=0.5*3.14*rad*rad
total_area=area_rectangle+area_circle
peri=2+len+bre+(3.14*rad)
print("Total area:",total_area)
print("Perimeter:",peri)