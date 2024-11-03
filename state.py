from cells import Square


class State:
    def __init__(self, rows, cols, board):
        self.rows = rows
        self.cols = cols
        self.board = board

    def __str__(self):
        result = ""
        for row in self.board:
            for square in row:
                result += str(square)
            result += '\n'
        return result
    
    def count_empty_squares(self):
        empty_count = sum(row.count('⬜️') for row in self.board)
        return empty_count

    def check_win(self):
        empty_squares = self.count_empty_squares()
        if empty_squares == 0:
            return True
        return False

    def __str__(self):
        result = ""
        for row in self.board:
            for square in row:
                result += str(square)
            result += '\n'
        return result

def main():
    init_board = [
        ['🟪', '🟪', '🟪'],
        ['🟪', '🟪', '🟪'],
        ['🟪', '🟪', '🟪'],
        ['🟪', '🟪', '🟪']
    ]
    rows = len(init_board)
    cols = len(init_board[0])

    board = [[None for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            square_type = '🟪'
            board[i][j] = Square(i, j, square_type)

    new_state = State(rows, cols, board)
    print(new_state)

if __name__ == '__main__':
    main()
