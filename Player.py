from turtle import Turtle

PLAYER_WIDTH = 4
PLAYER_HEIGHT = 0.2
MARGIN = 10

MAX_RIGHT = 300 - MARGIN - (PLAYER_WIDTH * 10)
MAX_LEFT = -300 + MARGIN + (PLAYER_WIDTH * 10)
INIT_X = 0
INIT_Y = -280
MOVE_DISTANCE = 10

class Player(Turtle):

    def __init__(self):
        super().__init__(shape="square")
        self.shapesize(PLAYER_HEIGHT, PLAYER_WIDTH)
        self.setheading(0)
        self.color("white")
        self.penup()
        self.goto(INIT_X, INIT_Y)
        self.pendown()

    def move_right(self):
        if self.xcor() < MAX_RIGHT:
            self.penup()
            self.forward(MOVE_DISTANCE)
            self.pendown()

    def move_left(self):
        if self.xcor() > MAX_LEFT:
            self.penup()
            self.forward(-MOVE_DISTANCE)
            self.pendown()

