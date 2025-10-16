#WAP for additoin of two time zone (HH:MM:SS) using operator overloading
class Time:
    def _init_(self, hh=0, mm=0, ss=0):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def _add_(self, other):
        total_seconds = self.ss + other.ss
        total_minutes = self.mm + other.mm + total_seconds // 60
        total_hours = self.hh + other.hh + total_minutes // 60

        return Time(total_hours % 24, total_minutes % 60, total_seconds % 60)

    def _str_(self):
        return f"{self.hh:02}:{self.mm:02}:{self.ss:02}"
    

t1 = Time(10, 45, 50)
t2 = Time(5, 30, 20)
t3 = t1 + t2
print(t3)
        