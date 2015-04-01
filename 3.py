# -*- coding: utf-8 -*-

import turtle

window=turtle.Screen()
window.bgcolor("lightblue")
window.title("Jogo do Mal")

base=turtle.Turtle()
base.speed(5)
base.color("black")
base.setpos(0,0)
base.left(90)
base.forward(250)
base.right(90)
base.forward(20)
base.right(90)
base.forward(40)

def cabeca():
    cabeca = turtle.Turtle()
    cabeca.penup()
    cabeca.setpos(20,190)
    cabeca.pendown()
    cabeca.circle(10)

cabeca()

def corpo():
    corpo=turtle.Turtle()
    corpo.penup()
    corpo.setpos(20,190)
    corpo.pendown()
    corpo.right(90)
    corpo.forward(50)

corpo()


window.exitonclick()