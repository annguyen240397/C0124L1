x = 5

def foo():

    global x

    x = 4

def bar(a, b):

    global x

    return a + b + x

foo()

print(bar(7, 8))