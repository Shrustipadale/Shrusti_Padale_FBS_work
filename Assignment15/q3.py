class Shirt:
    def __init__(self, sid=0, sname="Unknown", stype="Casual", price=0.0, size="Medium"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size
        print("Constructor called: Shirt object created.")

    def showShirt(self):
        print("\n--- Shirt Details ---")
        print(f"Shirt ID     : {self.sid}")
        print(f"Shirt Name   : {self.sname}")
        print(f"Shirt Type   : {self.stype}")
        print(f"Price        : ₹{self.price}")
        print(f"Size         : {self.size}")

    def __del__(self):
        print(f"Destructor called: Shirt '{self.sname}' object deleted.")


shirt1 = Shirt()
shirt1.showShirt()

shirt2 = Shirt(201, "Allen Solly", "Formal", 1599.99, "Large")
shirt2.showShirt()

del shirt2
