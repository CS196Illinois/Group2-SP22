class Board:
    level = 1

    gameStart = False

    def __init__(self):
        height = 20
        width = 10
        border = 2
        board = [[0 for n in range(width + border * 2)] for m in range(height + border)]
        for i in range(width + border * 2):
            for j in range(height + border):
                if i not in range(border, width + border) or j not in range(0, height):
                    board[j][i] = 1
        print(*board, sep="\n")

    def add_to_board(self, board, piece, coords):
        x, y = coords
        board_temp = [[0 for n in range(14)] for m in range(22)]
        for m in range(0, 20):
            for n in range(2, 12):
                board_temp[m][n] = board[m][n]
        for m in range(x, x+4):
            for n in range(y, y+4):
                board_temp[m][n] = board[m][n] + piece[m - x][n - y]
        return board_temp

    def hit(self, board, piece, coords):
        board_temp = self.add_to_board(board.copy(), piece, coords)
        for m in range(self.height + self.border):
            for n in range(self.wdith + self.border):
                if board_temp[m][n] % 2 != 0:
                    return True
        return False

    def lineClear(self):  # check if a horizontal line is fullfilled and delete it, and add scores. --Qi Chen
        for i in self.board:
            if i == [1 for n in range(16)]:
                scores += 1  # replace '1' by the specific marks.
                for m in range(1, self.board.index(i)):
                    self.board[m] = self.board[m-1]
