import time
import tkinter as tk


class GameOfLife:
    window = tk.Tk()
    window.title("Game of Life")
    window.geometry("800x800")
    canvas = tk.Canvas(window, bg="black", width=800, height=800, highlightthickness=0)
    canvas.pack()

    counter = 0

    def show_loading_animation(self):
        while True:
            self.tick()
            time.sleep(1)
            self.window.update_idletasks()

    def draw_square(self):
        self.canvas.create_rectangle(0, 0, 8, 8, fill="white")

    def start_window_loop(self):
        self.window.update_idletasks()
        self.window.mainloop()

    def tick(self):
        print("ticking")
        if self.counter == 1 or self.counter == 2 or self.counter == 3:
            self.draw_square_at_position(1, 1)
            self.counter += 1
        if self.counter == 2 or self.counter == 3:
            self.draw_square_at_position(2, 1)
            self.counter += 1
        if self.counter == 3:
            self.draw_square_at_position(3, 1)
            self.counter += 1
        if self.counter == 3:
            self.canvas.delete("all")
            self.counter = 0

    def draw_square_at_position(self, x_hundred_based: int, y_hundred_based: int):
        start_x = x_hundred_based * 8
        start_y = y_hundred_based * 8
        self.canvas.create_rectangle(start_x, start_y, start_x + 8, start_y + 8, fill="white")


if __name__ == "__main__":
    game = GameOfLife()
    game.show_loading_animation()
    game.start_window_loop()

