import turtle
import random

t = turtle.clone()

words = ('entrepreneurship','meet','nature','global warming','animals','recycle','tree','plastic', ' pollution')
underscore_position = []

#user_word_input = input('enter a letter')
#user_input = input()
t.penup()
t.goto(-400,0)
#functions here
#secret_word chooses a random word
secret_word = random.choice(words)
print(secret_word)
def words_length_underscore():
    for letter in secret_word:
        underscore_position.append(t.pos())
        t.pendown()
        t.forward(20)
        t.penup()
        t.forward(20)
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
global guess
guess = input('what letter would you like to guess')

def head():
#head
	turtle.circle(-50, 360)
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
	turtle.circle(-5, 360)
def eye2():
#for eye2
	turtle.penup()
	turtle.goto (20, 190)
	turtle.pendown()

#eye2
	turtle.circle(-5, 360)

def mouth():
#for mouth
	turtle.penup()
	turtle.goto (-20, 145)
	turtle.pendown()
	turtle.right(-90)
	turtle.circle(-20, 180)

#mouth_data = (-20, 145, -90, -20, 180)

#without refactor:
#draw_part_functions = [eye1, eye2]

i = -1
def check_letter_index():
#for letter in secret_word:
    global guess
    for index_of_letter in range(0,len(secret_word)):
            letter = secret_word[index_of_letter]
            print('checking letter: '+letter)
            if letter == guess:
                position_tuple_to_go_to = underscore_position[index_of_letter]
                
                turtle.goto(position_tuple_to_go_to)
                turtle.write(letter)
                guess = input('enter another letter')
            elif letter != guess:
                head()
                guess =input()
                print('here')
            elif letter != guess:
                body()
                guess = input()
            elif letter != guess:
                hand1()
                guess = input('enter a letter')
            elif letter != guess:        
                hand2()
                guess = input('enter a letter')
            elif letter != guess:
                leg1()
                guess = input('enter a letter')
            elif letter != guess:
                leg2()
                guess = input('enter a letter')
            elif letter != guess:
                eye1()
                guess = input('enter a letter')
            elif letter != guess:
                eye2()
                guess = input('enter a letter')
            elif letter != guess:
                mouth()
                guess = input('enter a letter')
            else:
                print('you`re right')
                
def printhi(thing_to_print):
	print(thing_to_print)
check_letter_index()
