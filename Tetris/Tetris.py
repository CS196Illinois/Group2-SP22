# from dataclasses import dataclass
import queue
# from typing_extensions import Self
import random
import pygame
from Piece import Piece
from Board import Board
from GameEngine import GameEngine

gameOn = False
pygame.init()
# initializes a display for pygame
display = pygame.display.set_mode((300, 300))
pygame.display.set_caption('')
while gameOn == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameOn = True

# Game Loop
count = 0
fps = 25
Pieces = Piece()
Pieces.add_to_queue()
score = 0
piece = Pieces.piece_queue.get()
board = Board()
board.add_to_board(piece, (0, 6))
coords = (0, 6)
Placed = False
gameengine = GameEngine()
while gameOn:
    # inputs
    for event in pygame.event.get():
        if event.type() == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gameengine.up_key(board, piece, coords)
                board.sprint()
            if event.key == pygame.K_DOWN:
                gameengine.down_key(board, piece, coords)
                board.sprint()
            if event.key == pygame.K_LEFT:
                gameengine.left_key(board, piece, coords)
                board.sprint()
            if event.key == pygame.K_RIGHT:
                gameengine.right_key(board, piece, coords)
                board.sprint()
            if event.key == pygame.K_SPACE:  # terminate game midway
                board.sprint()
                gameOn = False

    if (count % fps == 0):
        # checks that moving down won't hit the board, if it doesnt, moves it down
        x, y = coords
        if not board.hit(piece, coords, (x+1, y)):
            print(coords)
            gameengine.move_down(board, piece, coords)
            board.sprint()
            print()
            print(coords)
            coords = (x+1, y)
        else:  # if it will hit the board by moving down, keeps where it is and starts placed sequence for new piece
            Placed = True
            print("can't move down")
            board.sprint()
            print()

    if Placed:  # if the piece before was placed 'officially' on the board, this will name a new piece and place it on the top of board
        Placed = False
        # Gameover if cannot fit piece at top of board
        if board.hitWithOutOld(piece, (0, 6)):
            gameOn = False
        else:
            coords = (0, 6)
            piece = Piece.piece_queue.get()
            board.add_to_board(board, piece, coords)
            if board.piece_queue.qsize < 5:  # if the queue starts to run out of pieces,
                Piece.add_to_queue()  # adds 100 more pieces

    count += 1
