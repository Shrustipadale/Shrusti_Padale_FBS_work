# Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0

    def __init__(self, bid=0, bname="Unknown", price=0.0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
        print("Constructor called: Book object created.")

    def ShowBook(self):
        print("\n--- Book Details ---")
        print(f"Book ID     : {self.bid}")
        print(f"Book Name   : {self.bname}")
        print(f"Price       : ₹{self.price}")
        print(f"Author      : {self.author}")

    @staticmethod
    def ShowCount():
        print(f"\nTotal Books Created: {Book.count}")

    def __del__(self):
        print(f"Destructor called: Book '{self.bname}' object deleted.")


book1 = Book()
book1.ShowBook()

book2 = Book(101, "Python Programming", 450.50, "Guido van Rossum")
book2.ShowBook()

book3 = Book(102, "Data Science Basics", 599.99, "Joel Grus")
book3.ShowBook()

Book.ShowCount()

del book2
del book3
