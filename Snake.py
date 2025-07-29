from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 250
SPEED_UP = 1
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = "Green"
FOOD_COLOUR = "Red"
BACKGROUND_COLOUR = "Black"

canvas = NONE
label = None

class Snake:
   
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range (0 , BODY_PARTS):
            self.coordinates.append([0, 0])

        for x , y in self.coordinates:
            square = canvas.create_rectangle(x , y, x + SPACE_SIZE, y + SPACE_SIZE, fill= SNAKE_COLOUR, tags="snake")
            self.squares.append(square)

class Food:
    
    def __init__(self):
        
        x = random.randint(0, int(GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, int(GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x , y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tags="food")

def next_turn(snake, food):
    
    global SPEED

    x , y = snake.coordinates[0]

    if direction == "Up":
        y -= SPACE_SIZE
    elif direction == "Down":
        y += SPACE_SIZE
    elif direction == "Right":
        x += SPACE_SIZE
    elif direction == "Left":
        x -= SPACE_SIZE

    snake.coordinates.insert(0 , (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tags="snake")
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score
        
        score += 1
        label.config(text="Score : {}".format(score))

        SPEED -= SPEED_UP

        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collition(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):

    global direction

    if new_direction == "Left":
        if direction != "Right":
            direction = new_direction

    elif new_direction == "Down":
        if direction != "Up":
            direction = new_direction

    elif new_direction == "Right":
        if direction != "Left":
            direction = new_direction
 
    elif new_direction == "Up":
        if direction != "Down":
            direction = new_direction

def check_collition(snake):
    x,y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    
    elif y < 0 or y >GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=("consolas", 70), text="GAME OVER", fill="red", tags="game over")
    
    button1 = Button(window, text="RESTART", font=("consolas", 40),bg="#3C3C3C",
                     command= Restart)
    canvas.create_window(canvas.winfo_width()/2, (canvas.winfo_height()/2 + 100), window=button1)

def Restart():

    global canvas
    global label

    canvas.destroy()
    label.destroy()
    Game_Canvas()

def Game_Canvas():

    global score
    global direction
    global canvas
    global label
    global SPEED

    SPEED = 250
    score = 0
    direction = 'Down'

    label = Label(window, text="Score : {}".format(score), font=("consolas, 40"))
    label.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOUR, width=GAME_WIDTH, height=GAME_HEIGHT)
    canvas.pack()

    snake = Snake()
    food = Food()

    next_turn(snake , food)


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

Game_Canvas()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2) - 40)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event: change_direction("Left"))
window.bind("<Right>", lambda event: change_direction("Right"))
window.bind("<Up>", lambda event: change_direction("Up"))
window.bind("<Down>", lambda event: change_direction("Down"))

window.mainloop()