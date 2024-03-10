class CustomDate:
    def __init__(self, d, m ,y):
        self.d = d
        self.m = m
        self.y = y
    
    def set_day(self, d):
        self.d = d
    
    def __str__(self):
        return f"{self.d}/{self.m}/{self.y}"
        
    
custom_date = CustomDate(30, 4, 2024)
print(custom_date)
custom_date.set_day(20)
print(custom_date)