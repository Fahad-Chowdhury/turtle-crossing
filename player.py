from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self._create_turtle()

    def _create_turtle(self):
        """ Create the turtle. """
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """ Move turtle up by MOVE_DISTANCE co-ordinates. """
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """ Move turtle to the start, STARTING_POSITION co-ordinates. """
        self.goto(STARTING_POSITION)

    def is_at_finnish_line(self):
        """ Checks if the turtle reached the finish line,
        i.e. FINISH_LINE_Y co-ordinates. """
        return self.ycor() > FINISH_LINE_Y
