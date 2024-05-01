import time
from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_body[0].color("red")

    def create_snake(self):
        x_pos = 0
        position = (x_pos, 0)
        for i in range(3):
            self.add_segment(position)
            x_pos -= 20

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move_snake(self):
        for n in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[n].goto(self.snake_body[n-1].pos()) # to move each segment (from the last) and go to it's previous segment position
        self.snake_body[0].forward(20)

    def right(self):
        if not self.snake_body[0].heading() == 180:
            self.snake_body[0].setheading(0)
    def up(self):
        if not self.snake_body[0].heading() == 270:
            self.snake_body[0].setheading(90)
    def left(self):
        if not self.snake_body[0].heading() == 0:
            self.snake_body[0].setheading(180)
    def down(self):
        if not self.snake_body[0].heading() == 90:
            self.snake_body[0].setheading(270)

    def snake_reset(self):
        time.sleep(0.3)
        for i in self.snake_body:
            i.teleport(-6000, -6000)
        self.snake_body.clear()

        time.sleep(0.2)
        self.create_snake()
        self.snake_body[0].color("red")