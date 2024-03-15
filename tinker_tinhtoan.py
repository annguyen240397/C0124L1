from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Chương trình máy tính")
root.configure(bg="chartreuse")
#======= BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH
def addNumbers():
    num1 = int(so_thu_nhat.get())
    num2 = int(so_thu_hai.get())
    result = num1 + num2 
    Ket_qua.config(text = "Kết quả: " + str(result))
def subNumbers():
    num1 = int(so_thu_nhat.get())
    num2 = int(so_thu_hai.get())
    result = num1 - num2 
    Ket_qua.config(text = "Kết quả: " + str(result))
def mulNumbers():
    num1 = int(so_thu_nhat.get())
    num2 = int(so_thu_hai.get())
    result = num1 * num2 
    Ket_qua.config(text = "Kết quả: " + str(result))
def divNumbers():
    num1 = int(so_thu_nhat.get())
    num2 = int(so_thu_hai.get())
    result = num1 / num2 
    Ket_qua.config(text = "Kết quả: " + str(result))
Label(root, text = "Số thứ nhất").grid(row = 0, column = 0)
so_thu_nhat = Entry(root)
so_thu_nhat.grid(row = 0, column = 1)

Label(root, text = "Số thứ hai").grid(row = 1, column = 0)
so_thu_hai = Entry(root)
so_thu_hai.grid(row = 1, column = 1)

Button(root, text = "Cộng", command=addNumbers).grid(row = 2, column = 0)
Button(root, text = "Trừ", command=subNumbers).grid(row = 2, column = 1)
Button(root, text = "Nhân", command=mulNumbers).grid(row = 2, column = 2)
Button(root, text = "Chia", command=divNumbers).grid(row = 2, column = 3)
Ket_qua = Label(root, text = "Kết quả")
Ket_qua.grid(row = 3, column = 1)
#======= BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH

root.mainloop()