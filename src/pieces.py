#imports
import board

class Piece(): #default to pawn
    def __init__(self, y, x, colour, symbol):
        self.y = y
        self.x = x
        self.colour = colour
        self.symbol = symbol

    def diagonals(self, board):
        diagonals = set()
        for diagonal in [(-1,1),(1,1),(1,-1),(-1,-1)]:
            y, x = self.y + diagonal[0], self.x + diagonal[1]
            while is_in_bounds(y, x) and board.board[y][x] == '.':
                diagonals.add((y, x))
                y += diagonal[0]
                x += diagonal[1]
            if is_in_bounds(y, x):
                #obstacle
                obstacle = get_piece(board.pieces, y, x)
                if obstacle.colour != self.colour:
                    diagonals.add((y, x))

        return diagonals

    def straights(self, board):
        straights = set()
        for straight in [(0,1),(1,0),(0,-1),(-1,0)]:
            y, x = self.y + straight[0], self.x + straight[1]
            while is_in_bounds(y, x) and board.board[y][x] == '.':
                straights.add((y, x))
                y += straight[0]
                x += straight[1]
            if is_in_bounds(y, x):
                #obstacle
                obstacle = get_piece(board.pieces, y, x)
                if obstacle.colour != self.colour:
                    straights.add((y, x))

        return straights



class Pawn(Piece):
    def __init__(self, y, x, colour):
        super().__init__(y, x, colour, "P")

    def legal_moves(self, board):
        moves = set()
        #check forwards
        y = self.y
        x = self.x
        if is_in_bounds(y-1, x) and board.board[y-1][x] == '.':
            moves.add((y-1, x))

        if y == 6 and is_in_bounds(y-2, x) and board.board[y-2][x] == '.':
            moves.add((y-2, x))

        #check diagonals
        l = get_piece(board.pieces, y-1, x-1)
        r = get_piece(board.pieces, y-1, x+1)

        if l:
            if l.colour != self.colour:
                moves.add((y-1, x-1))

        if r:
            if r.colour != self.colour:
                moves.add((y-1, x+1))

        return moves

    def promote(symbol):
        pass


class Rook(Piece):
    def __init__(self, y, x, colour):
        super().__init__(y, x, colour, "R")

    def legal_moves(self, board):
        return self.straights(board)

class Knight(Piece):
    def __init__(self, y, x, colour):
        super().__init__(y, x, colour, "N")

    def legal_moves(self, board):
        pass

class Bishop(Piece):
    def __init__(self, y, x, colour):
        super().__init__(y, x, colour, "B")

    def legal_moves(self, board):
        return self.diagonals(board)

class Queen(Piece):
    def __init__(self, y, x, colour):
        super().__init__(y, x, colour, "Q")

    def legal_moves(self, board):
        return self.diagonals(board) | self.straights(board)

class King(Piece):
    def __init__(self, y, x, colour):
        super().__init__(y, x, colour, "K")

    def legal_moves(self, board):
        pass

    def check(self, board):
        '''
        no moves can put the king in check
        '''
        check = False
        king_pos = (self.y, self.x)

        for piece in board.pieces: #get other colour
            if piece.colour != self.colour:
                if king_pos in piece.legal_moves(board):
                    check = True
        return check

def is_in_bounds(y, x):
    return (8 > x and x >= 0) and (8 > y and y >= 0)

def get_piece(pieces, y, x):
    for piece in pieces:
        if piece.x == x and piece.y == y:
            return piece
    return None
