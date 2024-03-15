from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x250")
root.title("Bo cuc voi pack")
root.configure(bg="chartreuse")
###
Button(root, text = "Red", fg = "red").pack(side = LEFT)
Button(root, text = "Black", fg = "black").pack(side = RIGHT)
Button(root, text = "Blue", fg = "blue").pack(side = TOP)
Button(root, text = "Green", fg = "green").pack(side = BOTTOM)
root.mainloop()