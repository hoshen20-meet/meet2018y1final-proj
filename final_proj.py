
import turtle
import random

t = turtle.clone()

words = ('entrepreneurship','meet','nature','global warming','animals','recycle','tree','plastic', ' pollution')

#user_word_input = input('enter a letter')
#user_input = input()
t.penup()
t.goto(-400,0)
#functions here
def words_length_underscore():
    for word_list_counter in word_chooser:
        for letter in range (len(word_list_counter)) > 4:
            t.pendown()
            t.forward(20)
            t.penup()
            t.forward(20)
            
words_length_underscore()



turtle.penup()
turtle.goto (100,-300)
turtle.pendown()

#hanger
turtle.goto (400, -300)
turtle.goto (300, -300)
turtle.goto (300, 300)
turtle.goto (0, 300)
turtle.goto (0, 220)

#haed
turtle.circle(-50)
#for body
turtle.penup()
turtle.goto (0, 120)
turtle.pendown()

#body
turtle.goto (0, -110)
#for hand1
turtle.penup()
turtle.goto (0, 120)
turtle.pendown()

#hand1
turtle.goto (50, 40)

#for hand2
turtle.penup()
turtle.goto (0,120)
turtle.pendown()

#hand2
turtle.goto (-50, 40)

#for leg1
turtle.penup ()
turtle.goto (0, -110)
turtle.pendown ()

#leg1
turtle.goto (50, -190)

#for leg2
turtle.penup()
turtle.goto ( 0, -110)
turtle.pendown()

#leg2
turtle.goto (-50, -190)

#for eye1
turtle.penup()
turtle.goto (-20, 190)
turtle.pendown()

#eye1
turtle.circle(-5)

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
