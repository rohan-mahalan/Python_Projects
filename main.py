from turtle import Screen
from snake import BODY
from food import FOOD
from score import SCORE
import time

# stores the score of the player
my_score = SCORE()
y = Screen()
y.screensize(canvwidth=800, canvheight=800)
y.listen()
y.title(f"Snake Game    Score : {my_score.high_score}")
y.bgcolor("black")
y.tracer(0)

bite = FOOD()
rick = BODY()

flag = 1


def up():
    # make sure the snake doesn't go up while moving downwards
    if rick.segments[0].heading() != 270:
        rick.segments[0].setheading(90)


def down():
    if rick.segments[0].heading() != 90:
        rick.segments[0].setheading(270)


def right():
    if rick.segments[0].heading() != 180:
        rick.segments[0].setheading(0)


def left():
    if rick.segments[0].heading() != 0:
        rick.segments[0].setheading(180)


while flag == 1:
    time.sleep(0.1)

    # making the snake to move on its own
    rick.movement()
    # capturing the keystrokes
    y.onkey(fun=up, key="Up")
    y.onkey(fun=down, key="Down")
    y.onkey(fun=right, key="Right")
    y.onkey(fun=left, key="Left")
    # snake eating the food
    if rick.segments[0].distance(bite) < 20:
        # moving the food to new position
        bite.new_position()
        # extending the snake
        rick.new_part()
        # increasing the score
        my_score.update_score()
        y.title(f"Snake Game    Score : {my_score.high_score}")
    # checking collision with itself
    for i in range(1, len(rick.segments)):
        if rick.segments[0].distance(rick.segments[i]) < 10:
            flag = 0
    # checking collision with the wall
    if rick.segments[0].xcor() > 320 or rick.segments[0].ycor() > 280:
        flag = 0
    if rick.segments[0].xcor() < -320 or rick.segments[0].ycor() < -280:
        flag = 0
    y.update()
y.exitonclick()
