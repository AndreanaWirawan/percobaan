import turtle as t
t.bgcolor("pink")
t.speed(0)
t.width(12)
t.title("SELAMAT DATANG")

def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)
def heart():
    t.color("red","red")
    t.begin_fill()
    t.left(a)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()

heart()
t.pencolor("white")
t.penup()
t.goto(0,170)
t.pendown()

for zigzag in range(3):
    t.edge_right(a)
    t.forward(40)
    t.edge_left(u)
    t.forward(40)

t.done()
