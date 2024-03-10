class car:
    name = ""
    model = ""
    weight = 0
    color = ""
    def __init__(self,name1,model1,weight1,color1):
        self.name = name1
        self.weight = weight1
        self.model = model1
        self.color = color1
    def start(self):
        print("Runnnnnn")
    def dive(self):
        pass
    def stop(self):
        pass
    def brake(self):
        pass
    def toString(self):
        pass
    def show(self):
        print("Ten cua xe la: ", self.name)
        print("Can nang cua xe la: ", self.weight)
        print("Model cua xe la: ", self.model)
        print("Mau cua xe la: ", self.color)
vinfast = car("Vinfast","Electric", 100, "Blue")
vinfast.show()