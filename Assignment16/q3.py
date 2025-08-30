class Shirt:
    def __init__(self, sid=0, sname="Unknown", stype="Casual", price=0.0, size="Small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def showShirt(self):
        if self.size == "Small":
            final_price = self.price
        elif self.size == "Medium":
            final_price = self.price + (self.price * 0.10)
        elif self.size == "Large":
            final_price = self.price + (self.price * 0.20)
        elif self.size == "X-Large":
            final_price = self.price + (self.price * 0.30)
        else:
            final_price = self.price
        print(f"\nShirt ID: {self.sid}")
        print(f"Name: {self.sname}")
        print(f"Type: {self.stype}")
        print(f"Base Price: ₹{self.price}")
        print(f"Size: {self.size}")
        print(f"Final Price: ₹{final_price}")

    def __del__(self):
        print(f"Shirt '{self.sname}' deleted.")


shirt1 = Shirt()
shirt1.showShirt()

shirt2 = Shirt(301, "Allen Solly", "Formal", 1000, "Medium")
shirt2.showShirt()

shirt3 = Shirt(302, "Peter England", "Casual", 1000, "Large")
shirt3.showShirt()

shirt4 = Shirt(303, "Van Heusen", "Party Wear", 1000, "X-Large")
shirt4.showShirt()
