interior_area=float(input("Enter the area of interior walls: "))
interior_cost=float(input("Enter the cost:"))
exterior_area=float(input("Enter the area of exterior walls: "))
exterior_cost=float(input("Enter the cost:"))
int_cost=interior_cost*interior_area
ext_cost=exterior_cost*exterior_area
painting_cost=int_cost+ext_cost
print("Cost of painting:",painting_cost)