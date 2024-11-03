
from ast import main
import random
from cells import Square

class Game:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = self.build_random_board()

    def build_random_board(self):
        colors = ['🟪', '⬜️', '🟦', '🟥','⬛️']
        board = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(self.cols):
                square_type = random.choice(colors)
                board[i][j] = Square(i, j, square_type)

        return board

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
    def move_piece(self, x, y, direction):
        if direction == "up" and x > 0 and self.board[x-1][y].square_type == '⬜️':
            self.board[x-1][y].square_type, self.board[x][y].square_type = self.board[x][y].square_type, '⬜️'
        elif direction == "down" and x < self.rows - 1 and self.board[x+1][y].square_type == '⬜️':
            self.board[x+1][y].square_type, self.board[x][y].square_type = self.board[x][y].square_type, '⬜️'
        elif direction == "left" and y > 0 and self.board[x][y-1].square_type == '⬜️':
            self.board[x][y-1].square_type, self.board[x][y].square_type = self.board[x][y].square_type, '⬜️'
        elif direction == "right" and y < self.cols - 1 and self.board[x][y+1].square_type == '⬜️':
            self.board[x][y+1].square_type, self.board[x][y].square_type = self.board[x][y].square_type, '⬜️'

    def move_pieces_and_store(self):
        while True:
            self.print_board()
            key = input("Enter move (up, down, left, right) or 'q' to quit: ").strip().lower()
            if key == 'q':
                break

            x, y = self.find_movable_piece()
            if x is not None and y is not None:
                self.move_piece(x, y, key)

            board_copy = [row[:] for row in self.board]
            self.board_history.append(board_copy)
            self.print_board()


    def find_movable_piece(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j].square_type in ['🟥', '🟦']:
                    return (i, j)
        return (None, None)
    
def main():
      rows = int(input("Enter the number of rows: "))
      cols = int(input("Enter the number of columns: "))
      game_view = Game(rows, cols)
      print(game_view)
      if game_view.check_win():
        print("Congratulations! You've won the game.")
      else:
        print("Keep playing! Number of empty squares:", game_view.count_empty_squares())

      if __name__ == '__main__':
        main()
