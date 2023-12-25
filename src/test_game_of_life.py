from unittest import TestCase

from src.game_of_life import GameOfLife


class TestGameOfLife(TestCase):

    def test_get_dead_neighbors(self):
        game = GameOfLife()
        game.grid = [
            [False, False, False],
            [False, True, False],
            [False, False, False],
        ]

        dead_neighbors = game.get_dead_neighbors(1, 1)
        print(len(dead_neighbors))

        assert len(dead_neighbors) is 8

    def test_get_dead_neighbors_2(self):
        game = GameOfLife()
        game.grid = [
            [True, True, False],
            [True, False, False],
            [False, False, False],
        ]

        dead_neighbors = game.get_dead_neighbors(0, 1)
        print(len(dead_neighbors))
        print(game.available_neighbors(0, 1))

        assert len(dead_neighbors) is 7

    def test_get_dead_neighbors_3(self):
        game = GameOfLife()
        game.grid = [
            [True, True, True],
            [True, True, True],
            [True, True, True],
        ]

        dead_neighbors = game.get_dead_neighbors(1, 1)
        print(len(dead_neighbors))

        assert len(dead_neighbors) is 0

