class Product:
    discount = 0

    def __init__(self, pid=0, pname="Unknown", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Constructor called: Product object created.")

    def showProduct(self):
        print("\n--- Product Details ---")
        print(f"Product ID   : {self.pid}")
        print(f"Product Name : {self.pname}")
        print(f"Price        : ₹{self.price}")
        print(f"Quantity     : {self.quantity}")

    @staticmethod
    def setDiscount(discount):
        Product.discount = discount
        print(f"\nDiscount set to {Product.discount}%")

    def applyDiscount(self):
        discounted_price = self.price - (self.price * Product.discount / 100)
        print(f"Price after {Product.discount}% discount: ₹{discounted_price}")

    def __del__(self):
        print(f"Destructor called: Product '{self.pname}' object deleted.")


product1 = Product()
product1.showProduct()

product2 = Product(201, "Laptop", 55000, 2)
product2.showProduct()

Product.setDiscount(10)
product2.applyDiscount()

product3 = Product(202, "Mobile", 25000, 5)
product3.showProduct()
product3.applyDiscount()

del product2
del product3

