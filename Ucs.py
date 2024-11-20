import queue  

class IronPiece:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"IronPiece({self.x}, {self.y})"

class Magnet:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color  

    def move_iron_piece(self, iron_piece):
        if self.color == 'red':
            return self.pull(iron_piece)
        elif self.color == 'blue':
            return self.push(iron_piece)
    
    def pull(self, iron_piece):
        dx = iron_piece.x - self.x
        dy = iron_piece.y - self.y
        if abs(dx) > abs(dy):
            iron_piece.x -= 1 if dx > 0 else -1
        else:
            iron_piece.y -= 1 if dy > 0 else -1
        return iron_piece
    
    def push(self, iron_piece):
        dx = iron_piece.x - self.x
        dy = iron_piece.y - self.y
        if abs(dx) > abs(dy):
            iron_piece.x += 1 if dx > 0 else -1
        else:
            iron_piece.y += 1 if dy > 0 else -1
        return iron_piece


class Square:
    def __init__(self, row, col, square_type):
        self.row = row
        self.col = col
        self.square_type = square_type

    def __str__(self):
        return self.square_type

    def _str_(self) -> str:
        if self.square_type == "magnet":
            return '⬛️'
        elif self.square_type == "positive":
            return '🟥'
        elif self.square_type == "negative":
            return '🟦'
        elif self.square_type == "white":
            return '⬜️'
        else:
            return 'empty'


class GameState:
    def __init__(self, iron_pieces, magnets, cost=0, board=None):
        self.iron_pieces = iron_pieces  
        self.magnets = magnets  
        self.cost = cost  
        self.board = board  

    def __repr__(self):
        return f"GameState({self.iron_pieces}, {self.cost})"

    def get_next_states(self):
        next_states = []
        for magnet in self.magnets:
            for iron_piece in self.iron_pieces:
                new_iron_piece = IronPiece(iron_piece.x, iron_piece.y)
                new_iron_piece = magnet.move_iron_piece(new_iron_piece)
                new_state = GameState(
                    [new_iron_piece if ip == iron_piece else ip for ip in self.iron_pieces],
                    self.magnets,
                    cost=self.cost + 1,
                    board=self.board
                )
                next_states.append(new_state)
        return next_states

    def is_goal_state(self, goal_state):
        return all(self.board[ip.x][ip.y].square_type == "white" for ip in self.iron_pieces)

    def __lt__(self, other):
        return self.cost < other.cost  

    def print_board(self):
        board_rep = [['⬜️' for _ in range(len(self.board[0]))] for _ in range(len(self.board))]
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                square = self.board[row][col]
                board_rep[row][col] = square._str_()  

        
        for row in board_rep:
            print(' '.join(row))


class UCS:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def search(self):
        waiting = queue.PriorityQueue()  
        waiting.put((self.start_state.cost, self.start_state))  
        explored = set()

        while not waiting.empty():
            current_cost, current_state = waiting.get()  

            if current_state.is_goal_state(self.goal_state):
                return current_state

    
            explored.add(tuple((ip.x, ip.y) for ip in current_state.iron_pieces))  

            for next_state in current_state.get_next_states():
                
                next_state_tuple = tuple((ip.x, ip.y) for ip in next_state.iron_pieces)

                if next_state_tuple not in explored:
                    waiting.put((next_state.cost, next_state)) 
                    print(f"Current State Cost: {next_state.cost}")
                    next_state.print_board() 

        return None  


def create_game(map_number):
    if map_number == "1":
        stones = [[2, 0, "negative"], [1, 2, "iron piece"]]
        homes = [[1, 1], [1, 3]]
        size = 4
    elif map_number == "2":
        stones = [[4, 0, "negative"], [1, 2, "iron piece"], [2, 1, "iron piece"], [2, 3, "iron piece"], [3, 2, "iron piece"]]
        homes = [[0, 2], [2, 0], [2, 2], [2, 4], [4, 2]]
        size = 5
    elif map_number == "3":
        stones = [[2, 0, "negative"], [1, 2, "iron piece"]]
        homes = [[0, 3], [2, 3]]
        size = 4
    elif map_number == "4":
        stones = [[2, 0, "negative"], [1, 1, "iron piece"]]
        homes = [[1, 0], [1, 2]]
        size = 3
    else:
        raise ValueError("Invalid map number")

    board = [[Square(r, c, "empty") for c in range(size)] for r in range(size)]
    iron_pieces = []
    magnets = []

    for stone in stones:
        if stone[2] == "negative":
            board[stone[0]][stone[1]] = Square(stone[0], stone[1], "negative")
        elif stone[2] == "iron piece":
            iron_pieces.append(IronPiece(stone[0], stone[1]))
            board[stone[0]][stone[1]] = Square(stone[0], stone[1], "iron piece")
    for home in homes:
        magnets.append(Magnet(home[0], home[1], "red" if home[1] % 2 == 0 else "blue"))
        board[home[0]][home[1]] = Square(home[0], home[1], "magnet")

    return iron_pieces, magnets, board

map_number = input("Enter map number (1, 2, 3, 4): ")
iron_pieces, magnets, board = create_game(map_number)
start_state = GameState(iron_pieces, magnets, board=board)
goal_state = GameState(
    [],
    magnets,  
    board=board
)

ucs = UCS(start_state, goal_state)
solution = ucs.search()

if solution:
    print(f"SUCCESSFUL: {solution}")
    solution.print_board()
else:
    print("FAILED")
