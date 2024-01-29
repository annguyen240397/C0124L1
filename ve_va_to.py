import turtle
shapeinput = input('circle and square, what is your favourite shape?: ')
if shapeinput == 'circle' or shapeinput == 'square' or shapeinput == 'turtle':
    colorinput = input('What color will it be?, yellow, red or blue?: ')
    if colorinput == 'red' or colorinput == 'yellow' or colorinput == 'blue' :
        wn = turtle.Screen()
        wn.bgcolor('black')
        wn.title('your shape')
        t = turtle.Turtle()
        t.shape(shapeinput)
        t.color(colorinput)
        turtle.done()
    else :
        print('Sorry, i dont have this color :(')
else :
    print('sorry, i dont have this shape :(')