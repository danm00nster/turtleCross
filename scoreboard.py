from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-290,270)
        self.write(f"level:  {self.level}",font=FONT)

    def increase_level(self):
       self.level+=1
       self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"level:  {self.level}", font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER ! Twój level to:  {self.level}", align="center",font=FONT)

