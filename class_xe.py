class car:
    #Liet ke cac thuoc tinh cua o to
    engine = "V8"
    color = "Black"
    max_speed = 100
    #Liet ke cac ham cua lop
    def run(self):
        print("Chuyen dong cua o to")
    def load(self):
        print("Co the cho hang")
    def show(self):
        print("Mau cua o to = ", self.color)
        print("Dong co cua o to = ", self.engine)
        print("Van toc toi da cua o to = ", self.max_speed)
#xe santafe
santafe = car()
santafe.color = "White"
santafe.max_speed = 250
santafe.show()
#xe Sonata
sonata = car()
sonata.color = "Blue"
sonata.max_speed = 200
sonata.engine = 'V6'
sonata.show()