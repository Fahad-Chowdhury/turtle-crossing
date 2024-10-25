import time
from game_screen import GameScreen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


def collision_detected(player: Player, car_manager: CarManager):
    """ Detect turtle collision with any of the cars. Return True if
    there is a collision with any of the cars, else False. """
    for car in car_manager.cars:
        if car.distance(player) < 20:
            return True
    return False


def main():
    """ Main method for the Turtle crossing game.  """
    game_is_on = True
    screen = GameScreen()
    player = Player()
    car_manager = CarManager()
    score_board = ScoreBoard()
    screen.listen_to_keys(key="Up", fun=player.go_up)

    while game_is_on:

        screen.update_screen()
        car_manager.create_car()
        car_manager.move_cars()

        # Detect turtle collision with a car.
        if collision_detected(player, car_manager):
            score_board.display_game_over()
            game_is_on = False

        # Detect Successful turtle crossing.
        if player.is_at_finnish_line():
            player.go_to_start()
            car_manager.level_up()
            score_board.increase_level()

    screen.exit_screen_on_click()


if __name__ == "__main__":
    main()
