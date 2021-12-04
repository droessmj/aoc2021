class BingoBoard:
    board = []
    winning_number_sets = []
    all_numbers_set = set()

    def __init__(self, board):
        self.board = board

        for val_row in board:
            row_set = set()
            # row values as a set
            for entry in val_row:
                self.all_numbers_set.add(entry)
                row_set.add(entry)
            self.winning_number_sets.append(row_set)

        # calc column value as a set
        for col in range(len(board)):
            col_set = { board[0][col], board[1][col], board[2][col], board[3][col], board[4][col] }
            self.winning_number_sets.append(col_set)
    
    def __str__(self):
        return f"{self.board}\n"

    def __repr__(self) -> str:
        return f"{self.board}\n"

all_called_numbers = []
all_bingo_boards = []
with open("./test.txt") as f:
    all_called_numbers = [int(i) for i in f.readline().split(",")]
    f.readline()

    # build boards
    idx = 0
    board_lines = []
    for line in f:
        # pass on empty lines
        if len(line) < 3:
            continue

        #append line as row to board being built
        board_lines.append([int(n) for n in line.strip().split(' ') if n != ''])
        idx += 1

        if idx > 4:
            all_bingo_boards.append(BingoBoard(board_lines))
            idx = 0
            board_lines = []
            

print(all_bingo_boards)
