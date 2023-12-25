import time

from gui import GUI
from game_of_life import GameOfLife

has_just_started = True

def tick():
    game.evaluate_grid()
    gui.set_alive_positions(game.get_alive_position())


gui = GUI()

game = GameOfLife()

game.start()
gui.set_alive_positions(game.get_alive_position())

gui.on_tick(tick)
gui.enter_main_loop()
