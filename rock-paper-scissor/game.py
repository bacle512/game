from tkinter import *
from PIL import Image, ImageTk
from random import randint

screen = Tk()
screen.title("Rock Scissor Paper")
screen.configure(background = 'light blue')

rock_img = ImageTk.PhotoImage(Image.open('rock-user.png'))
paper_img = ImageTk.PhotoImage(Image.open('paper-user.png'))
scissor_img = ImageTk.PhotoImage(Image.open('scissor-user.png'))
rockComp_img = ImageTk.PhotoImage(Image.open('rock-comp.png'))
paperComp_img = ImageTk.PhotoImage(Image.open('paper-comp.png'))
scissorComp_img = ImageTk.PhotoImage(Image.open('scissor-comp.png'))

user_label = Label(screen, image= scissor_img, bg= 'light blue')
comp_label = Label(screen, image= scissorComp_img, bg= 'light blue')
comp_label.grid(row = 1, column = 4)
user_label.grid(row = 1, column= 0)

#scores
playerScore = Label(screen, text = 0, font = 100, bg= 'light blue', fg= 'black')
playerScore.grid(row = 1, column = 1)
compScore = Label(screen, text = 0, font = 100, bg= 'light blue', fg= 'black')
compScore.grid(row = 1, column = 3)

#indicators
user_indicator = Label(screen, font= 50, text= 'USER', bg= 'light blue', fg= 'black')
user_indicator.grid(row= 0, column= 1)
comp_indicator = Label(screen, font= 50, text= 'COMPUTER', bg= 'light blue', fg= 'black')
comp_indicator.grid(row= 0, column= 3)

#messages
msg = Label(screen, font= 50, bg= 'light blue', fg= 'black')
msg.grid(row= 3, column= 2)

def updateMassage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playerScore['text'])
    score += 1
    playerScore['text'] = str(score)
    
def updateCompScore():
    score = int(compScore['text'])
    score += 1
    compScore['text'] = str(score)

#check winner
def checkWin(user, comp):
    if user == comp:
        updateMassage('Tie!!!')
        
    elif user == 'rock':
        if comp == 'paper':
            updateMassage('Computer won')
            updateCompScore()
        else:
            updateMassage('Player won')
            updateUserScore()
            
    elif user == 'paper':
        if comp == 'scissor':
            updateMassage('Computer won')
            updateCompScore()
        else:
            updateMassage('Player won')
            updateUserScore()
    
    elif user == 'scissor':
        if comp == 'rock':
            updateMassage('Computer won')
            updateCompScore()
        else:
            updateMassage('Player won')
            updateUserScore()
    
    else:
        pass

#update choices
choices = ['rock', 'paper', 'scissor']

def updateChoice(x):
    #for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == 'rock':
        comp_label.configure(image= rockComp_img)
    elif compChoice == 'paper':
        comp_label.configure(image= paperComp_img)
    else:    
        comp_label.configure(image= scissorComp_img)
        
    #for user
    if x == 'rock':
        user_label.configure(image= rock_img)
    elif x == 'paper':
        user_label.configure(image= paper_img)
    else:
        user_label.configure(image= scissor_img)
    
    checkWin(x, compChoice)

#buttons
rock = Button(screen, width= 20, height= 2, text= 'ROCK', bg= 'red', fg= 'white', command= lambda: updateChoice('rock')).grid(row= 2, column= 1)
paper = Button(screen, width= 20, height= 2, text= 'PAPER', bg= 'green', fg= 'white', command= lambda: updateChoice('paper')).grid(row= 2, column= 2)
scissor = Button(screen, width= 20, height= 2, text= 'SCISSOR', bg= 'blue', fg= 'white', command= lambda: updateChoice('scissor')).grid(row= 2, column= 3)

screen.mainloop()