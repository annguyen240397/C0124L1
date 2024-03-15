from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("400x500")
root.title("Address Book")
root.configure(bg="chartreuse")
###

datas = []
Name = StringVar()
Number = StringVar()

###
def update_book():
    select.delete(0,END)
    for n,p,a in datas:
        select.insert(END, n)

def add():
    global datas
    datas.append([Name.get(), Number.get(), address.get(1.0, "end-1c")])
    update_book()

def view():
    Name.set(datas[int(select.curselection()[0])][0])
    Number.set(datas[int(select.curselection()[0])][0])
    address.delete(1.0,"end")
    address.insert(1.0, datas[int(select.curselection()[0])][2])

def delete():
    del datas[int(select.curselection()[0])]
    update_book()

def reset():
    Name.set('')
    Number.set('')
    address.delete(1.0,"end")
###

Frame1 = Frame(root)
Frame1.pack(pady=10) 

Frame2 = Frame(root)
Frame2.pack(pady=10) 

Frame3 = Frame(root)
Frame3.pack(pady=10) 

###
Label(Frame1, text = "Name").pack(side=LEFT)
Entry(Frame1, textvariable= Name, width=50).pack()

Label(Frame2, text = "Phone NO.").pack(side=LEFT)
Entry(Frame2, textvariable= Number,width=50).pack()

Label(Frame3, text = "Address").pack(side=LEFT)
address = Text(Frame3,width=50,height=10)
address.pack()

Button(root, text = "Add", command=add).place(x=100, y= 270)
Button(root, text = "View", command=view).place(x=100, y= 310)
Button(root, text = "Delete", command=delete).place(x=100, y= 350)
Button(root, text = "Reset", command=reset).place(x=100, y= 390)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=260)

###
root.mainloop()