from turtle import Turtle


class Brick:
    margin = 20
    margin = 20
    bricks_widthpx = 45
    bricks_heightpx = 30
    bricks_heightgap = 100

    def __init__(self, screen_width, screen_height):
        self.bricks = []
        self.bricks_width = 2
        self.bricks_height = 1
        self.name = "brick"
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.screen_width = 480
        self.screen_height = 500

    def create_brick(self, pos_x, pos_y, color):
        brick = Turtle(shape="square")
        brick.shapesize(self.bricks_height, self.bricks_width)
        brick.color(color)
        brick.penup()
        brick.goto(pos_x, pos_y)
        brick.pendown()
        return brick

    def create_bricks(self):
        top_x = -1 * int(self.screen_width / 2) + self.margin + 10
        top_y = int(self.screen_height / 2) - self.margin - self.bricks_heightgap

        brick_color = ["red", "orange", "green", "yellow"]
        for j in range(4):
            for i in range(int(self.screen_width / self.bricks_widthpx)):
                brick = self.create_brick( i*self.bricks_widthpx + top_x, -j*self.bricks_heightpx + top_y, brick_color[j])
                self.bricks.append(brick)

    def hidebrick(self, brick):
        brick.penup()
        brick.goto(99999, 99999)
        brick.pendown()