
from dataclasses import dataclass
from queue import queue
from typing_extensions import Self
from random import random

class Piece ():
    def __init__(self, n_rows[][], n_cols, color) :
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.color = color
    # include rotate functions, etec

def startGame():
    queue = queue()
    y = 7 * random()
    i_piece = Piece(1, 4, "blue")
    t_piece = Piece(2, 3, "yellow")
    z_piece = Piece()
    s_piece = Piece()
    j_piece = Piece()
    o_piece = Piece()
    l_piece = Piece()
    all_pieces = [t_piece, i_piece, z_piece, s_piece, j_piece, o_piece, l_piece]
    queue.append(all_pieces[y])

