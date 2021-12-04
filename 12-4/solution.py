class BingoBoard:
    board = []
    winning_number_sets = []
    all_numbers_set = set()

    def __init__(self, board):
        self.board = board
        self.winning_number_sets = []
        self.all_numbers_set = set()

        for val_row in self.board:
            row_set = set()
            # row values as a set
            for entry in val_row:
                self.all_numbers_set.add(entry)
                row_set.add(entry)
            self.winning_number_sets.append(row_set)

        # calc column value as a set
        for col in range(len(self.board)):
            col_set = { self.board[0][col], self.board[1][col], self.board[2][col], self.board[3][col], self.board[4][col] }
            self.winning_number_sets.append(col_set)
    
    def __str__(self):
        return f"{self.board}\n"

    def __repr__(self) -> str:
        return f"{self.board}\n"

    def check_for_winner(self, called_numbers):
        if len(self.all_numbers_set.intersection(set(called_numbers))) < 5:
            return False
        else:
            for s in self.winning_number_sets:
                matches_count = len(s.intersection(set(called_numbers)))
                if matches_count == 5:
                    return True
            return False
    
    def calc_score(self, called_numbers):
        marked = self.all_numbers_set.intersection(set(called_numbers))
        sum_unmarked = sum(list(self.all_numbers_set.difference(marked)))
        return sum_unmarked * called_numbers[-1]

def callNumber_returnIsWinner(called_numbers, all_bingo_boards):
    # take the called number, check all boards for state
    # if a winner is detected calc the return value
    if len(called_numbers) < 5:
        return False

    result_list = []
    for board in all_bingo_boards:
        if board.check_for_winner(called_numbers):
            result_list.append(board)
    
    if result_list:
        return result_list
    else:
        # return result as False or winning value
        return False


all_num_to_call = []
all_bingo_boards = []
with open("./input.txt") as f:
    all_num_to_call = [int(i) for i in f.readline().split(",")]
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
            bb = BingoBoard(board_lines)
            all_bingo_boards.append(bb)
            idx = 0
            board_lines = []

print(f"All Bingo boards: {len(all_bingo_boards)}")
call_idx = 0 
called_numbers = []
last_board = None
while len(all_bingo_boards) > 0:
    if (call_idx == 99):
        print(f"Remaining boards: {len(all_bingo_boards)}")

    called_numbers.append(all_num_to_call[call_idx])
    result_board_list = callNumber_returnIsWinner(called_numbers, all_bingo_boards)
    if result_board_list: 
        for board in result_board_list:
            all_bingo_boards.remove(board)
            last_board = board

    call_idx += 1

print(last_board.calc_score(called_numbers))

### part 1 solved