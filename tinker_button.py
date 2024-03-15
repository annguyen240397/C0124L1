from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Kiem tra nut")
root.geometry("100x100")
root.configure(bg="chartreuse")
####
def apple():
    print("Day la apple")

def banana():
    print("Day la banana")

Button(root, text = "Apple", command=apple).pack()
Button(root, text = "Banana", command=banana).pack()
####
root.mainloop()