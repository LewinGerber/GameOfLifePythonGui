import copy
from typing import List


class Position:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col


class GameOfLife:
    grid = [
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False]
    ]

    def start(self):
        self.grid[1][2] = True
        self.grid[1][3] = True
        self.grid[1][4] = True

    def evaluate_grid(self):
        dead_neighbors = []
        new_grid = copy.deepcopy(self.grid)

        for row_index in range(len(self.grid)):
            for col_index in range(len(self.grid[row_index])):
                if self.grid[row_index][col_index]:
                    dead_neighbors_of_cell = self.get_dead_neighbors(row_index, col_index)
                    alive_neighbors = self.available_neighbors(row_index, col_index) - len(dead_neighbors_of_cell)

                    print(
                        f"{row_index}, {col_index} => Found alive {alive_neighbors} ({len(dead_neighbors_of_cell)} dead) resolution: ")

                    if alive_neighbors < 2 or alive_neighbors > 3:
                        print("died")
                        new_grid[row_index][col_index] = False
                    else:
                        print("lived")

                    for neighbor in dead_neighbors_of_cell:
                        dead_neighbors.append(neighbor)

        for neighbor in dead_neighbors:
            dead_neighbors_of_cell = self.get_dead_neighbors(neighbor.row, neighbor.col)
            alive_neighbors = self.available_neighbors(neighbor.row, neighbor.col) - len(dead_neighbors_of_cell)
            if alive_neighbors == 3:
                new_grid[neighbor.row][neighbor.col] = True

        self.grid = new_grid

    def available_neighbors(self, row, col) -> int:
        total = 8

        if row == 0:
            total -= 3
        if col == 0:
            total -= 2
        if col == len(self.grid[0]) - 1:
            total -= 2
        if row == len(self.grid) - 1:
            total -= 3

        return total

    def get_dead_neighbors(self, row, col) -> List[Position]:
        dead_neighbors = []
        upper_row = row - 1
        left_hand = col - 1
        right_hand = col + 1
        lower_row = row + 1

        if not upper_row < 0:
            if not self.grid[upper_row][col]:
                dead_neighbors.append(Position(upper_row, col))

        if not upper_row < 0 and not left_hand < 0:
            if not self.grid[upper_row][left_hand]:
                dead_neighbors.append(Position(upper_row, left_hand))

        if not upper_row < 0 and not right_hand > len(self.grid[0]) - 1:
            if not self.grid[upper_row][right_hand]:
                dead_neighbors.append(Position(upper_row, right_hand))

        if not lower_row > len(self.grid) - 1:
            if not self.grid[lower_row][col]:
                dead_neighbors.append(Position(lower_row, col))

        if not lower_row > len(self.grid) - 1 and not left_hand < 0:
            if not self.grid[lower_row][left_hand]:
                dead_neighbors.append(Position(lower_row, left_hand))

        if not lower_row > len(self.grid) - 1 and not right_hand > len(self.grid[0]) - 1:
            if not self.grid[lower_row][right_hand]:
                dead_neighbors.append(Position(lower_row, right_hand))

        if not left_hand < 0:
            if not self.grid[row][left_hand]:
                dead_neighbors.append(Position(row, left_hand))

        if not right_hand > len(self.grid[0]) - 1:
            if not self.grid[row][right_hand]:
                dead_neighbors.append(Position(row, right_hand))

        return dead_neighbors

    def get_alive_position(self):
        alive_positions = []
        for row_index in range(len(self.grid)):
            for col_index in range(len(self.grid[row_index])):
                if self.grid[row_index][col_index]:
                    alive_positions.append(Position(row_index, col_index))
        return alive_positions
