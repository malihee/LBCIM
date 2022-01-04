class Player:
    def __init__(self, color, token_number, turn, approach):
        self.color = color
        self.token_number = token_number
        self.turn_ = turn  # boolean type
        self.approach_ = approach

    def player_score(self, graph_position):
        global score
        return score

    def give_token(self):
        self.tokennumber = -1
        return

    @property
    def tokennumber(self):
        return self.token_number

    @tokennumber.setter
    def tokennumber(self, val):
        if self.tokennumber > 0:
            self.token_number -= val
        else:
            print('this player tokens are finished')
        return self.token_number

    @property
    def turn(self):
        return self.turn_

    @turn.setter
    def turn(self, turn):
        self.turn_ = turn

    @property
    def approach(self):
        return self.approach_

    @approach.setter
    def approach(self, type):
        self.approach_ = type
# each player can choose the heuristics he wanna use
