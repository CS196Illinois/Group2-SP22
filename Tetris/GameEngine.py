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

# Moving Pieces Down, can add level system later on by increasing fps

display = pygame.display.set_mode((300, 300))
pygame.display.set_caption('idk what im doing')
while gameOn == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameOn = True

print(*board, sep="\n")
while gameOn:
    if init:  # initializes board & pieces/queue
        board = Board()  # idk if this works
        Piece.add_to_queue(Piece)
        init = False
        piece = Piece.piece_queue.get()
        board = Board.add_to_board(board, piece, (0, 6))
        coords = (1, 6)
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                board.remove_from_board(piece, coords)
                piece.rot_cw(board, coords)
                board.add_to_board(piece, coords)
            if event.key == pygame.K_DOWN:
                board.remove_from_board(piece, coords)
                coords = piece.push_down(board, coords)
                board.add_to_board(piece, coords)
                Placed = True
            if event.key == pygame.K_LEFT:
                board.remove_from_board(piece, coords)
                coords = piece.move_left(board, coords)
                board.add_to_board(piece, coords)
            if event.key == pygame.K_RIGHT:
                board.remove_from_board(piece, coords)
                coords = piece.move_right(board, coords)
                board.add_to_board(piece, coords)
            if event.key == pygame.K_SPACE:
                gameOn = False
                init = True
    if (count % (fps // Board.level) == 0):
        print(*board, sep="\n")
        if gameOn:
            coords = Piece.move_down(piece, coords)
            x, y = coords
            if not Board.hit(piece, coords):
                board.remove_from_board(piece, (x - 1, y))
                board.add_to_board(piece, coords)
            else:
                Placed = True
                board.add_to_board(piece, coords)

    if Placed:  # if the piece before was placed 'officially' on the board, this will name a new piece and place it on the board
        Placed = False
        if Board.hit(piece, (0, 6)):  # Gameover
            gameOn = False
        else:
            coords = (0, 6)
            piece = Piece.piece_queue.get()
            board = Board.add_to_board(board, piece, coords)

    if Board.piece_queue.qsize < 5:  # if the queue starts to run out of pieces,
        Piece.add_to_queue(Piece)  # adds 100 more pieces
