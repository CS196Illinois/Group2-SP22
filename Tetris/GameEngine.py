import Board
import Piece
import pygame

pygame.init()
count = 0
fps = 25
gameOn = False
piece = []
board = []

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
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Piece.rot_cw
            if event.key == pygame.K_DOWN:
                Piece.push_down
            if event.key == pygame.K_LEFT:
                Piece.move_left
            if event.key == pygame.K_RIGHT:
                Piece.move_right
            if event.key == pygame.K_SPACE:
                gameOn = False
    if (count % (fps // Board.Board.level) == 0):
        if gameOnfr:
            Piece.move_down
    #Board.Board()
    #Piece.Piece()
    
 