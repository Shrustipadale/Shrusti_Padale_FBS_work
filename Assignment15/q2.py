# Create a class Product with members as pid,pname,price and quantity .Add following methods:\
# d. Constructor (Support both parameterized and parameterless)e. Destructorf. ShowBook

class Product:
    def __init__(self,pid=0,pname="",p=0,q=0):
        self.pid=pid
        self.pname=pname
        self.p=p
        self.q=q
        print("Constructor called :Product object created")

    def showProduct(self):
        print("\n--- Product Details ---")
        print(f"Product ID   : {self.pid}")
        print(f"Product Name : {self.pname}")
        print(f"Price        : ₹{self.p}")
        print(f"Quantity     : {self.q}")


    def __del__(self):
        print(f"Destructor called: Book '{self.pname}' object deleted.")
product1 = Product()
product1.showProduct()

product2 = (101, "Python Programming", 450.50, 5)
product2.showProduct()

del product2