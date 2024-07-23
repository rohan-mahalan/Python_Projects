from turtle import Turtle, Screen
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class BODY:
    def __init__(self):
        self.segments = []
        for i in range(0, 3):
            n = Turtle()
            n.penup()
            n.shape("square")
            n.color("white")
            n.goto(POSITIONS[i])
            self.segments.append(n)

    # method for moving the snake
    def movement(self):
        for i in range(len(self.segments)-1, 0, -1):
            x_pos = self.segments[i-1].xcor()
            y_pos = self.segments[i-1].ycor()
            self.segments[i].goto(x_pos, y_pos)
        self.segments[0].forward(20)

    # method for increasing the size of the snake
    def new_part(self):
        n = Turtle()
        # making sure that new block doesn't show up on screen
        n.goto(999, 999)
        n.penup()
        n.shape("square")
        n.color("white")
        self.segments.append(n)

