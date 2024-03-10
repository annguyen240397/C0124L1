import turtle
t=turtle.Turtle()
t.hideturtle()
t.pencolor('red')
def hv(a):
    for i in range(4):
        t.forward(a)
        t.right(90)
    turtle.done()
b=int(input("Nhap gia tri cua canh: "))
hv(b)