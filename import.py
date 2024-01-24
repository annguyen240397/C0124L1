#turtle
#math
import math
import turtle
r=int(input("Nhap ban kinh: "))
S=math.pi * (r**2)
print("Dien tich cua hinh tron la ", S)
print("Diện tích của hình tròn có bán kính = {r} là {S}".format(r=r, S=S))
t = turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.color("red")
t.fillcolor("yellow")
t.begin_fill()
t.circle(r)
t.end_fill()
turtle.done()