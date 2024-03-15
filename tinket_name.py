from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Chương trình máy tính")
root.configure(bg="chartreuse")
#======= BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH
def hovaten():
    ho1 = ho.get()
    ten1 = ten.get()
    result = ho1 + " " + ten1 
    Ket_qua.config(text = "Chào " + result)

Label(root, text = "Họ").grid(row = 0, column = 0)
ho = Entry(root)
ho.grid(row = 0, column = 1)

Label(root, text = "Tên đệm + Tên").grid(row = 1, column = 0)
ten = Entry(root)
ten.grid(row = 1, column = 1)

Button(root, text = "Xử lí", command=hovaten).grid(row = 2, column = 0)
Ket_qua = Label(root, text = "Kết quả")
Ket_qua.grid(row = 3, column = 1)
#======= BẮT ĐẦU PHẦN THÂN CHƯƠNG TRÌNH

root.mainloop()