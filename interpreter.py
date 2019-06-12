# Text-based command interpreter for the game

import argparse

from controller import Controller, GameState

parser = argparse.ArgumentParser()
parser.add_argument('rows', 'Number of rows in the game board')
parser.add_argument('cols', 'Number of columns in the game board')
parser.add_argument('mines', 'Number of mines')
args = parser.parse_args()

cols = args.cols
rows = args.rows
mines = args.mines

controller = Controller(cols, rows, mines)
print(f'Initialized game with {rows} rows, {cols} columns, and {mines} mines.')


def print_board(board):
    num_cols = len(board[0])
    vertical_border = ''.join(['-' for _ in range(num_cols)])
    print(vertical_border)
    for row in board:
        row_str_list = ['|']
        for cell in row:
            if cell.is_revealed:
                if cell.is_mine:
                    row_str_list.append('*')
                else:
                    row_str_list.append('O')
            else:
                if cell.is_marked:
                    row_str_list.append('!')
                else:
                    row_str_list.append('?')
            row_str_list.append('|')
        print(''.join(row_str_list))
    print(vertical_border)


def print_revealed_board(board):
    num_cols = len(board[0])
    vertical_border = ''.join(['-' for _ in range(num_cols)])
    print(vertical_border)
    for row in board:
        row_str_list = ['|']
        for cell in row:
            if cell.is_mine:
                row_str_list.append('*')
            else:
                row_str_list.append('O')
            row_str_list.append('|')
        print(''.join(row_str_list))
    print(vertical_border)


board = controller.board
exiting = False
while not exiting:
    input_line = input('Please enter your command: ')
    tokens = input_line.split(' ')
    if tokens[0] == 'show':
        if controller.state == GameState.PLAYING:
            print('The game is still in progress.')
            print_board(board)
        elif controller.state == GameState.LOST:
            print('The game is over, you have lost.')
            print_revealed_board(board)
        elif controller.state == GameState.WON:
            print('The game is over, you have won.')
            print_revealed_board(board)
        print('Showing state of the game board:')