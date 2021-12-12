import sys

def cascade(board,r,c, col_len, row_len):
    count = 0
    if r-1 > -1 and c-1 > -1 and board[r-1][c-1] != 0:  # diagonal left above
        board[r-1][c-1] += 1
        if board[r-1][c-1] > 9:
            board[r-1][c-1] = 0
            count += 1
            count += cascade(board,r-1,c-1, col_len, row_len)

    if c-1 > -1 and board[r][c-1] != 0: # col left of r,c
        board[r][c-1] += 1
        if board[r][c-1] > 9:
            board[r][c-1] = 0
            count += 1
            count += cascade(board,r,c-1, col_len, row_len)

    if r+1 < row_len and c-1 > -1 and board[r+1][c-1] != 0: # diagonal left lower
        board[r+1][c-1] += 1
        if board[r+1][c-1] > 9:
            board[r+1][c-1] = 0
            count += 1
            count += cascade(board,r+1,c-1, col_len, row_len)

    if r-1 > -1 and board[r-1][c] != 0: # above 
        board[r-1][c] += 1
        if board[r-1][c] > 9:
            board[r-1][c] = 0
            count += 1
            count += cascade(board,r-1,c, col_len, row_len)

    if r+1 < row_len and board[r+1][c] != 0: # below
        board[r+1][c] += 1
        if board[r+1][c] > 9:
            board[r+1][c] = 0
            count += 1
            count += cascade(board,r+1,c, col_len, row_len)

    if r-1 > -1 and c+1 < col_len and board[r-1][c+1] != 0:  # diagonal right above
        board[r-1][c+1] += 1
        if board[r-1][c+1] > 9:
            board[r-1][c+1] = 0
            count += 1 
            count += cascade(board,r-1,c+1, col_len, row_len)

    if c+1 < col_len and board[r][c+1] != 0: # straight right
        board[r][c+1] += 1
        if board[r][c+1] > 9:
            board[r][c+1] = 0
            count += 1
            count += cascade(board,r,c+1, col_len, row_len)

    if r+1 < row_len and c+1 < col_len and board[r+1][c+1] != 0:  # diagonal right lower
        board[r+1][c+1] += 1
        if board[r+1][c+1] > 9:
            board[r+1][c+1] = 0
            count += 1
            count += cascade(board,r+1,c+1, col_len, row_len)

    return count

def process_day(board, col_len, row_len):
    count = 0

    # increment all numbers
    for r,row in enumerate(board):
        for c,col in enumerate(row):
            board[r][c] += 1

    # handle 9's cascading
    for r,row in enumerate(board):
        for c,col in enumerate(row):
            if board[r][c] > 9:
                board[r][c] = 0
                count += 1
                count += cascade(board,r,c, col_len, row_len)

    return count

in_file = 'test2'
days_to_process = 3

if len(sys.argv) > 1:
    in_file = sys.argv[1]

if len(sys.argv) > 2:
    days_to_process = int(sys.argv[2])

board = []
with open(f"./{in_file}.txt") as f:
    for line in f:
        row = []
        line = line.strip()
        for c in line:
            row.append(int(c))
        board.append(row)

cur_day = 0
count = 0
col_len = len(board)
row_len = len(board[0])

while cur_day < days_to_process:
    count += process_day(board, col_len, row_len)
    cur_day += 1

    printstr=''
    for row in board:
        for col in row:
            printstr+=str(col)
        printstr+='\n'
    print(printstr)

print(count)