from random import *
import time
from turtle import *
from tkinter import *

easyDifficulty = False
mediumDifficulty = False
hardDifficulty = False
leftDoor = False
centerDoor = False
rightDoor = False
a = 0#door number
b = 0#ghost number
score =0
wid = 300
hei = 500
dia = 10

#ingame messages
message0 ='''
In front of you there are three doors.
Behind one of them hides a ghost.
You have to make right decissions in order to get out
safely.
'''
message1 = '''
There were no ghosts behind this door.
you can go further.
'''
message2 = '''
You have managed to escape the mansion.
Congratulations and thank you for playing.
'''

message3 = '''
You have encountered a ghost.
Your life ends here...
'''

#difficulties 
def easy():
    global easyDifficulty
    easyDifficulty = not easyDifficulty

     
def medium():
    global mediumDifficulty
    mediumDifficulty = not mediumDifficulty

def hard():
    global hardDifficulty
    hardDifficulty = not hardDifficulty
    
def closeWindow():
    window.destroy()

#player choices

def left_door():
    global leftDoor
    leftDoor = not leftDoor

def center_door():    
    global centerDoor
    centerDoor = not centerDoor
    
def right_door():    
    global rightDoor
    rightDoor = not rightDoor
    
#grafical stuff

def resetScreen(a,b):
    reset()
    speed(1000)
    up()
    backward(a)
    left(90)
    forward(b)
    right(90)
    down()

    
def repositionDoor():
        up()
        backward(150)
        right(90)
        forward(250)
        right(90)
        down()

def door(wid,hei,dia):
    for i in range(2):
        forward(wid)
        right(90)
        forward(hei)
        right(90)
    forward(wid)
    right(90)
    forward(hei/2)
    right(90)
    up()
    forward(dia*2)
    down()
    circle(dia)

def doors():
    resetScreen(550,250)
    for i in range(3):        
        door(wid,hei,dia)
        repositionDoor()
        

def deathScreen():
    resetScreen(150,250)
    Screen().bgcolor("black")

#def resetMessage():
    
    
def game():
    global a
    global b
    global score
    global message1
    global message2
    global message3
    doors()
    #generating a ghost position depending on difficulty
    if easyDifficulty == True:
        b = randint(1,7)
    elif mediumDifficulty == True:
        b = randint(1,5)
    elif hardDifficulty == True:
        b = randint(1,3)
    #choosing the door
    if leftDoor == True:
        a = 1
        if a != b:
            T.delete("1.0", 'end')
            T.insert('end', message1)
            score = score + 1
    elif centerDoor == True:
        a = 2
        if a != b:
            T.delete("1.0", 'end')
            T.insert('end', message1)
            score = score + 1
    elif rightDoor == True:
        a = 3
        if a != b:
            T.delete("1.0", 'end')
            T.insert('end', message1)
            score = score + 1
    if score == 25:
        T.delete("1.0", 'end')
        T.insert('end', message2)
        time.sleep(5)
        quit()
    elif a == b:
        deathScreen()
        T.delete("1.0", 'end')
        T.insert('end', message3)
        print( "Yor score is ", score)
        time.sleep(5)
        quit()



#Difficulty settings
window = Tk()
window.title('Select difficulty')
window.geometry('450x100')


btn1 = Button(window, text='Easy', height = 6, width = 20, command=lambda:[ easy(), closeWindow()] )
btn1.grid(column=1, row=0)

btn2 = Button(window, text = 'Medium', height = 6, width = 20, command=lambda:[ medium(), closeWindow()] )
btn2.grid(column=2, row=0)

btn3 = Button(window, text = 'Hard', height = 6, width = 20, command=lambda:[ hard(), closeWindow()] )
btn3.grid(column=3, row=0)

window.mainloop()

#Controls
window = Tk()
window.title('The haunted mansion')
window.geometry('450x200')


T = Text(window, height = 6, width = 57)
T.grid(column=1,row=0, columnspan = 3)
T.insert('end', message0)


btnA = Button(window, text='Left', height = 6, width = 20, command = lambda:[left_door(), game()] )
btnA.grid(column=1, row=2)
    
btnB = Button(window, text='Center', height = 6, width = 20, command = lambda:[center_door(), game()])
btnB.grid(column=2, row=2)
    
btnC = Button(window, text='Right', height = 6, width = 20, command = lambda:[right_door(),game()])
btnC.grid(column=3, row=2) 
    
window.mainloop()



