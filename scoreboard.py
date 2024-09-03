# scoreboard.py
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        with open("data.txt") as hs_data:
            self.high_score = int(hs_data.read())
        # self.write(f"Score: {self.score}", move=False, align="center", font=("Courier New", 20, "normal"))
        self.update_score()

    def update_score(self):
        self.clear()
        # self.score += 1 # creating this as a separate method
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False, align="center", font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
    #

    # New methods for recording high score & restarting the game!
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_data:  # writing to file so that high score saved when code re-run.
                new_data.write(str(self.score))
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()