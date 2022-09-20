import time
from turtle import Turtle, Screen
from Brick import Brick
from Player import Player
from Ball import Ball

screen_width: int = 600
screen_height = 600

# setup screen
screen = Screen()
screen.setup(screen_width + 20, screen_height + 20)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer(0)

# Wall
box = Turtle()
box.color("red")
box.hideturtle()
box.penup()
box.goto(-screen_width / 2 + 2, screen_height / 2 - 2)
box.pendown()
box.goto(screen_width / 2 - 2, screen_height / 2 - 2)
box.goto(screen_width / 2 - 2, -screen_height / 2 + 2)
box.goto(-screen_width / 2 + 2, -screen_height / 2 + 2)
box.goto(-screen_width / 2 + 2, screen_height / 2 - 2)
box.penup()
screen.tracer(0)

# Brick
bricks = Brick(screen_width, screen_height)
bricks.create_bricks()
player = Player()
ball = Ball()

screen.listen()
screen.onkeypress(key="Right", fun=player.move_right)
screen.onkeypress(key="Left", fun=player.move_left)

while True:
    ball.move()
    if ball.isBallOutOfRange():
        print("Game Over")
        break

    if ball.hitPlayerBoard(player):
        ball.bounce(player)

    for brick in bricks.bricks:
        if ball.distance(brick) < 20:
            ball.bounce(brick)
            bricks.hidebrick(brick)

    time.sleep(0.05)
    screen.update()

screen.exitonclick()