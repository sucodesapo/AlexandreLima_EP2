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
base.forward(70)
base.right(90)
distance=100
ang=90

for i in range(1):
    base.forward(distance)
    base.right(ang)