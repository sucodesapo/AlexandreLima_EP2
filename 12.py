# -*- coding: utf-8 -*-

import turtle

window=turtle.Screen()
window.bgcolor("lightblue")
window.title("Jogo do Mal")
window.setup(width=1500, height=700, startx=0, starty=0)


base=turtle.Turtle()
base.speed(5)
base.color("black")
base.penup()
base.setpos(-300,-50)
base.pendown()
base.left(90)
base.forward(250)
base.right(90)
base.forward(20)
base.right(90)
base.forward(40)

def cabeca():
    cabeca = turtle.Turtle()
    cabeca.penup()
    cabeca.setpos(-280,140)
    cabeca.pendown()
    cabeca.circle(10)
    
    
def corpo():
    corpo=turtle.Turtle()
    corpo.penup()
    corpo.setpos(-280,140)
    corpo.pendown()
    corpo.right(90)
    corpo.forward(50)
    
def braco1():
    braco1=turtle.Turtle()
    braco1.penup()
    braco1.setpos(-280,140)
    braco1.pendown()
    braco1.right(30)
    braco1.forward(20)
    
def braco2():
    braco2=turtle.Turtle()
    braco2.penup()
    braco2.setpos(-280,140)
    braco2.pendown()
    braco2.right(150)
    braco2.forward(20)
    
def perna():
    perna=turtle.Turtle()
    perna.penup()
    perna.setpos(-280,100)
    perna.pendown()
    perna.right(30)
    perna.forward(20)  
    
def perna2():
    perna2 =turtle.Turtle()
    perna2.penup()
    perna2.setpos(-280,100)
    perna2.pendown()
    perna2.right(150)
    perna2.forward(20)
    
arquivo=open("entrada.txt",encoding = 'utf-8')
lines=arquivo.readlines()

cleanlist=[]
for number in range(0, len(lines)):
        clean=lines[number].strip()      
        if clean != "":
            cleanlist.append(clean)
import random

escolha = random.choice(cleanlist)

t = len(escolha)

def gap(size):
    gapT=turtle.Turtle()
    gapT.penup()
    gapT.setpos(-250,-50)
    gapT.pendown()
    for x in range(0,size):
        gapT.right(0)
        gapT.forward(40)
        gapT.penup()
        gapT.forward(10)
        gapT.pendown()

gap(t)

w=0
while w<6:
    tentativa =  window.textinput("Jogo do Mal", "Escolha uma letra: ")
    wrotealetter = False
    for i in range(0,t):
        if tentativa==escolha[i]:
            turtle.penup()
            turtle.setpos(10*i,0)
            turtle.setpos(-250+50*i,-50)
            
            turtle.write(tentativa, font=("Arial",20))
            wrotealetter = True
    if not wrotealetter:
        w+=1

        if w==1:
            cabeca()
        elif w==2:
            corpo()
        elif w==3:
            braco1()
        elif w==4:
            braco2()
        elif w==5:
            perna()
        elif w==6:
            perna2()
            turtle.setpos(0,0)
            turtle.write("GAME OVER", font=("Arial",25))
    
    
window.exitonclick()