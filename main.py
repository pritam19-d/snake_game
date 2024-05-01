from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()
my_screen = Screen()

my_screen.setup(750,650)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

is_game_over = False

scoreboard.update_score()
while not is_game_over:
    snake.move_snake()
    time.sleep(0.1)
    if snake.snake_body[0].distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.update_score()
    my_screen.update()
    ## A Game over function when the snake get hit the wall and another as same when the snake hit the screen edge
    if not -350 < snake.snake_body[0].xcor() < 350 or not -310 < snake.snake_body[0].ycor() < 310:
        scoreboard.game_reset()
        snake.snake_reset()
    # The easy mode where it wont hit the wall
    # if not -380 < snake.snake_body[0].xcor() < 370:
    #     snake.snake_body[0].goto((snake.snake_body[0].xcor())*-1, snake.snake_body[0].ycor())
    # if not -310 < snake.snake_body[0].ycor() < 300:
    #     snake.snake_body[0].goto(snake.snake_body[0].xcor(), (snake.snake_body[0].ycor())*-1)
    # Another Game over function when the snake hits its own body
    for each_segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(each_segment) < 10:
            scoreboard.game_reset()
            snake.snake_reset()


print(my_screen.canvheight, my_screen.canvwidth)
my_screen.exitonclick()