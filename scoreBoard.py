from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../OneDrive\Desktop\score_file.txt") as score_file:
            self.highest_score = int(score_file.read())
        self.penup()
        self.pencolor("white")
        self.goto(0, 270)
        self.write_score()
        self.hideturtle()

    def write_score(self):
        self.write(f"Score: {self.score}   Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over! Final Score: {self.score} \nHighest Score: {self.high_score}", align=ALIGNMENT,
    #     font=FONT)

    def reset(self):
        if self.highest_score < self.score:
            self.highest_score = self.score
            with open("../../OneDrive\Desktop\score_file.txt", mode="w") as file:
                x = str(self.highest_score)
                file.write(x)
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.update()
