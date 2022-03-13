import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# Creates a playground for turtles
tess = turtle.Turtle()
tess.pensize(1)
tess.pencolor("red")
# Create a turtle, assign to alex

def draw_poly (t,n,sz):
    for i in range (n):
        t.forward(sz)
        t.left(360/n)
        

draw_poly(tess,8,50)
wn.mainloop() 