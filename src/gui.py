import tkinter as tk

from typing import List

from game_of_life import Position


class GUI:
    window = tk.Tk()
    window.title("Game of Life")
    window.geometry("200x200")
    canvas = tk.Canvas(window, bg="black", width=200, height=200, highlightthickness=0)
    canvas.pack()

    alive_positions = []

    def on_tick(self, tick):
        tick()
        self.draw()

        self.window.after(3000, lambda: self.on_tick(tick))

    def set_alive_positions(self, positions: List[Position]):
        self.alive_positions = positions

    def enter_main_loop(self):
        self.canvas.update_idletasks()
        self.window.mainloop()

    def draw(self):
        self.canvas.delete('all')
        print(self.alive_positions)
        for position in self.alive_positions:
            self.draw_square_at_position(position.row, position.col)

    def draw_square_at_position(self, row: int, col: int):
        row_y = row * 20
        col_x = col * 20
        self.canvas.create_rectangle(col_x, row_y, col_x + 20, row_y + 20, fill="white")