import turtle
import random

t = turtle.clone()

words = ('entrepreneurship','meet','nature','global warming','animals','recycle','tree','plastic', ' pollution')
underscore_position = []

#user_word_input = input('enter a letter')
#user_input = input()
t.penup()
t.goto(-500,0)
#functions here
#word_chooser chooses a random word
word_chooser = random.choice(words)
print(word_chooser)
def words_length_underscore():
    for letter in word_chooser:
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(20)
        underscore_position.append(t.pos())
        print(underscore_position)
words_length_underscore()



turtle.penup()
turtle.goto (400,-300)
turtle.pendown()

#hanger
turtle.goto (400, -300)
turtle.goto (300, -300)
turtle.goto (300, 300)
turtle.goto (0, 300)
turtle.goto (0, 220)

def head():
#head
    turtle.circle(-50)
def body():
#for body
    turtle.penup()
    turtle.goto (0, 120)
    turtle.pendown()
    #body
    turtle.goto (0, -110)
def hand1():
#for hand1
    turtle.penup()
    turtle.goto (0, 120)
    turtle.pendown()
#hand1
    turtle.goto (50, 40)
def hand2():
#for hand2
    turtle.penup()
    turtle.goto (0,120)
    turtle.pendown()

    #hand2
    turtle.goto (-50, 40)
def leg1():
#for leg1
    turtle.penup ()
    turtle.goto (0, -110)
    turtle.pendown ()

#leg1
    turtle.goto (50, -190)
def leg2():
#for leg2
    turtle.penup()
    turtle.goto ( 0, -110)
    turtle.pendown()

#leg2
    turtle.goto (-50, -190)
def eye1():
#for eye1
    turtle.penup()
    turtle.goto (-20, 190)
    turtle.pendown()

#eye1
    turtle.circle(-5)
def eye2():
#for eye2
    turtle.penup()
    turtle.goto (20, 190)
    turtle.pendown()

#eye2
    turtle.circle(-5)

    turtle.penup()
    turtle.goto (-20, 145)
    turtle.pendown()

    turtle.right(-90)
    turtle.circle(-20, 180)
