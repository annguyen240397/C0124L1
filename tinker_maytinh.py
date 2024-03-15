from tkinter import *
from tkinter import ttk
root = Tk()
root.title("May tinh cam tay")
root.geometry("250x250")
root.configure(bg="chartreuse")
###
def onPress(number):
    Nhapso.insert("end",number)
def onEqual():
    Value = Nhapso.get()
    result = eval(Value)
    Nhapso.delete(0,"end")
    Nhapso.insert("end", result)
def onClear():
    Nhapso.delete(0,"end")
###
Nhapso = Entry(root)
Nhapso.grid(row=0,columnspan=4,pady=10,padx=50)
###
Button(root,width=4,height=2,text="1",command=lambda:onPress("1")).grid(row=1,column=0)
Button(root,width=4,height=2,text="2",command=lambda:onPress("2")).grid(row=1,column=1)
Button(root,width=4,height=2,text="3",command=lambda:onPress("3")).grid(row=1,column=2)
Button(root,width=4,height=2,text="+",command=lambda:onPress("+")).grid(row=1,column=3)

Button(root,width=4,height=2,text="4",command=lambda:onPress("4")).grid(row=2,column=0)
Button(root,width=4,height=2,text="5",command=lambda:onPress("5")).grid(row=2,column=1)
Button(root,width=4,height=2,text="6",command=lambda:onPress("6")).grid(row=2,column=2)
Button(root,width=4,height=2,text="-",command=lambda:onPress("-")).grid(row=2,column=3)

Button(root,width=4,height=2,text="7",command=lambda:onPress("7")).grid(row=3,column=0)
Button(root,width=4,height=2,text="8",command=lambda:onPress("8")).grid(row=3,column=1)
Button(root,width=4,height=2,text="9",command=lambda:onPress("9")).grid(row=3,column=2)
Button(root,width=4,height=2,text="*",command=lambda:onPress("*")).grid(row=3,column=3)

Button(root,width=4,height=2,text="0",command=lambda:onPress("0")).grid(row=4,column=0)
Button(root,width=4,height=2,text="Clear",command=onClear).grid(row=4,column=1)
Button(root,width=4,height=2,text="=",command=onEqual).grid(row=4,column=2)
Button(root,width=4,height=2,text="/",command=lambda:onPress("/")).grid(row=4,column=3)

Button(root,width=4,height=2,text=".",command=lambda:onPress(".")).grid(row=5,column=0)

###
root.mainloop()