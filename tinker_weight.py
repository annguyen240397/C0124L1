from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Weight Conversion")
root.configure(bg="chartreuse")
####
def Gram():
    gam = float(kg.get()) * 1000
    pound = float(kg.get()) * 2.20462
    ounce = float(kg.get()) * 0.028349
    t1.delete("1.0",END)
    t1.insert(END, gam)
    t2.delete("1.0",END)
    t2.insert(END, pound)
    t3.delete("1.0",END)
    t3.insert(END, ounce)

###
Label(root, text = "Nhập cân nặng của Nhật Quyên").grid(row=0,column=0)
kg=Entry(root)
kg.grid(row=0, column=1)
Button(root, text="Quy đổi", command=Gram).grid(row=0,column=2)
Label(root, text = "Gam").grid(row=1,column=0)
Label(root, text = "Pound").grid(row=1,column=1)
Label(root, text = "Ounce").grid(row=1,column=2)
t1 = Text(root, width=20,height=1)
t1.grid(row=2,column=0)
t2 = Text(root, width=20,height=1)
t2.grid(row=2,column=1)
t3 = Text(root, width=20,height=1)
t3.grid(row=2,column=2)
###
root.mainloop()