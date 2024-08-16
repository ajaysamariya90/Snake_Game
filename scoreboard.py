from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.color("White")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align="center", font=("Arial", 25, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")

        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Arial", 25, "normal"))

    def increment(self):
        self.score += 1
        self.update_score()
