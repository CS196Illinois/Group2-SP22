
from Board import Board
import random
from queue import Queue


class Piece():
    i_piece = ([
        [0, 15, 0, 0],
        [0, 15, 0, 0],
        [0, 15, 0, 0],
        [0, 15, 0, 0]])
    t_piece = ([
        [0, 3, 0, 0],
        [3, 3, 3, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]])
    z_piece = ([
        [5, 5, 0, 0],
        [0, 5, 5, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]])
    s_piece = ([
        [0, 7, 7, 0],
        [7, 7, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]])
    j_piece = ([
        [0, 9, 0, 0],
        [0, 9, 0, 0],
        [9, 9, 0, 0],
        [0, 0, 0, 0]])
    o_piece = ([
        [11, 11, 0, 0],
        [11, 11, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]])
    l_piece = ([
        [13, 0, 0, 0],
        [13, 13, 13, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]])
    all_pieces = [t_piece, i_piece, z_piece,
                  s_piece, j_piece, o_piece, l_piece]

    piece_queue = Queue(maxsize=100)

    def add_to_queue(self):
        for i in range(0, 100):
            y = random.randint(0, 6)
            Piece.piece_queue.put(self.all_pieces[y])

    def rot_ccw(self):  # rotate couterclockwise
        rotpiece = [[0 for n in range(4)] for m in range(4)]
        for m in range(0, 4):
            for n in range(0, 4):
                rotpiece[m][n] = self[n][3 - m]
        return rotpiece

    def rot_cw(self):  # rotate clockwise
        rotpiece = [[0 for n in range(4)] for m in range(4)]
        for m in range(0, 4):
            for n in range(0, 4):
                rotpiece[m][n] = self[3 - n][m]
        return rotpiece

    def move_right(self, board, coords):
        x, y = coords
        if Board.hit(self, (x, y+1)) == False:
            return (x, y+1)
        else:
            return (x, y)

    def move_left(self, board, coords):
        x, y = coords
        if Board.hit(self, (x, y-1)) == False:
            return (x, y-1)
        else:
            return (x, y)

    def move_down(self, board, coords):
        x, y = coords
        if Board.hit(self, (x, y-1)) == False:
            return (x+1, y)
        else:
            return (x, y)

    def push_down(self, board, coords):
        x, y = coords
        for i in range(20):
            if Board.hit(self, (x + i, y)):
                return (x+(i-1), y)
