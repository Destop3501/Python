from tkinter import *
import random

def next_Turn(row,column):
    
    global player

    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:

            buttons[row][column]["text"] = player

            if check_winner() is True:
                label.config(text=(player + " Wins"))

            elif check_winner() is False:
                player = players[1]
                label.config(text=(player + " Turn"))

            elif check_winner() == "Tie":
                label.config(tect=("Tie"))

        else:
            
            buttons[row][column]["text"] = player

            if check_winner() is True:
                label.config(text=(player + " Wins"))

            elif check_winner() is False:
                player = players[0]
                label.config(text=(player + " Turn"))

            elif check_winner() == "Tie":
                label.config(text=("Tie"))

def check_winner():

    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] !="" :
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] !="" :
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
        
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] !="" :
            buttons[0][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[2][2].config(bg="green")
            return True
    
    elif buttons[2][0]["text"] == buttons[1][1]["text"] == buttons[0][2]["text"] !="" :
            buttons[2][0].config(bg="green")
            buttons[1][1].config(bg="green")
            buttons[0][2].config(bg="green")
            return True
    
    elif empty_Space() is False:
        for row in range (3):
            for column in range (3):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    else:
        return False

def empty_Space():
    
    spaces = 9

    for row in range (3):
        for column in range (3):
            if buttons[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def New_game():
    global player

    player = random.choice(players)

    label.config(text=player + " Turn")

    for row in range (3):
        for column in range (3):
            buttons[row][column].config(text="", bg="white")

window = Tk()
window.title("Tik Tak Toe")

players = ["x", "o"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text= player + " Turn", font=('consolas',40))
label.pack(side= TOP)

reset_button = Button(text="Restart", font=("consolas", 20), command=New_game)
reset_button.pack()

frame = Frame(window)
frame.pack()

for row in range (3):
    for column in range (3):
        buttons[row][column] = Button(frame, text="", font=('consolas',40), height=2, width=4, bg="white",
                                       command= lambda row=row, column=column: next_Turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()