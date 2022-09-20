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
        if x > WALL_FAR_X[1] :
            if angle > 0 and angle <= 90:
                angle = 180 - angle
            elif angle > 270 and angle <= 360:
                angle = 360 - angle + 180
        elif x < WALL_FAR_X[0] :
            if angle > 90 and angle <= 180:
                angle = 90 - (angle - 90)
            elif angle > 180 and angle <= 270:
                angle = 270 - angle + 270
        elif y > WALL_FAR_Y[1] and y > prevY:
                if x > prevX:
                    angle = 270 + (90 - angle)
                else:
                    angle = 270 - (angle - 90)

        self.prevY = y
        self.prevX = x

        self.setheading(angle)
        self.penup()
        self.forward(MOVE_DISTANCE)
        self.pendown()

    def bounce(self, board:Turtle):
        x = self.xcor()
        y = self.ycor()

        angle = self.heading()

        if board.ycor() == -280:
            # bounce player board

            playerX = board.xcor()
            playerWidth = board.shapesize()[1]
            playerXStart = playerX - 20 * (playerWidth / 2)
            playerXEnd = playerX + 20 * (playerWidth / 2)

            print(x, playerXStart, playerXStart, playerXEnd, angle)
            angle = (((x - playerXStart) / (playerXStart + playerXEnd)) - 0.5) * 20 + angle

            if angle <= 180:
                angle = 180 - angle
            else:
                angle = 180 - ( angle - 180 )

        else:
            # bounce brick
            if y > self.prevY:
                if angle > 180 and angle < 360:
                    angle = ( 360 - angle ) + 180
                elif angle <= 90:
                    angle = 360 - angle
                else:
                    angle = -1 * (angle - 360)
            elif y < self.prevY:
                if angle >= 270:
                    angle = 360 - angle
                elif angle > 180 and angle < 270:
                    angle = 270 - angle + 90

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
        #print(x, y, playerY, distanceY, playerXStart, playerXEnd)

        return distanceY >=0 and distanceY <= 10 and x >= playerXStart and x <= playerXEnd
        #return self.distance(player) < 20