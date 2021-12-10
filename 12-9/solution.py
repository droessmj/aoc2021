import sys
from functools import reduce

lookup = {}

# return True if smaller than above/below
def check_col_smallest(board,r,c, board_len, row_len):
    if c == 0:  # can't check above
        return board[r][c] < board[r][c+1]
    elif c == row_len - 1: # can't check below
        return board[r][c] < board[r][c-1]
    else: # top and bottom can be checked
        return board[r][c] < board[r][c-1] and board[r][c] < board[r][c+1]

# return True if smaller than left, right
def check_row_smallest(board,r,c, board_len, row_len):
    if r == 0:  # can't check left
        return board[r][c] < board[r+1][c]
    elif r == board_len - 1: # can't check right
        return board[r][c] < board[r-1][c]
    else: # left and right can be checked
        return board[r][c] < board[r-1][c] and board[r][c] < board[r+1][c]

# return True if smaller than above/below
def get_non_nine_neighbors(board,r,c, board_len, row_len):
    possible_neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
    if r == 0: # skip check above
        possible_neighbors.remove([-1,0])
    if r == board_len -1: #skip check below
        possible_neighbors.remove([1,0])
    if c == 0: # skip check left
        possible_neighbors.remove([0,-1])
    if c == row_len -1: #skip check right
        possible_neighbors.remove([0,1])

    viable_neighbors = []
    for neighbor in possible_neighbors: #TODO add a lookup table 
        if board[r+neighbor[0]][c+neighbor[1]] != 9 and str(r+neighbor[0])+str(c+neighbor[1]) not in lookup:
            viable_neighbors.append([r+neighbor[0],c+neighbor[1]])
            lookup[str(r+neighbor[0])+str(c+neighbor[1])] = True
    print(viable_neighbors)
    return viable_neighbors

def calc_basin_size(board,r,c,board_len,row_len):
    basin_size = 1
    # look to all four locations, add value to check if exists and not 9
    viable_neighbors = get_non_nine_neighbors(board,r,c,board_len,row_len)
    idx = 0
    while idx < len(viable_neighbors):
        basin_size += 1
        viable_neighbors += get_non_nine_neighbors(board,viable_neighbors[idx][0],viable_neighbors[idx][1],board_len,row_len)
        idx += 1
    print( basin_size )
    return basin_size

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
basin_points = []
while r < board_len:
    c = 0
    while c < row_len:
        if check_row_smallest(board,r,c,board_len,row_len) and check_col_smallest(board,r,c,board_len,row_len):
            risk += 1 + int(board[r][c])
            basin_points.append([r,c])
        c += 1
    r +=1 

basin_sizes = []
for point in basin_points:
    # check if adjacent points are in basin 
    basin_size = calc_basin_size(board,point[0], point[1],board_len,row_len)
    basin_sizes.append(basin_size)

basin_sizes.sort()
print(basin_sizes)
largest_3 = basin_sizes[3::-1]

print(reduce(lambda a, b: a * b, largest_3))