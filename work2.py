import turtle

turtle.bgcolor("black")
t = turtle.Pen()
t.pensize(2)
colors = ["red", "yellow","blue", "green","orange","purple"]
for x in range(200):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(61)
