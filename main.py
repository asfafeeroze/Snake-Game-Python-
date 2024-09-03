# main.py
# https://docs.python.org/3.10/library/turtle.html
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)  # adjusting our window size
screen.bgcolor("black")
screen.title("Simple Snake Game")
screen.tracer(0)  # turning off tracer (make sure to use update method after doing this)

# Creating the Snake Body
#
# snake_body = []
# x_cor = 0
# for square in range(3):
#     snake = Turtle(shape="square")
#     snake.penup()
#     snake.color("white")
#     snake.goto(x=x_cor, y=0)
#     x_cor -= 20
#     snake_body.append(snake)

# Using Snake Class
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Animating / Moving the snake body
game_is_on = True


while game_is_on:
    screen.update()  # update the screen once all the segments have moved forward
    time.sleep(0.1)
    # for body in snake_body:
    #     body.forward(10)

    # for body_num in range(len(snake_body) - 1, 0, -1):  # going from last body square to first
    #     new_x = snake_body[body_num - 1].xcor()
    #     new_y = snake_body[body_num - 1].ycor()
    #     snake_body[body_num].goto(new_x, new_y)
    #
    # snake_body[0].forward(20)
    # snake_body[0].left(90)
    snake.move()

    # Detect collision with food
    if snake.snake_body[0].distance(food) < 15:  # the food is 10 * 10 pixels
        # print("collided!")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].xcor() < -280 or \
            snake.snake_body[0].ycor() < -280:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    # if head collides with any segment in the tail:
    sliced_list = snake.snake_body[1:]
    for segment in sliced_list:
        # if segment == snake.snake_body[0]:
        #     pass
        # elif snake.snake_body[0].distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()

        # By using slicing:
        if snake.snake_body[0].distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()
screen.exitonclick()