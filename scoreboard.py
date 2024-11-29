from turtle import Turtle, Screen
from prettytable import PrettyTable

POINTS_PER_FOOD = 1
FONT_SCORE = ('Arial', 15, 'normal')
FONT_HIGHSCORE = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.score = 0
        self.screen = screen
        self.game_is_on = True
        self.highscore = []
        lines = []
        with open("high_score.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name_line = line.split(": ")[0]
                score_line = int(line.split(": ")[1])
                self.highscore.append([name_line, score_line])
        self.hideturtle()
        y = screen.window_height()/2 - 50
        self.setposition(x=-50, y=y)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Punkte = {self.score}", font=FONT_SCORE)
    def add_points(self):
        self.score += POINTS_PER_FOOD
        self.clear()
        self.update_scoreboard()

    def game_ends(self):
        self.game_is_on = False
        self.new_highscore()

    def new_highscore(self):
        user_name = self.screen.textinput(prompt="What is your name?", title="Enter name")
        if len(self.highscore) < 4 or self.score > int(self.highscore[-1][1]):
            self.highscore.append([user_name, self.score])
        self.highscore.sort(key=lambda x: x[1], reverse=True)
        table = PrettyTable()
        table.field_names = ["Name", "Punkte"]
        entries_to_display = 3 if len(self.highscore) > 3 else len(self.highscore)
        with open("high_score.txt", "w") as file:
            for entry in range(entries_to_display):
                print(entry)
                table.add_row([self.highscore[entry][0], self.highscore[entry][1]])
                file.write(self.highscore[entry][0] + ": ")
                file.write(str(self.highscore[entry][1]) + "\n")
        turtle = Turtle()
        turtle .pencolor("white")
        table.align = "r"
        turtle .write(arg=table.get_string(border=False), font=FONT_HIGHSCORE)

