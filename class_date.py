class Date:
    def __init__(self,day,month,year):
        self.day=int(day)
        self.month=int(month)
        self.year=int(year)
    def get_day(self):
        return self.day
    def get_month(self):
        return self.month
    def get_year(self):
        return self.year
    def set_day(self,day):
        self.day = day
    def set_month(self,month):
        self.month = month
    def set_year(self,year):
        self.year = year
    def set_date(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    def tostring(self):
        return f"{self.day}/{self.month}/{self.year}"
date1 = Date(30,4,2024)
print(date1.tostring())
date1.set_day(24)
date1.set_month(3)
date1.set_year(1997)
print(date1.tostring())