from dataclasses import dataclass
from queue import queue
from typing_extensions import Self
from random import random


class Piece ():
    def __init__(self, n_grid, n_color):
        self.n_grid = n_grid
        self.n_color = n_color
    # include rotate functions, etc

def startGame():
    queue = queue()
    y = 7 * random()
    i_piece = Piece([
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0]]
    , "blue")
    t_piece = Piece([
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ], "yellow")
    z_piece = Piece([
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], "red")
    s_piece = Piece([
        [0, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ], "orange")
    j_piece = Piece([
        [0, 1, 0, 0],
        [0, 1, 0, 0], 
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ], "green")
    o_piece = Piece([
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ], "purple")
    l_piece = Piece([
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ], "pink")
    all_pieces = [t_piece, i_piece, z_piece, s_piece, j_piece, o_piece, l_piece]
    queue.append(all_pieces[y])

