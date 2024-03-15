from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Temperature Converter")
root.configure(bg="chartreuse")
###
def csangf():
    c1 = int(c.get())
    result = (c1*1.8)+32
    Ket_qua1.config(text = str(result) + " \N{DEGREE FAHRENHEIT}")

def fsangc():
    f1 = int(f.get())
    result = (f1 - 32 )/1.8
    Ket_qua2.config(text = str(result) + " \N{DEGREE CELSIUS}")

c = Entry(root)
c.grid(row = 0, column=0)
Label(root,text = "\N{DEGREE CELSIUS}").grid(row=0, column=1)
Button(root, text = "\N{RIGHTWARDS BLACK ARROW}",command=csangf).grid(row=0,column=2)
Ket_qua1 = Label(root, text = "Kết quả")
Ket_qua1.grid(row=0,column=3)
f = Entry(root)
f.grid(row=1,column=0)
Label(root,text = "\N{DEGREE FAHRENHEIT}").grid(row=1, column=1)
Button(root, text = "\N{RIGHTWARDS BLACK ARROW}",command=fsangc).grid(row=1,column=2)
Ket_qua2 = Label(root, text = "Kết quả")
Ket_qua2.grid(row=1,column=3)
root.mainloop()