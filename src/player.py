#imports

class Player():
    def __init__(self, id):
        self.id = id

    def join(self, game):
        game.players.append(self)

    def resign(self, game):
        pass

    def offer_draw(self, game):
        pass

    def make_move(self):
        pass

    def select_piece(self):
        pass
