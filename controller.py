from enum import Enum
from random import randrange


class GameState(Enum):
    PLAYING = 0
    WON = 1
    LOST = 2


class Cell:
    def __init__(self):
        self.is_revealed = False
        self.is_marked = False
        self.is_mine = False


class Controller:
    def __init__(self, width, height, num_mines):
        # Board cell is tuple (is_revealed, is_marked, is_mine)
        self.board = [
            [Cell() for _ in range(width)]
            for _ in range(height)
        ]
        mine_locs = self._randomize_mine_locs(num_mines, width*height)
        for index in mine_locs:
            row = index // width
            col = index % width
            self.board[row][col].is_mine = True
        self.num_mines = num_mines
        self.num_empty_cells = width * height - num_mines
        self.num_revealed = 0
        self.state = GameState.PLAYING

    @staticmethod
    def _randomize_mine_locs(num_mines, num_cells):
        # Randomly place mines using Fisher-Yates algo.
        # Shortcut by placing all mines at the right and then
        # iterating through those cells only.
        is_mine_list = [not x < num_cells - num_mines for x in range(num_cells)]
        for i in range(num_cells - num_mines, num_cells):
            swap_index = randrange(0, i)
            is_mine_list[i] = is_mine_list[swap_index]
            is_mine_list[swap_index] = True
        mine_locs = []
        for i in range(len(is_mine_list)):
            if is_mine_list[i]:
                mine_locs.append(i)
        return mine_locs

    def toggle_mark(self, row, column):
        self.board[row][column] = not self.board[row][column]

    def reveal_cell(self, row, column):
        cell = self.board[row][column]
        if not cell.is_revealed:
            self.num_revealed += 1
            cell.is_revealed = True
        if self.state == GameState.PLAYING:
            if cell.is_mine:
                self.state = GameState.LOST
            elif self.num_revealed == self.num_empty_cells:
                self.state = GameState.WON
