from Board import Board
from Piece import Piece
import pygame

pygame.init()
count = 0
fps = 25
gameOn = False
Placed = True
piece = []
board = []
init = True
coords = (0, 6)

#Moving Pieces Down, can add level system later on by increasing fps

display = pygame.display.set_mode((300, 300))
pygame.display.set_caption('idk what im doing')
while gameOn == False:
    for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameOn = True

gameOnfr = False
while gameOn == True:
    if init: #initializes board
        Board()
        Piece()
        Piece.add_to_queue(Piece)
        init = False
        piece = Piece.piece_queue.get()
        board = Board.add_to_board(board, piece, (0,6))
        coords = (1,6)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                piece = Piece.rot_cw(board, piece, coords)
                board = Board.add_to_board(board, piece, coords)
            if event.key == pygame.K_DOWN:
                coords = Piece.push_down(board, piece, coords)
                board = Board.add_to_board(board, piece, coords)
            if event.key == pygame.K_LEFT:
                coords = Piece.move_left(board, piece, coords)
                board = Board.add_to_board(board, piece, coords)
            if event.key == pygame.K_RIGHT:
                coords = Piece.move_right(board, piece, coords)
                board = Board.add_to_board(board, piece, coords)
            if event.key == pygame.K_SPACE:
                gameOn = False
                init = True
    if (count % (fps // Board.level) == 0):
        if gameOn:
            board = Board.remove_from_board(Board, board, piece, coords)
            coords = Piece.move_down(Piece, board, piece, coords)
            board = Board.add_to_board(Board, board, piece, coords)
            print(*board, sep="\n")

    if Placed: #if the piece before was placed 'officially' on the board, this will name a new piece and place it on the board
        Placed = False
        coords = (0,6)
        piece = Piece.piece_queue.get()
        board = Board.add_to_board(board, piece, coords)

    
 