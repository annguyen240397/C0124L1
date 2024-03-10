class hcn:
    cd = 0
    cr = 0
    def dien_tich(self):
        return self.cd * self.cr 
    def cv(self):
        return (self.cd + self.cr)*2
hcn1 = hcn()
hcn1.cd = 5
hcn1.cr = 3
print(hcn1.dien_tich())
print(hcn1.cv())