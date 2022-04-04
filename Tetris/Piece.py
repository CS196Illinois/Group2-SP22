import Board


class Piece():
    def __init__(self, n_grid, n_color):
        self.n_grid = n_grid
        self.n_color = n_color

    def rot_ccw(self, piece):  # rotate couterclockwise
        rotpiece = [[0 for n in range(4)] for m in range(4)]
        for m in range(0, 4):
            for n in range(0, 4):
                rotpiece[m][n] = piece[n][3 - m]
        return rotpiece

    def rot_cw(self, piece):  # rotate clockwise
        rotpiece = [[0 for n in range(4)] for m in range(4)]
        for m in range(0, 4):
            for n in range(0, 4):
                rotpiece[m][n] = piece[3 - n][m]
        return rotpiece

    def move_right(self, board, piece, coords):
        x, y = coords
        if Board.hit(board, piece, (x, y+1)) == False:
            return (x, y+1)
        else:
            return (x, y)

    def move_left(self, board, piece, coords):
        x, y = coords
        if Board.hit(board, piece, (x, y-1)) == False:
            return (x, y-1)
        else:
            return (x, y)

    def push_down(self, board, piece, coords):
        x, y = coords
        for i in range(15):
            if Board.hit(board, piece, (x + i, y)) == True:
                return (x+(i-1), y)
