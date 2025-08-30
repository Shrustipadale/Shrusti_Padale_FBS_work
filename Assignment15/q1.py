class Book:
    def __init__(self,bid=0,nm="",p=0,a=""):
        self.bid=bid
        self.nm=nm
        self.p=p
        self.a=a
        print("Constructor called :Book object created")

    def showBook(self):
        print("\nBook Details: ")
        print(f"{self.bid}")
        print(f"{self.nm}")
        print(f"{self.p}")
        print(f"{self.a}")

    def __del__(self):
        print(f"Destructor called: Book '{self.nm}' object deleted.")
book1 = Book()
book1.showBook()

book2 = Book(101, "Python Programming", 450.50, "Guido van Rossum")
book2.showBook()

del book2
