import math
import turtle
d=float(input("Nhap chieu dai la: "))
r=float(input("Nhap chieu rong la: "))
cv=(d+r)*2
s=d*r
print("Chu vi hcn co chieu dai {d}, chieu rong {r} la {cv}".format(d=d,r=r,cv=cv))
print("Dien tich hcn co chieu dai {d}, chieu rong {r} la {s}".format(d=d,r=r,s=s))
t=turtle.Turtle()
t.fillcolor("Brown")
t.begin_fill()
t.forward(d)
t.right(90)
t.forward(r)
t.right(90)
t.forward(d)
t.right(90)
t.forward(r)
t.end_fill()
turtle.done()