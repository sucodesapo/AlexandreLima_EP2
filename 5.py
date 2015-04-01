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

def corpo():
    corpo=turtle.Turtle()
    corpo.penup()
    corpo.setpos(20,190)
    corpo.pendown()
    corpo.right(90)
    corpo.forward(50)

def braco1():
    braco1=turtle.Turtle()
    braco1.penup()
    braco1.setpos(20,190)
    braco1.pendown()
    braco1.right(30)
    braco1.forward(20)

def braco2():
    braco2=turtle.Turtle()
    braco2.penup()
    braco2.setpos(20,190)
    braco2.pendown()
    braco2.right(150)
    braco2.forward(20)

def perna():
    perna=turtle.Turtle()
    perna.penup()
    perna.setpos(20,140)
    perna.pendown()
    perna.right(30)
    perna.forward(20)  

def perna2():
    perna2=turtle.Turtle()
    perna2.penup()
    perna2.setpos(20,140)
    perna2.pendown()
    perna2.right(150)
    perna2.forward(20)
    

arquivo=open("entrada.txt","r", encoding = 'utf-8')
lines=arquivo.readlines()
print(lines)

cleanlist=[]
for number in range(0, len(lines)):
        clean=lines[number].strip()
        cleanlist.append(clean)
print(cleanlist)


window.exitonclick()