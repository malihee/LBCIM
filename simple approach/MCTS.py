from mcts_rewrite import mcts
from graph import Graph
import setting as set


class State:

    def __init__(self, graph, curr_player, red_player_token, black_player_token):
        self.graph = graph
        self.curr_player = curr_player
        self.black_player_token = black_player_token
        self.red_player_token = red_player_token

    def getPossibleActions(self):

        if set.type_of_game == 'full_loyalty_more_token' or set.type_of_game == 'harder_reactivation':
            # print('1')
            if set.flmt_strategy == 'naive' or set.hra_strategy == 'naive':
                # print('18')
                global flag
                # print('20')
                flag = False
                # print('22')
                if self.curr_player == 'black':
                    # print('2')
                    possibleActions = []
                    next_position, token_capacity = self.graph.next_position_of_graph(self.curr_player, self.black_player_token)
                    # print('3')
                    for idx, pos in enumerate(next_position):
                        if self.black_player_token >= token_capacity[idx]:
                            possibleActions.append(Action(player=self.curr_player, graph=pos, rtoken=self.red_player_token,
                                                          btoken=self.black_player_token, token_capacity=token_capacity[idx]))
                            # print('4')
                    if len(possibleActions) == 0 and self.black_player_token > 0:
                        flag = True
                        next_position, token_capacity = self.graph.next_position_of_graph(self.curr_player, self.black_player_token)
                        for idx, pos in enumerate(next_position):
                            possibleActions.append(Action(player=self.curr_player, graph=pos, rtoken=self.red_player_token,
                                                          btoken=self.black_player_token,
                                                          token_capacity=token_capacity[idx]))
                    if len(possibleActions) == 0:
                         possibleActions.append(Action(player=self.curr_player, graph=self.graph, rtoken=self.red_player_token,
                                                       btoken=self.black_player_token+1, token_capacity=0))

                elif self.curr_player == 'red':
                    # print('45')
                    possibleActions = []
                    next_position, token_capacity = self.graph.next_position_of_graph(self.curr_player, self.red_player_token)
                    # print('48')
                    for idx, pos in enumerate(next_position):
                        if self.red_player_token >= token_capacity[idx]:
                            possibleActions.append(Action(player=self.curr_player, graph=pos, rtoken=self.red_player_token,
                                                          btoken=self.black_player_token, token_capacity=token_capacity[idx]))
                            # print('50')

                    if len(possibleActions) == 0 and self.red_player_token > 0:
                        flag = True
                        # set.type_of_game = 'full_loyalty_variant'
                        # return self.getPossibleActions()
                        next_position, token_capacity = self.graph.next_position_of_graph(self.curr_player, self.red_player_token)
                        for idx, pos in enumerate(next_position):
                            possibleActions.append(Action(player=self.curr_player, graph=pos, rtoken=self.red_player_token,
                                                          btoken=self.black_player_token,
                                                          token_capacity=token_capacity[idx]))
                    if len(possibleActions) == 0:
                        possibleActions.append(Action(player=self.curr_player, graph=self.graph, rtoken=self.red_player_token+1,
                                                      btoken=self.black_player_token, token_capacity=0))
            elif set.flmt_strategy == 'advanced':
                if self.curr_player == 'black':
                    possibleActions = []
                    next_position, token_capacity = self.graph.next_position_of_graph(self.curr_player,
                                                                                      self.black_player_token)
                    for idx, pos in enumerate(next_position):
                        if self.black_player_token >= token_capacity[idx]:
                            possibleActions.append(
                                Action(player=self.curr_player, graph=pos, rtoken=self.red_player_token,
                                       btoken=self.black_player_token, token_capacity=token_capacity[idx]))
                    if len(possibleActions) == 0:
                        possibleActions.append(
                            Action(player=self.curr_player, graph=self.graph, rtoken=self.red_player_token,
                                   btoken=self.black_player_token + 1, token_capacity=0))

                elif self.curr_player == 'red':
                    possibleActions = []
                    next_position, token_capacity = self.graph.next_position_of_graph(self.curr_player,
                                                                                      self.red_player_token)
                    for idx, pos in enumerate(next_position):
                        if self.red_player_token >= token_capacity[idx]:
                            possibleActions.append(
                                Action(player=self.curr_player, graph=pos, rtoken=self.red_player_token,
                                       btoken=self.black_player_token, token_capacity=token_capacity[idx]))
                    if len(possibleActions) == 0:
                        possibleActions.append(
                            Action(player=self.curr_player, graph=self.graph, rtoken=self.red_player_token + 1,
                                   btoken=self.black_player_token, token_capacity=0))

        else:
            possibleActions = []
            if self.curr_player == 'red':
                next_position = self.graph.next_position_of_graph(self.curr_player, self.red_player_token)
            elif self.curr_player == 'black':
                next_position = self.graph.next_position_of_graph(self.curr_player, self.black_player_token)
            for pos in next_position:
                possibleActions.append(Action(player=self.curr_player, graph=pos, rtoken=self.red_player_token,
                                              btoken=self.black_player_token, token_capacity=1))

        return possibleActions

    def takeAction(self, action):

        if set.type_of_game == 'full_loyalty_more_token' or set.type_of_game == 'harder_reactivation':
            if action.player == 'black':  # and action.b_token - action.token_capacity > 0:
                return State(graph=action.graph, curr_player='red', red_player_token=action.r_token,
                             black_player_token=action.b_token - action.token_capacity)

            elif action.player == 'red':  # and action.r_token - action.token_capacity > 0:
                return State(graph=action.graph, curr_player='black',
                             red_player_token=action.r_token-action.token_capacity, black_player_token=action.b_token)
        else:
            if action.player == 'black':
                return State(graph=action.graph, curr_player='red', red_player_token=action.r_token,
                             black_player_token=action.b_token-1)

            elif action.player == 'red':
                return State(graph=action.graph, curr_player='black', red_player_token=action.r_token-1,
                             black_player_token=action.b_token)

    def isTerminal(self):

        if set.type_of_game == 'full_loyalty_variant':
            black_nodes, red_nodes, inactive_nodes = self.graph.nodes_state()
            if (self.red_player_token == 0 and self.black_player_token == 0) or black_nodes+red_nodes == self.graph.node_number():
                return True
            else:
                return False
        elif set.type_of_game == 'zero_loyalty_variant':
            if (self.red_player_token == 0 and self.black_player_token == 0) or self.graph.is_in_exploding_loop:
                return True
            else:
                return False
        if set.type_of_game == 'different_loyalty_variant':
            black_nodes, red_nodes, inactive_nodes = self.graph.nodes_state()
            if (self.red_player_token == 0 and self.black_player_token == 0) or black_nodes+red_nodes == self.graph.node_number():
                return True
            else:
                return False

        if set.type_of_game == 'full_loyalty_more_token' or set.type_of_game == 'harder_reactivation':
            black_nodes, red_nodes, inactive_nodes = self.graph.nodes_state()
            if (self.red_player_token == 0 and self.black_player_token == 0) or black_nodes + red_nodes == self.graph.node_number():
                return True
            else:
                return False

    def getReward(self):

        if set.type_of_game == 'full_loyalty_variant':
            if self.isTerminal():
                red_nodes, black_nodes, deactive_nodes = self.graph.nodes_state()
                if set.current_player.color == 'red':
                    return red_nodes - black_nodes
                elif set.current_player.color == 'black':
                    return black_nodes - red_nodes
            else:
                return False
        elif set.type_of_game == 'zero_loyalty_variant':
            if self.isTerminal():
                red, black = self.graph.token_num_in_graph()
                if set.current_player.color == 'red':
                    return red - black
                elif set.current_player.color == 'black':
                    return black - red
            else:
                return False
        elif set.type_of_game == 'different_loyalty_variant':
            if self.isTerminal():
                red_nodes, black_nodes, deactive_nodes = self.graph.nodes_state()
                if set.current_player.color == 'red':
                    return red_nodes - black_nodes
                elif set.current_player.color == 'black':
                    return black_nodes - red_nodes
            else:
                return False

        elif set.type_of_game == 'full_loyalty_more_token' or set.type_of_game == 'harder_reactivation':
            if self.isTerminal():
                red_nodes, black_nodes, deactive_nodes = self.graph.nodes_state()
                if set.current_player.color == 'red':
                    return red_nodes - black_nodes
                elif set.current_player.color == 'black':
                    return black_nodes - red_nodes
            else:
                return False


class Action:
    def __init__(self, player, graph, rtoken, btoken, token_capacity):
        self.player = player
        self.graph = graph
        self.r_token = rtoken
        self.b_token = btoken
        self.token_capacity = token_capacity

    # def __str__(self):
    #     return str((self.x, self.y))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.graph == other.graph and self.player == other.player

    def __hash__(self):
        return hash((self.player, self.graph))

