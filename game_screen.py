from turtle import Screen
import time

class GameScreen:

    def __init__(self):
        self.screen = Screen()
        self._setup_screen()

    def _setup_screen(self):
        """ Setup screen. """
        self.screen.setup(width=600, height=600)
        self.screen.title("Turtle Crosssing")
        self.screen.tracer(0)
        self.screen.listen()

    def update_screen(self):
        """ Update the screen. """
        time.sleep(0.1)
        self.screen.update()

    def listen_to_keys(self, key, fun):
        """ Map keyboard stroke to  move. """
        self.screen.onkey(key=key, fun=fun)

    def exit_screen_on_click(self):
        """ Close screen on mouseclick. """
        self.screen.exitonclick()
