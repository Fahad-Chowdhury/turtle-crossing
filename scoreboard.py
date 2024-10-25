from turtle import Turtle


FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self._display_level()

    def _display_level(self):
        """ Update the scoreboard. """
        self.clear()
        msg = f"Level: {self.level}"
        self.write(msg, move=False, align="left", font=FONT)

    def increase_level(self):
        """ Increase the level and update level on screen. """
        self.level += 1
        self._display_level()

    def display_game_over(self):
        """ Display game over message at the center of the screen. """
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)
