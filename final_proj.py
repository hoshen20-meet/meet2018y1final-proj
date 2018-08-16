import turtle
import random
turtle.shape('blank')
t = turtle.clone()
t.shape('blank')
words = ('entrepreneurship','meet','nature','global warming','animals','recycle','treehous','plastic', 'pollution', 'water', 'ground','toxic waist','grass','forest','enviornment','earthquake','extinct','climate')
underscore_position = []

head_drawn = False
body_drawn = False
hand1_drawn = False
hand2_drawn = False
leg1_drawn = False
leg2_drawn = False
eye1_drawn = False
eye2_drawn = False
mouth_drawn = False

#user_word_input = input('enter a letter')
#user_input = input()
t.penup()
t.goto(-400,-300)
#functions here
#secret_word chooses a random word
secret_word = random.choice(words)
def words_length_underscore():
    for letter in secret_word:
    	underscore_position.append(t.pos())
    	t.pendown()
    	t.forward(20)
    	t.penup()
    	t.forward(20)
words_length_underscore()

turtle.penup()
turtle.goto (500,-300)
turtle.pendown()

#hanger
turtle.goto (500, -300)
turtle.goto (400, -300)
turtle.goto (400, 300)
turtle.goto (100, 300)
turtle.goto (100, 220)
global guess
guess = input('what letter would you like to guess')

def head():
#head
    global head_drawn
    turtle.circle(-50, 360)
    head_drawn = True

def body():
#for body
    global body_drawn
    turtle.penup()
    turtle.goto (100, 120)
    turtle.pendown()
    body_drawn = True
    #body
    turtle.goto (100, -110)
def hand1():
#for hand1
    global hand1_drawn
    turtle.penup()
    turtle.goto (100, 120)
    turtle.pendown()#hand1
    turtle.goto (150, 40)
    hand1_drawn = True
def hand2():
#for hand2
    global hand2_drawn
    turtle.penup()
    turtle.goto (100,120)
    turtle.pendown()
    #hand2
    turtle.goto (50, 40)
    hand2_drawn = True
def leg1():
#for leg1
    global leg1_drawn
    turtle.penup ()
    turtle.goto (100, -110)
    turtle.pendown ()#leg1
    turtle.goto (150, -190)
    leg1_drawn = True
def leg2():
#for leg2
    global leg2_drawn
    turtle.penup()
    turtle.goto ( 100, -110)
    turtle.pendown()
    #leg2
    turtle.goto (50, -190)
    leg2_drawn = True
def eye1():
#for eye1
    global eye1_drawn
    turtle.penup()
    turtle.goto (120, 190)
    turtle.pendown()
#eye1
    turtle.circle(-5, 360)
    eye1_drawn = True
def eye2():
#for eye2
    global eye2_drawn  
    turtle.penup()
    turtle.goto (80, 190)
    turtle.pendown()
#eye2
    turtle.circle(-5, 360)
    eye2_drawn = True

def mouth():
#for mouth
    global mouth_drawn
    turtle.penup()
    turtle.goto (80, 145)
    turtle.pendown()
    turtle.right(-90)
    turtle.circle(-20, 180)
    mouth_drawn = True

#without refactor:
#draw_part_functions = [eye1, eye2]
used_letters = []
correct_letters = 0
def check_letters():
#for letter in secret_word:
    global guess
    global correct_letters
    if guess.lower() in used_letters:
        print('you have already guessed that letter')
    elif not (guess.lower()) in secret_word.lower():
        if not head_drawn:
            head()
        elif not body_drawn:
            body()
        elif not hand1_drawn:
            hand1()
        elif not hand2_drawn:
            hand2()
        elif not leg1_drawn:
            leg1()
        elif not leg2_drawn:
            leg2()
        elif not eye1_drawn:
            eye1()
        elif not eye2_drawn:
            eye2()
        elif not mouth_drawn:
            mouth()
            t.goto(-400,180)
            t.color('red')
            t.write('YOU LOSE!!',font =  ('Comic Sans MS', 50, 'normal'))
            quit()
    else:
        for index_of_letter in range(0,len(secret_word)):
            letter = secret_word[index_of_letter]
            if letter.lower() == guess.lower():
                position_tuple_to_go_to = underscore_position[index_of_letter]
                t.goto(position_tuple_to_go_to)
                t.write(letter, font = ('Comic Sans MS', 20, 'normal'))
                print('YOU ARE RIGHT!')
                correct_letters += 1
                
    used_letters.append(guess.lower())
    if (len(secret_word) == correct_letters):
        print('YOU WON!!!')
        t.goto(-400,180)
        t.color('green')
        t.write('YOU WON!!!',font =  ('Comic Sans MS', 50, 'normal'))
        quit()
   # else:
        
    guess = input('enter another letter')
    check_letters()
           	 
check_letters()




