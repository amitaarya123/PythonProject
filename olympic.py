from turtle import *

t=Turtle()
t.pensize(30)
t.penup()
t.right(180)
t.forward(190)
t.pendown()

t.color("yellow")
t.circle(140,360)
t.penup()
t.home()
t.right(180)
t.forward(-150)
t.pendown()


t.color("green")
t.circle(140,360)
t.penup()
t.home()
t.left(180)
t.forward(500)
t.left(90)
t.forward(-10)
t.pendown()

t.color("blue")
t.circle(140,360)
t.penup()
t.home()
t.forward(120)
t.left(90)
t.forward(10)
t.pendown()


t.color("black")
t.circle(140,360)
t.penup()
t.home()
t.forward(460)
t.left(90)
t.forward(10)
t.pendown()

t.color("red")
t.circle(140,360)

t.done()