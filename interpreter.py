# Text-based command interpreter for the game

import argparse

from controller import Controller, GameState

parser = argparse.ArgumentParser()
parser.add_argument('rows', help = 'Number of rows in the game board',
                    type=int)
parser.add_argument('cols', help = 'Number of columns in the game board',
                    type=int)
parser.add_argument('mines', help = 'Number of mines', type=int)
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
                    row_str_list.append(str(cell.num_adj_mines))
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
                row_str_list.append('#')
            row_str_list.append('|')
        print(''.join(row_str_list))
    print(vertical_border)


def print_legend():
    legend_text = '''
    * - cell revealed to be mine
    # - cell revealed to be empty, at end of game
    ! - marked cell, not revealed
    ? - unmarked cell, not revealed
    While the game is still in progress, revealed empty cells are displayed
    with an integer indicating the number of adjacent mines.
    '''
    print(legend_text)


def print_help():
    help_text = '''
    help - print this help message
    show - print out the game board and game state
    legend - print out the legend of game board symbols
    mark {row} {col} - toggle marking for the cell at the specified row and col
    reveal {row} {col} - reveal the cell at the specified row and col
    exit - exit the program
    '''
    print(help_text)


board = controller.board
exiting = False
while not exiting:
    input_line = input('Please enter your command: ')
    tokens = input_line.split(' ')
    if tokens[0] == 'show':
        print('Showing state of the game board:')
        if controller.state == GameState.PLAYING:
            print('The game is still in progress.')
            print_board(board)
        elif controller.state == GameState.LOST:
            print('The game is over, you have lost.')
            print_revealed_board(board)
        elif controller.state == GameState.WON:
            print('The game is over, you have won.')
            print_revealed_board(board)
    elif tokens[0] == 'reveal':
        if len(tokens) >= 3:
            row = int(tokens[1])
            col = int(tokens[2])
            controller.reveal_cell(row, col)
        else:
            print('Both row and col must be specified.')
    elif tokens[0] == 'mark':
        if len(tokens) >= 3:
            row = int(tokens[1])
            col = int(tokens[2])
            controller.toggle_mark(row, col)
        else:
            print('Both row and col must be specified.')
    elif tokens[0] == 'legend':
        print_legend()
    elif tokens[0] == 'exit':
        exiting = True
    else:
        print_help()
