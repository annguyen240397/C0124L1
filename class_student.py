class student:
    def __init__(self, id, name, birth, home_town, specialization, Class):
        self.id = int(id)
        self.name = str(name)
        self.birth = str(birth)
        self.home_town = str(home_town)
        self.specialization = str(specialization)
        self.Class = int(Class)
    def show(self):
        print('Ma sinh vien: ',self.id)    
        print('Ho va ten: ',self.name)
        print('Ngay thang nam sinh: ',self.birth)
        print('Que quan: ',self.home_town)
        print('Chuyen nganh: ',self.specialization)
        print('Lop: ',self.Class)
student1 = student(1, 'Nguyen Thien An', '24/03/1997', 'Da Nang', 'Su pham Toan', 8 )
student2 = student(2, 'Tran Nhat Quyen', '15/01/1997', 'Da Nang', 'Kiem Toan', 9)
class Student_list:
    def __init__(self):
        self.student_list = []
    def show(self):
        print(self.student_list)
s1 = Student_list()
print(student1)