from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Bo cuc voi Place")
root.configure(bg="chartreuse")
###
Label(root, text = "Name").place(x=30, y=50)
Label(root, text = "Email").place(x=30, y=90)
Label(root, text = "Password").place(x=30, y=130)
Entry(root).place(x=80, y=50)
Entry(root).place(x=80, y=90)
Entry(root).place(x=95, y=130)
root.mainloop()