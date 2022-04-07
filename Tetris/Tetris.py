# from dataclasses import dataclass
import queue
# from typing_extensions import Self
import random
import pygame
import Piece
import Board

queue = []
i_piece = Piece([
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0]])
t_piece = Piece([
    [0, 3, 0, 0],
    [3, 3, 3, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])
z_piece = Piece([
    [5, 5, 0, 0],
    [0, 5, 5, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])
s_piece = Piece([
    [0, 7, 7, 0],
    [7, 7, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])
j_piece = Piece([
    [0, 9, 0, 0],
    [0, 9, 0, 0],
    [9, 9, 0, 0],
    [0, 0, 0, 0]
])
o_piece = Piece([
    [0, 0, 0, 0],
    [0, 11, 11, 0],
    [0, 11, 11, 0],
    [0, 0, 0, 0]
])
l_piece = Piece([
    [13, 0, 0, 0],
    [13, 13, 13, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])


def gameStart():
    y = random.randint(0, 6)
    all_pieces = [t_piece, i_piece, z_piece,
                  s_piece, j_piece, o_piece, l_piece]
    queue.append(all_pieces[y])


scores = 0

# try to read highest record from saved file,jump over this step if fail


# save scores as a file if it's higher than the record


count = 0
fps = 25
gameOn = True


# Game Loop
while gameOn:
    # adds pieces to queue
    # Moving Pieces Down, can add level system very easy
    if (count % (fps // Board.level) == 0):
        if board.gameStart:
            piece.push_down
    count += 1

    # Inputs will be controlled using some sofware, I assume pygame
    if pygame.event.type == pygame.KEYDOWN:
        if pygame.event.key == pygame.K_UP:
            Piece.rot_cw
        if pygame.event.key == pygame.K_DOWN:
            Piece.push_down
        if pygame.event.key == pygame.K_LEFT:
            Piece.move_left
        if pygame.event.key == pygame.K_RIGHT:
            Piece.move_right
        if pygame.event.key == pygame.K_SPACE:
            gameOn = False
        if pygame.event.key == pygame.K_ESCAPE:
            piece_queue = 0  # piece that is pulled from queue, increases when piece is placed later
            for i in range(200):  # appends 200 pieces to queue when escape is hit(initialized)
                gameStart()

    Placed = False
    # when a piece is added to board, make true
    while Placed:
        piece_queue += 1
        Board.add_to_board(Board, queue[piece_queue], (0, 12))

    # default coordinates for where pieces drop--row 22 to 23 -- Evan
    # do default coordinates change based on piece? what is the default position for each piece? -- Evan

    # start dropping pieces -- Joseph
    # use second iteration of board that updates with moving pieces -- Joseph
    # falls, controlled w/ inputs-- Joseph
    # pushdown function -- anyone with extra time??
    # hit floor, get added to board -- devon
    # delay between blocks hitting & being added to permanent board (not being able to control piece anymore) -- devon
    # lines clear, added to score --Qi Chen
    # function that tests if/how many lines have been cleared--Qi Chen
    # gameover -- Qi Chen
    # have game over function by start dropping peices, checks if top lines has enough space for piece
