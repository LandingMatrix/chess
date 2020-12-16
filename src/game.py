#imports
from player import Player
import board
import pieces

class Game():
    def __init__(self, players=[]): #log can load/save games
        self.players = players

    def start(self):
        self.board = board.Board()
        self.board.set_pieces()
        self.board.update_board()
        #randomise players

    def load(self, log):
        for move in log:
            pass
            #make_move(move)


if __name__ == '__main__':
    game = Game()

    player1 = Player(id=len(game.players))
    player1.join(game)

    player2 = Player(id=len(game.players))
    player2.join(game)

    game.start()


    game.board.print_board()

    print()
    game.board.flip()
    game.board.print_board()
