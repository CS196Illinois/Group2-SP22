import Board
import random
from queue import Queue

class Piece():
    def __init__(self, n_grid):
        self.n_grid = n_grid
        piece_queue = Queue()
        i_piece = Piece([
            [0, 15, 0, 0],
            [0, 15, 0, 0],
            [0, 15, 0, 0],
            [0, 15, 0, 0]])
        t_piece = Piece([
            [0, 3, 0, 0],
            [3, 3, 3, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]])
        z_piece = Piece([
            [5, 5, 0, 0],
            [0, 5, 5, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]])
        s_piece = Piece([
            [0, 7, 7, 0],
            [7, 7, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]])
        j_piece = Piece([
            [0, 9, 0, 0],
            [0, 9, 0, 0],
            [9, 9, 0, 0],
            [0, 0, 0, 0]])
        o_piece = Piece([
            [0, 0, 0, 0],
            [0, 11, 11, 0],
            [0, 11, 11, 0],
            [0, 0, 0, 0]])
        l_piece = Piece([
            [13, 0, 0, 0],
            [13, 13, 13, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]])
        all_pieces = [t_piece, i_piece, z_piece,
                        s_piece, j_piece, o_piece, l_piece]


    def add_to_queue(self):
        for i in range(0,100):
            y = random.randint(0, 6)
            self.piece_queue.put(self.all_pieces[y])

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

    def move_down(self, board, piece, coords):
        x, y = coords
        if Board.hit(board, piece, (x, y-1)) == False:
            return (x+1, y)
        else:
            return (x, y)

    def push_down(self, board, piece, coords):
        x, y = coords
        for i in range(15):
            if Board.hit(board, piece, (x + i, y)) == True:
                return (x+(i-1), y)
