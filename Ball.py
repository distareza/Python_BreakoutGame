import math
from turtle import Turtle

INIT_X = 0
INIT_Y = -180
BALL_RADIUS = .5
MOVE_DISTANCE = 10
WALL_FAR_X = ( -280, 280)
WALL_FAR_Y = ( -280, 280)

INIT_ANGLE = 45

class Ball(Turtle):

    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.shapesize(BALL_RADIUS)
        self.prevY = -280
        self.prevX = 0
        self.setheading(INIT_ANGLE)

        self.penup()
        self.goto(INIT_X, INIT_Y)
        self.pendown()

    def move(self):
        x = self.xcor()
        y = self.ycor()
        prevX = self.prevX
        prevY = self.prevY
        angle = self.heading()

        # Bounch when hit the wall
        if x > WALL_FAR_X[1] and x > prevX:
            if y > prevY:
                angle += 90
            else:
                angle -= 90
        if x < WALL_FAR_X[0] and x < prevX:
            if y < prevY:
                angle += 90
            else:
                angle -= 90
        if y > WALL_FAR_Y[1]:
            if x > prevX:
                angle -= 90
            else:
                angle += 90

        self.prevY = y
        self.prevX = x

        self.setheading(angle)
        self.penup()
        self.forward(MOVE_DISTANCE)
        self.pendown()

    def bounce(self, point):
        x = self.xcor()
        y = self.ycor()

        angle = self.heading()
        if x < self.prevX and y < self.prevY:
            angle -= 90 + point
        else:
            angle += 90 + point
        # if self.prevy < self.ycor():
        #     angle += 90
        # elif self.prevy > self.ycor():
        #     angle -= 90
        # self.prevy = y

        self.setheading(angle)
        self.penup()
        self.forward(MOVE_DISTANCE)
        self.pendown()

    def isBallOutOfRange(self):
        return self.ycor() < -300

    def calculateAngle(self):
        x = self.xcor()
        y = self.ycor()
        prevX = self.prevX
        prevY = self.prevY
        r = math.degrees(math.atan2(y-prevY, x-prevX))

    def hitPlayerBoard(self, player:Turtle):
        x = self.xcor()
        y = self.ycor()
        playerX = player.xcor()
        playerY = player.ycor()
        playerWidth = player.shapesize()[1]
        playerXStart = playerX - 20*(playerWidth/2)
        playerXEnd = playerX + 20*(playerWidth/2)

        distanceY = y - playerY
        print(x, y, playerY, distanceY, playerXStart, playerXEnd)

        return distanceY >=0 and distanceY <= 20 and x >= playerXStart and x <= playerXEnd
        #return self.distance(player) < 20