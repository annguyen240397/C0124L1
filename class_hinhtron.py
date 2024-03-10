import turtle
import math
class Circle:
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    def draw(self):
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        t.circle(self.r)
        turtle.done()
    def cv(self):
        return self.r * 2 * math.pi
    def dt(self):
        return self.r * self.r * math.pi
circle1 = Circle(100, 100, 200)
circle2 = Circle(100, -100, -200)
circle3 = Circle(10, 100, 200)
print(circle3.dt())
print(circle2.cv())