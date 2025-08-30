# Create a class Distance with data members as km,m and cm and add following
#methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator
class Distance:
    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        self._normalize()

    def __del__(self):
        # Optional: shows when an instance is destroyed
        print(f"Destroying Distance({self.km} km, {self.m} m, {self.cm} cm)")

    def _normalize(self):
        # Convert cm to m
        if self.cm >= 100:
            extra_m = self.cm // 100
            self.cm %= 100
            self.m += extra_m
        # Convert m to km
        if self.m >= 1000:
            extra_km = self.m // 1000
            self.m %= 1000
            self.km += extra_km

        # Handle negative cm by borrowing from meters
        if self.cm < 0:
            borrow = (abs(self.cm) + 99) // 100
            self.m -= borrow
            self.cm += borrow * 100
        # Handle negative meters by borrowing from kilometers
        if self.m < 0:
            borrow = (abs(self.m) + 999) // 1000
            self.km -= borrow
            self.m += borrow * 1000

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return Distance(self.km + other.km,
                        self.m + other.m,
                        self.cm + other.cm)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return Distance(self.km - other.km,
                        self.m - other.m,
                        self.cm - other.cm)

    def __str__(self):
        return f"{self.km} km, {self.m} m, {self.cm} cm"

    def __repr__(self):
        return f"Distance(km={self.km}, m={self.m}, cm={self.cm})"


