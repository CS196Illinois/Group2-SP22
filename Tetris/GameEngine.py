from Board import Board
from Piece import Piece
import pygame

class GameEngine():
    def up_key(board, piece, coords):
        board.remove_from_board(piece, coords)
        piece.rot_cw(board.list2d, coords)
        board.add_to_board(piece, coords)

    def down_key(board, piece, coords):
        board.remove_from_board(piece, coords)
        coords = piece.push_down(board.list2d, coords)
        board.add_to_board(piece, coords)
    
    def left_key(board, piece, coords):
        board.remove_from_board(piece, coords)
        coords = piece.move_left(board.list2d, coords)
        board.add_to_board(piece, coords)

    def right_key(board, piece, coords):
        board.remove_from_board(piece, coords)
        coords = piece.move_right(board.list2d, coords)
        board.add_to_board(piece, coords)

    def move_down(board, piece, coords):
        x,y = coords
        coords = (x + 1, y) # moves coordinates down 1
        board.remove_from_board(piece, (x, y))
        board.add_to_board(piece, coords)

