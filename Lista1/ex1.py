import turtle
# Allows us to use turtles
wn = turtle.Screen()
wn.bgcolor("lightgreen")
# Creates a playground for turtles
alex = turtle.Turtle()
# Create a turtle, assign to alex

def draw_rectangle(l, x, y):
    alex.penup()
    alex.goto(x,y)
    alex.pendown()
    alex.forward(l)
    alex.left(90)
    alex.forward(l)
    alex.left(90)
    alex.forward(l)
    alex.left(90)
    alex.forward(l)
    alex.left(90)


alex.pensize(1)
alex.pencolor("red")

draw_rectangle(20,0,0)
draw_rectangle(40,-10,-10)
draw_rectangle(60,-20,-20)
draw_rectangle(80,-30,-30)
draw_rectangle(100,-40,-40)
alex.penup()
alex.goto(-50,-50)
alex.pendown()




wn.mainloop() 
# Wait for user to close window
