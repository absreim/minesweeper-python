from controller import GameState, Controller


def test_victory():
    game = Controller(3,3,2)
    board = game.board
    for row_num in range(len(board)):
        for col_num in range(len(board[row_num])):
            cell = board[row_num][col_num]
            if not cell.is_mine:
                game.reveal_cell(row_num, col_num)
    assert game.state == GameState.WON


def test_defeat():
    game = Controller(5,4,10)
    board = game.board
    for row_num in range(len(board)):
        mine_found = False
        for col_num in range(len(board[row_num])):
            cell = board[row_num][col_num]
            if cell.is_mine:
                game.reveal_cell(row_num, col_num)
                mine_found = True
                break
        if mine_found:
            break
    assert game.state == GameState.LOST
