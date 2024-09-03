# snake.py
from turtle import Turtle

# Using constants make it convenient for if you want to start with different values.
MOVE_DISTANCE = 20
STARTING_SNAKE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # tuples of starting positions
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:
    def __init__(self):
        # Creating the Snake Body
        self.snake_body = []
        for position in STARTING_SNAKE_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_body.append(snake)

    def extend(self):  # to be used once snake eats food to extend length.
        # Add a new segment to the snake.
        self.add_segment(self.snake_body[-1].position())  # using the last position of the segment to add another.

    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):  # going from last body square to first
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_body[0].heading() != DOWN:  # to avoid it going back on itself
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    # function to reinitialize the snake
    def reset(self):
        for segment in self.snake_body:  # making previous snake disappear by taking it off-screen.
            segment.goto(1000,1000)
        self.snake_body.clear()  # .clear() clears all items/segments in the list.
        for position in STARTING_SNAKE_POSITIONS:
            self.add_segment(position)