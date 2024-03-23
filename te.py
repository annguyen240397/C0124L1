from tkinter import *
from PIL import ImageTk, Image
img=[0,0,0]
game=Tk()
game.title('Internet Disconnect')
canvas = Canvas(master=game,width=600,height=300,background="White")
canvas.pack()
img[0]=ImageTk.PhotoImage(Image.open("photos/dragon.jpg"))
img[1]=ImageTk.PhotoImage(Image.open("photos/cloud.jpg"))
img[2]=ImageTk.PhotoImage(Image.open("photos/tree.jpg"))

dragon=canvas.create_image(0,250,anchor=NW,image=img[0])
cloud=canvas.create_image(550,50,anchor=NW,image=img[1])
tree=canvas.create_image(550,250,anchor=NW,image=img[2])
canvas.update()
game.mainloop()