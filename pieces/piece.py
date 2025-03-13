class Piece:
    def __init__(self, color, row, col):
        self.color = color  # "w" for white, "b" for black
        self.row = row
        self.col = col

    def valid_moves(self, board):
        return []
