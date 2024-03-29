import sys
import random
from PIL import *
from tkinter import Tk, Frame, Canvas, ALL, NW
 
WIDTH      = 300
HEIGHT     = 300
DELAY      = 100
DOT_SIZE   = 10
ALL_DOTS   = 900 #WIDTH * HEIGHT / (DOT_SIZE * DOT_SIZE)
RAND_POS   = 27
 
x = [0] * ALL_DOTS
y = [0] * ALL_DOTS
 
class Board(Canvas):
   def __init__(self, parent):
       Canvas.__init__(self, width=WIDTH, height=HEIGHT, 
                       background="black", highlightthickness=0)
       self.parent = parent
       self.initGame()
       self.pack()
  
   def initGame(self):
       self.right = True
       self.left = False
       self.up = False
       self.down = False
  
       self.inGame = True
       self.dots = 3
  
       self.apple_x = 100
       self.apple_y = 190
  
       for i in range(self.dots):
           x[i] = 50 - i * 10
           y[i] = 50
  
       try: 
           self.dotImage = Image.open("dot.png")
           self.dotImage.thumbnail((10, 10), Image.ANTIALIAS)
           self.dot = ImageTk.PhotoImage(self.dotImage)
  
           self.headImage = Image.open("head.png")
           self.headImage.thumbnail((10, 10), Image.ANTIALIAS) 
           self.head = ImageTk.PhotoImage(self.headImage)
  
           self.appleImage = Image.open("apple.png")
           self.appleImage.thumbnail((10, 10), Image.ANTIALIAS) 
           self.apple = ImageTk.PhotoImage(self.appleImage)
  
       except IOError as e:
           print (e)
           sys.exit(1)
  
       self.createObjects()
       self.locateApple()
       self.bind_all("<Key>", self.onKeyPressed)
       self.after(DELAY, self.onTimer)
  
   def createObjects(self):
       self.create_image(self.apple_x, self.apple_y, image=self.apple,
       anchor=NW, tag="apple")
       self.create_image(x[0], y[0], image=self.head, anchor=NW, tag="head")
       self.create_image(x[1], y[1], image=self.dot, anchor=NW, tag="dot")
       self.create_image(x[2], y[2], image=self.dot, anchor=NW, tag="dot") 
  
   def locateApple(self):
       apple = self.find_withtag("apple")
       self.delete(apple[0])
  
       r = random.randint(0, RAND_POS)
       self.apple_x = r * DOT_SIZE
       r = random.randint(0, RAND_POS)
       self.apple_y = r * DOT_SIZE
  
       self.create_image(self.apple_x, self.apple_y, image=self.apple,
                         anchor=NW, tag="apple") 
  
   def doMove(self):
       dots = self.find_withtag("dot")
       head = self.find_withtag("head")
  
       items = dots + head
  
       z = 0
  
       while z < len(items) - 1:
           c1 = self.coords(items[z])
           c2 = self.coords(items[z + 1])
           self.move(items[z], c2[0]-c1[0], c2[1]-c1[1])
           z += 1
  
       if self.left:
           self.move(head, -DOT_SIZE, 0)
  
       if self.right:
           self.move(head, DOT_SIZE, 0)
  
       if self.up:
           self.move(head, 0, -DOT_SIZE)
  
       if self.down:
           self.move(head, 0, DOT_SIZE)
  
   def checkCollisions(self):
       dots = self.find_withtag("dot")
       head = self.find_withtag("head")
  
       x1, y1, x2, y2 = self.bbox(head)
       overlap = self.find_overlapping(x1, y1, x2, y2)
  
       for dot in dots:
           for over in overlap:
               if over == dot:
                   self.inGame = False
  
       if x1 < 0: 
           self.inGame = False
       if x1 > WIDTH - DOT_SIZE:
           self.inGame = False
       if y1 < 0: 
           self.inGame = False
       if y1 > HEIGHT - DOT_SIZE:
           self.inGame = False
  
   def checkApple(self):
       apple = self.find_withtag("apple")
       head = self.find_withtag("head")
  
       x1, y1, x2, y2 = self.bbox(head)
       overlap = self.find_overlapping(x1, y1, x2, y2)
  
       for ovr in overlap:
           if apple[0] == ovr:
               x, y = self.coords(apple)
               self.create_image(x, y, image=self.dot, anchor=NW, tag="dot")
               self.locateApple()
  
   def onTimer(self): 
       if self.inGame:
           self.checkCollisions()
           self.checkApple()
           self.doMove()
           self.after(DELAY, self.onTimer)
       else:
           self.gameOver()
  
   def onKeyPressed(self, e):
       key = e.keysym
  
       if key == "Left" and not self.right:
          self.left = True
          self.up = False
          self.down = False
  
       if key == "Right" and not self.left:
           self.right = True
           self.up = False
           self.down = False
  
       if key == "Up" and not self.down:
           self.up = True
           self.right = False
           self.left = False
  
       if key == "Down" and not self.up:
           self.down = True
           self.right = False
           self.left = False
  
       if key == "Escape":
          self.quit()
  
   def gameOver(self):
      self.delete(ALL)
      self.create_text(self.winfo_width() / 2, self.winfo_height() / 2, 
                       text="Game Over", fill="white")
  
class Snake(Frame):
   def __init__(self, parent):
       Frame.__init__(self, parent)
       parent.title("Snake")
       self.board = Board(parent)
       self.pack()
  
root = Tk()
snake = Snake(root)
root.mainloop()