from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("First_Program")
root.configure(bg="Crimson")
#tao text
ttk.Label(root, text = "Hello World !").pack()
#tao nut an
Button(root, text = "Cong").pack()
#Select box
ttk.Combobox(root, values = ["Mua xuan","Mua ha","Mua thu","Mua dong"]).pack()
#check box
ttk.Checkbutton(root, text = "Chon").pack()
#O nhap du lieu
ttk.Entry(root).pack()
#Thanh keo
ttk.Scale(root, from_=0, to =100, orient=HORIZONTAL).pack()
#O nhap so
ttk.Spinbox(root, from_=0, to =100).pack()
#O nhap nhieu text
Text(root).pack()
#Ket thuc
root.mainloop()