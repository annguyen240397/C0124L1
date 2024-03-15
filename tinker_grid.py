from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Ứng dụng hẹn hò")
root.configure(bg="chartreuse")
###
Label(root, text = "Trình bày lí do cà chớn").grid(row=0,column=1)
Label(root, text = "Lí do 1").grid(row=1, column=0)
Entry(root).grid(row=1, column=1)
Label(root, text = "Lí do 2").grid(row=2, column=0)
Entry(root).grid(row=2, column=1)
Label(root, text = "Thực ra không có lí do gì cả thích thì cà chớn thôi").grid(row=3,column=1)
root.mainloop()