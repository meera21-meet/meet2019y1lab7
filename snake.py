import turtle
import random 

turtle.tracer(1,0) 

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) 
                         
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 3
TIME_STEP = 100


pos_list = []
stamp_list = []
food_pos = []
food_stamps = []


snake = turtle.clone()
snake.shape("square")


turtle.hideturtle()


def new_stamp():
    snake_pos = snake.pos() 
    
    pos_list.append(snake.pos) 
             
    snake_stamp = snake.stamp()
       
    stamp_list.append(snake_stamp)

     
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1] 

    
    x_pos+=SQUARE_SIZE

    snake.goto( x_pos, y_pos)
   
    new_stamp()

def remove_tail():
    old_stamp = stamp_list.pop (0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

def up():
    snake.direction = 'up'
    move_snake()
    print ("you pressed the up key!")
def down():
    snake.direction = 'down'
    move_snake()
    print ("you pressed the down key!")
def left ():
    snake.direction ='left'
    move_snake()
    print ("you pressed the left key!")
def right ():
    snake.direction ='right'
    move_snake()
    print ("you pressed the right key!")

turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "right")

turtle.listen()

def move_snake():
    my_pos= snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if snake.direction=="up":
        snake.goto(x_pos, SQUARE_SIZE)
        print("you moved up!")
    elif snake.direction=="Down":
         snake.goto(x_pos, y_pos - SQUARE_SIZE)
    elif snake.direction=="Right":
         snake.goto(x_pos, y_pos + SQUARE_SIZE)
    elif snake.direction=="Left":
         snake.goto(x_pos, y_pos - SQUARE_SIZE)

    new_stamp()
    remove_tail()
    new_pos=snake.pos()

turtle.mainloop()
