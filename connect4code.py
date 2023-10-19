import numpy as np
ROW_COUNT=6
COL_COUNT=7
def create_board():
    board=np.zeros((6,7))
    return board

def drop_piece(board,row,col,piece):
    board[row][col]=piece
def is_valid_location(board,col):
    return board[5][col]==0 #if the fifth row is still 0,you can drop the piece

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r
def print_board(board):
    print(np.flip(board,0))
c4 = create_board()
print(c4)
game_over=False
turn=0
while not game_over:
    if turn%2==0:
        col=int(input("Player1: enter your selection [0-6]"))
        if is_valid_location(c4,col):
            row=get_next_open_row(c4,col)
            drop_piece(c4,row,col,1)
    else:
        col = int(input("Player2: enter your selection [0-6]"))
        if is_valid_location(c4,col):
            row=get_next_open_row(c4,col)
            drop_piece(c4,row,col,2)
    print_board(c4)
    turn=turn+1

