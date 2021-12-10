import sys

# return True if smaller than above/below
def check_col(board,r,c, board_len, row_len):
    if c == 0:  # can't check above
        return board[r][c] < board[r][c+1]
    elif c == row_len - 1: # can't check below
        return board[r][c] < board[r][c-1]
    else: # top and bottom can be checked
        return board[r][c] < board[r][c-1] and board[r][c] < board[r][c+1]

# return True if smaller than left, right
def check_row(board,r,c, board_len, row_len):
    if r == 0:  # can't check left
        return board[r][c] < board[r+1][c]
    elif r == board_len - 1: # can't check right
        return board[r][c] < board[r-1][c]
    else: # left and right can be checked
        return board[r][c] < board[r-1][c] and board[r][c] < board[r+1][c]

in_file = 'test'

if len(sys.argv) > 1:
    in_file = sys.argv[1]

board = []
with open(f"./{in_file}.txt") as f:
    for line in f:
        row = []
        line = line.strip()
        for c in line:
            row.append(c)
        board.append(row)

risk = 0
board_len = len(board)
row_len = len(board[0])

r = 0
while r < board_len:
    c = 0
    while c < row_len:
        if check_row(board,r,c,board_len,row_len) and check_col(board,r,c,board_len,row_len):
            risk += 1 + int(board[r][c])
        c += 1
    r +=1 

print(risk)