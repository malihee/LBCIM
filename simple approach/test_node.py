import heuristics as hs
import setting as set


class Node:
    def __init__(self, data, level, player, red_player_token, black_player_token):
        self.data = data
        self.level = level
        self.player = player
        self.red_player_token = red_player_token
        self.black_player_token = black_player_token


