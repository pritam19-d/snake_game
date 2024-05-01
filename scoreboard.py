from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 300)
        self.score = -1

    def update_score (self):
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", False, "center", ("ariel", 14, "bold"))

    def game_reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as data:
                self.high_score = data.write(f"{self.score}")
        self.score = -1
        self.update_score()
