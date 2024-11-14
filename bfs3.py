from collections import defaultdict, deque

class Square:
    def __init__(self, square_type):
        self.square_type = square_type

class GameBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[Square('⬜️') for _ in range(cols)] for _ in range(rows)]
    
    def setup_board(self):
        self.board[0][0].square_type = '⬜️'
        self.board[0][1].square_type = '🟥'
        self.board[0][2].square_type = '⬛️'
        
        self.board[1][0].square_type = '⬛️'
        self.board[1][1].square_type = '🟦'
        self.board[1][2].square_type = '⬜️'
    
    def find_possible_moves(self, x, y):
        possible_moves = []
        if x > 0 and self.board[x-1][y].square_type not in {'⬛️', '⬛️',}:
            possible_moves.append((x-1, y))
        if x < self.rows - 1 and self.board[x+1][y].square_type not in {'⬛️', '⬛️'}:
            possible_moves.append((x+1, y))
        if y > 0 and self.board[x][y-1].square_type not in {'⬛️', '⬛️'}:
            possible_moves.append((x, y-1))
        if y < self.cols - 1 and self.board[x][y+1].square_type not in {'⬛️', '⬛️'}:
            possible_moves.append((x, y+1))
        return possible_moves

    def print_board(self):
        for row in self.board:
            print(" ".join(square.square_type for square in row))

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s, board):
        visited = {s}
        queue = deque([s])
        path = []

        while queue:
            x, y = queue.popleft()
            path.append((x, y))
            print((x, y), end=" ")

            if board[x][y].square_type in {'🟥', '🟦'}:
                board[x][y].square_type = '⬜️'

            for neighbor in self.graph[(x, y)]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print()
        print("Path taken:", path)
        print()

game_board = GameBoard(2, 3)
game_board.setup_board()

print("Initial Game Board:")
game_board.print_board()

g = Graph()
x, y = 0, 0

for i in range(game_board.rows):
    for j in range(game_board.cols):
        for move in game_board.find_possible_moves(i, j):
            g.addEdge((i, j), move)

print("\nBFS Path:")
g.BFS((x, y), game_board.board)

print("\nUpdated Game Board:")
game_board.print_board()
