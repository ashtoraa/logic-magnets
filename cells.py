class Square:
    def __init__(self, row, col, square_type):
        self.row = row
        self.col = col
        self.square_type = square_type

    def __str__(self):
        return self.square_type


def _str_(self) -> str:
 if self.type== "normal":
    return '⬛️'
 elif self.type == "positive":
    return '🟥'
 elif self.type == "Negative":
    return '🟦'
 elif self.type =="white":
     return '⬜️'
 else:
     return '🟪'
 
