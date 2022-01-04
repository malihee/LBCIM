from player import Player
import setting as set
from test_tree import make_tree
import heuristics as hs
import random
import msvcrt as msv
from mcts_rewrite import mcts as MCTS
from MCTS import State, Action
import numpy as np

num_of_black_winning = 0
num_of_red_winning = 0
num_of_draws = 0


def minimax(position, depth, alpha, beta, player):

    if set.type_of_game == 'zero_loyalty_variant':
        if set.current_player.color == 'black':

            if depth == 0 or position.root.data.is_in_exploding_loop:  # or game over in position
                # if the desired player won the position
                if black_player.tokennumber - 2 >= 0:
                    # tree depth that is 3

                    cond, winner = position.root.data.determine_winner()
                    if winner == set.current_player.color:
                        score = hs.linear_combination(position.root.data, player)
                    else:
                        score = 100 * (hs.linear_combination(position.root.data, 'black') - hs.linear_combination(
                            position.root.data, 'red')) / (hs.linear_combination(position.root.data, 'black') +
                            hs.linear_combination(position.root.data, 'red'))
                else:
                    score = 100 * (hs.linear_combination(position.root.data, 'black') - hs.linear_combination(position.root.data, 'red'))\
                            / (hs.linear_combination(position.root.data, 'black') + hs.linear_combination(position.root.data, 'red'))

                return score
            # this is the max scope
            if player == 'black':
                best_child = None

                # print('turn to black')
                # print('depth:', depth)
                max_val = -float('Inf')
                # set.current_player = red_player
                for child in position.children:
                    val = minimax(child, depth - 1, alpha, beta, 'red')
                    if val > max_val:
                        max_val = val
                        best_child = child
                    # print('val:', val)
                    alpha = max(alpha, val)
                    if beta <= alpha:
                        # print('hellooo')
                        break
                if depth == 3:
                    if best_child is None:
                        raise TypeError("Maliheeee!!!class: game ,function: minimax best_child is none")
                    else:
                        return max_val, best_child
                else:
                    return max_val
            # this is min scope
            elif player == 'red':
                best_child = None
                # print('turn to red')
                # print('depth:', depth)
                min_val = float('Inf')
                for child in position.children:
                    val = minimax(child, depth-1, alpha, beta, 'black')
                    # min_val = min(min_val, val)
                    if val < min_val:
                        min_val = val
                        if depth == 3:
                            best_child = child
                    beta = min(beta, val)
                    if beta <= alpha:
                        # print('helloooo')
                        break
                if depth == 3:
                    if best_child is None:
                        raise TypeError("Maliheeee!!!class: game ,function: minimax best_child is none")
                    else:
                        return min_val, best_child
                else:
                    return min_val

        if set.current_player.color == 'red':

            if depth == 0 or position.root.data.is_in_exploding_loop:  # or game over in position
                if red_player.tokennumber - 2 >= 0:  # and black_player.tokennumber - 2 == 0:
                    cond, winner = position.root.data.determine_winner()
                    if winner == set.current_player.color:
                        score = hs.linear_combination(position.root.data, player)
                    else:
                        score = 100 * (hs.linear_combination(position.root.data, 'red') - hs.linear_combination(
                            position.root.data, 'black')) \
                                / (hs.linear_combination(position.root.data, 'black') + hs.linear_combination(
                            position.root.data, 'red'))
                else:
                    score = 100 * (hs.linear_combination(position.root.data, 'red') - hs.linear_combination(position.root.data, 'black'))\
                            / (hs.linear_combination(position.root.data, 'black') + hs.linear_combination(position.root.data, 'red'))
                return score

            # this is the max scope
            if player == 'red':
                best_child = None
                max_val = -float('Inf')
                # set.current_player = red_player
                for child in position.children:
                    val = minimax(child, depth - 1, alpha, beta, 'black')
                    # max_val = max(max_val, val)
                    if val > max_val:
                        max_val = val
                        if depth == 3:
                            best_child = child
                    alpha = max(alpha, val)
                    if beta <= alpha:
                        break
                if depth == 3:
                    if best_child is None:
                        raise TypeError("Maliheeee!!!class: game ,function: minimax best_child is none")
                    else:
                        return max_val, best_child
                else:
                    return max_val

            # this is min scope
            elif player == 'black':
                best_child = None
                min_val = float('Inf')
                for child in position.children:
                    val = minimax(child, depth-1, alpha, beta, 'red')
                    # min_val = min(min_val, val)
                    if val < min_val:
                        min_val = val
                        if depth == 3:
                            best_child = child
                    beta = min(beta, val)
                    if beta <= alpha:
                        break
                if depth == 3:
                    if best_child is None:
                        raise TypeError("Maliheeee!!!class: game ,function: minimax best_child is none")
                    else:
                        return min_val, best_child
                else:
                    return min_val

    elif set.type_of_game == 'full_loyalty_variant' or set.type_of_game == 'different_loyalty_variant':
        if set.current_player.color == 'black':

            if depth == 0:
                if black_player.tokennumber - 2 >= 0:

                    cond, winner = position.root.data.determine_winner()
                    if winner == set.current_player.color:
                        score = hs.linear_combination(position.root.data, player)
                        print('score:', score)
                    else:
                        score = 100 * (hs.linear_combination(position.root.data, 'black') - hs.linear_combination(
                            position.root.data, 'red')) / (hs.linear_combination(position.root.data, 'black') +
                                                           hs.linear_combination(position.root.data, 'red'))
                else:
                    score = 100 * (hs.linear_combination(position.root.data, 'black') - hs.linear_combination(
                        position.root.data, 'red')) \
                            / (hs.linear_combination(position.root.data, 'black') + hs.linear_combination(
                               position.root.data, 'red'))

                return score

            elif len(position.children) == 0:
                if black_player.tokennumber - 1 >= 0:

                    cond, winner = position.root.data.determine_winner()
                    if winner == set.current_player.color:
                        score = hs.linear_combination(position.root.data, player)
                    else:
                        score = 100 * (hs.linear_combination(position.root.data, 'black') - hs.linear_combination(
                            position.root.data, 'red')) / (hs.linear_combination(position.root.data, 'black') +
                                                           hs.linear_combination(position.root.data, 'red'))
                else:
                    score = 100 * (hs.linear_combination(position.root.data, 'black') - hs.linear_combination(
                        position.root.data, 'red')) \
                            / (hs.linear_combination(position.root.data, 'black') + hs.linear_combination(
                               position.root.data, 'red'))

                return score

            # this is the max scope
            if player == 'black':
                best_child = None

                # print('turn to black')
                # print('depth:', depth)
                max_val = -float('Inf')
                # set.current_player = red_player
                for child in position.children:
                    val = minimax(child, depth - 1, alpha, beta, 'red')
                    if val > max_val:
                        max_val = val
                        if depth == 3:
                            best_child = child
                    # print('val:', val)
                    alpha = max(alpha, val)
                    if beta <= alpha:
                        # print('hellooo')
                        break
                if depth == 3:
                    if best_child is None:
                        raise TypeError("Maliheeee!!!class: game ,function: minimax best_child is none")
                    else:
                        return max_val, best_child
                else:
                    return max_val
            # this is min scope
            elif player == 'red':
                best_child = None
                # print('turn to red')
                # print('depth:', depth)
                min_val = float('Inf')
                for child in position.children:
                    val = minimax(child, depth - 1, alpha, beta, 'black')
                    # min_val = min(min_val, val)
                    if val < min_val:
                        min_val = val
                        if depth == 3:
                            best_child = child
                    beta = min(beta, val)
                    if beta <= alpha:
                        # print('helloooo')
                        break
                if depth == 3:
                    if best_child is None:
                        raise TypeError("Maliheeee!!!class: game ,function: minimax best_child is none")
                    else:
                        return min_val, best_child
                else:
                    return min_val

        if set.current_player.color == 'red':

            if depth == 0:  # or game over in position
                if red_player.tokennumber - 2 >= 0:  # and black_player.tokennumber - 2 == 0:
                    cond, winner = position.root.data.determine_winner()
                    if winner == set.current_player.color:
                        score = hs.linear_combination(position.root.data, player)
                    else:
                        score = 100 * (hs.linear_combination(position.root.data, 'red') - hs.linear_combination(
                            position.root.data, 'black')) \
                                / (hs.linear_combination(position.root.data, 'black') + hs.linear_combination(
                            position.root.data, 'red'))
                else:
                    score = 100 * (hs.linear_combination(position.root.data, 'red') - hs.linear_combination(
                        position.root.data, 'black')) \
                            / (hs.linear_combination(position.root.data, 'black') + hs.linear_combination(
                        position.root.data, 'red'))
                return score

            elif len(position.children) == 0:  # or game over in position
                if red_player.tokennumber - 1 >= 0:  # and black_player.tokennumber - 2 == 0:
                    cond, winner = position.root.data.determine_winner()
                    if winner == set.current_player.color:
                        score = hs.linear_combination(position.root.data, player)
                    else:
                        score = 100 * (hs.linear_combination(position.root.data, 'red') - hs.linear_combination(
                            position.root.data, 'black')) \
                                / (hs.linear_combination(position.root.data, 'black') + hs.linear_combination(
                            position.root.data, 'red'))
                else:
                    score = 100 * (hs.linear_combination(position.root.data, 'red') - hs.linear_combination(
                        position.root.data, 'black')) \
                            / (hs.linear_combination(position.root.data, 'black') + hs.linear_combination(
                        position.root.data, 'red'))
                return score

            # this is the max scope
            if player == 'red':
                best_child = None
                max_val = -float('Inf')
                # set.current_player = red_player
                for child in position.children:
                    val = minimax(child, depth - 1, alpha, beta, 'black')
                    # max_val = max(max_val, val)
                    if val > max_val:
                        max_val = val
                        if depth == 3:
                            best_child = child
                    alpha = max(alpha, val)
                    if beta <= alpha:
                        break
                if depth == 3:
                    if best_child is None:
                        raise TypeError("Maliheeee!!!class: game ,function: minimax best_child is none")
                    else:
                        return max_val, best_child
                else:
                    return max_val

            # this is min scope
            elif player == 'black':
                best_child = None
                min_val = float('Inf')
                for child in position.children:
                    val = minimax(child, depth - 1, alpha, beta, 'red')
                    # min_val = min(min_val, val)
                    if val < min_val:
                        min_val = val
                        if depth == 3:
                            best_child = child
                    beta = min(beta, val)
                    if beta <= alpha:
                        break
                if depth == 3:
                    if best_child is None:
                        raise TypeError("Maliheeee!!!class: game ,function: minimax best_child is none")
                    else:
                        return min_val, best_child
                else:
                    return min_val


def start_game(graph):
    global num_of_draws
    global num_of_black_winning
    global num_of_red_winning
    while not (msv.kbhit() and msv.getch() == chr(27).encode()):
        if set.type_of_game == 'zero_loyalty_variant':
            if red_player.tokennumber > 0 or black_player.tokennumber > 0:
                if not graph.is_in_exploding_loop:
                    if set.current_player.approach == 'alpha_beta':
                        tree_depth = 3
                        tree_search = make_tree(graph, tree_depth, 0, set.current_player.color)
                        print('tree created')
                        minimax_val, best_child = minimax(position=tree_search, depth=tree_depth, alpha=-float('Inf'),
                                              beta=float('Inf'), player=set.current_player.color)
                        print('minimax is done with value:', minimax_val)

                        # choosing the next move by exchange the current graph with the best child
                        graph = best_child.root.data
                        # get one token from the player who make the move
                        set.current_player.token_number -= 1
                        if set.current_player.color == 'red':
                            set.red_player_token = set.current_player.token_number
                        elif set.current_player.color == 'black':
                            set.black_player_token = set.current_player.token_number
                        # print('is it in loop?', graph.is_in_exploding_loop)
                        # for v in graph.vertices:
                        r, b = graph.token_num_in_graph()
                        print('num of all tokens:', r+b)
                        print('red players token:', red_player.tokennumber)
                        print('black players token:', black_player.tokennumber)

                    elif set.current_player.approach == 'MCTS':
                        initialState = State(graph=graph, curr_player=set.current_player.color,
                                             red_player_token=red_player.tokennumber,
                                             black_player_token=black_player.tokennumber)
                        mcts = MCTS(iterationLimit=100)
                        action = mcts.search(initialState=initialState)
                        graph = action.state.graph
                        set.current_player.token_number -= 1
                        if set.current_player.color == 'red':
                            set.red_player_token = set.current_player.token_number
                        elif set.current_player.color == 'black':
                            set.black_player_token = set.current_player.token_number

                    elif set.current_player.approach == 'dummy':

                        children = graph.next_position_of_graph(player=set.current_player.color,
                                                                player_remaining_token=set.current_player.token_number)
                        rand = random.randint(0, len(children)-1)
                        graph = children[rand]
                        set.current_player.token_number -= 1
                        if set.current_player.color == 'red':
                            set.red_player_token = set.current_player.token_number
                        elif set.current_player.color == 'black':
                            set.black_player_token = set.current_player.token_number
                        # print('is it in loop?', graph.is_in_exploding_loop)
                        r, b = graph.token_num_in_graph()
                        print('num of all tokens:', r + b)
                        print('red player token num ', red_player.tokennumber)
                        print('black player token num ', black_player.tokennumber)

                    elif set.current_player.approach == 'test':
                        children = graph.next_position_of_graph(player=set.current_player.color,
                                                                player_remaining_token=set.current_player.token_number)
                        max_val = - float('inf')
                        min_val = float('inf')
                        best_child = None
                        for child in children:
                            val = hs.linear_combination(child, set.current_player.color)
                            if val > max_val:
                                max_val = val
                                best_child = child
                        graph = best_child
                        set.current_player.token_number -= 1
                        if set.current_player.color == 'red':
                            set.red_player_token = set.current_player.token_number
                        elif set.current_player.color == 'black':
                            set.black_player_token = set.current_player.token_number

                    if set.current_player.color == 'black':
                        # print('turns to red')
                        black_player.turn = False
                        red_player.turn = True
                        set.current_player = red_player
                        set.opponent_player = black_player
                    elif set.current_player.color == 'red':
                        # print('turn to black')
                        red_player.turn = False
                        black_player.turn = True
                        set.current_player = black_player
                        set.opponent_player = red_player

                else:

                    if graph.is_one_color_token():
                        cond, winner = graph.determine_winner()
                        with open('zero_loyalty.txt', 'a') as file:
                            file.write('\n'+winner)

                        if winner == 'black':
                            num_of_black_winning += 1
                            return num_of_black_winning
                        elif winner == 'red':
                            num_of_red_winning += 1
                            return num_of_red_winning
                        print('clear victoryyyyy,', winner, 'wins')
                    else:
                        with open('zero_loyalty.txt', 'a') as file:
                            file.write('\n'+'none')
                        print('NOT ENDED STUCK IN LOOP :(((')
                        num_of_draws += 1
                        return num_of_draws

            elif red_player.tokennumber == 0 and black_player.tokennumber == 0:
                cond, winner = graph.determine_winner()

                if cond:
                    print('winner is:', winner)
                    if winner == 'black':
                        with open('zero_loyalty.txt', 'a') as file:
                            file.write('\n' + winner)
                        num_of_black_winning += 1
                        return num_of_black_winning
                    elif winner == 'red':
                        with open('zero_loyalty.txt', 'a') as file:
                            file.write('\n' + winner)
                        num_of_red_winning += 1
                        return num_of_red_winning
                    else:
                        with open('zero_loyalty.txt', 'a') as file:
                            file.write('\n' + 'none')
                        print('the game ended but non of players won')
                        # global num_of_draws
                        num_of_draws += 1
                        return num_of_draws

        elif set.type_of_game == 'full_loyalty_variant':
            black_nodes, red_nodes, inactive = graph.nodes_state()
            if (red_player.tokennumber > 0 or black_player.tokennumber > 0) and black_nodes + red_nodes < graph.node_number():
                if set.current_player.approach == 'alpha_beta':
                    tree_depth = 3
                    tree_search = make_tree(graph, tree_depth, 0, set.current_player.color)
                    print('tree created')
                    minimax_val, best_child = minimax(position=tree_search, depth=tree_depth, alpha=-float('Inf'),
                                                      beta=float('Inf'), player=set.current_player.color)
                    print('minimax is done with value:', minimax_val)

                    # choosing the next move by exchange the current graph with the best child
                    graph = best_child.root.data
                    # get one token from the player who make the move
                    set.current_player.token_number -= 1
                    if set.current_player.color == 'red':
                        set.red_player_token = set.current_player.token_number
                    elif set.current_player.color == 'black':
                        set.black_player_token = set.current_player.token_number
                    for node in graph.vertices:
                        print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token', node.redtoken,
                              'state:', node.state)
                    print('red players token:', red_player.tokennumber)
                    print('black players token:', black_player.tokennumber)

                elif set.current_player.approach == 'MCTS':
                    initialState = State(graph=graph, curr_player=set.current_player.color,
                                         red_player_token=red_player.tokennumber,
                                         black_player_token=black_player.tokennumber)
                    mcts = MCTS(iterationLimit=100)
                    action = mcts.search(initialState=initialState)
                    # graph = best_child.state.graph  # action.graph
                    graph = action.graph

                    set.current_player.token_number -= 1
                    if set.current_player.color == 'red':
                        set.red_player_token = set.current_player.token_number
                    elif set.current_player.color == 'black':
                        set.black_player_token = set.current_player.token_number

                    for node in graph.vertices:
                        print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token', node.redtoken,
                              'state:', node.state)
                    print('red players token:', red_player.tokennumber)
                    print('black players token:', black_player.tokennumber)

                elif set.current_player.approach == 'dummy':
                    children = graph.next_position_of_graph(player=set.current_player.color,
                                                            player_remaining_token=set.current_player.token_number)
                    rand = random.randint(0, len(children) - 1)
                    graph = children[rand]
                    set.current_player.token_number -= 1
                    if set.current_player.color == 'red':
                        set.red_player_token = set.current_player.token_number
                    elif set.current_player.color == 'black':
                        set.black_player_token = set.current_player.token_number
                    for node in graph.vertices:
                        print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token', node.redtoken,
                              'state:', node.state)
                    print('red player token num ', red_player.tokennumber)
                    print('black player token num ', black_player.tokennumber)

                if set.current_player.color == 'black':
                    # print('turns to red')
                    black_player.turn = False
                    red_player.turn = True
                    set.current_player = red_player
                    set.opponent_player = black_player
                elif set.current_player.color == 'red':
                    # print('turn to black')
                    red_player.turn = False
                    black_player.turn = True
                    set.current_player = black_player
                    set.opponent_player = red_player

            else:
                cond, winner = graph.determine_winner()

                if cond:
                    print('winner is:', winner)
                    if winner == 'black':
                        with open('full_loyalty.txt', 'a') as file:
                            file.write('\n' + winner)
                        num_of_black_winning += 1
                        return num_of_black_winning
                    elif winner == 'red':
                        with open('full_loyalty.txt', 'a') as file:
                            file.write('\n' + winner)
                        num_of_red_winning += 1
                        return num_of_red_winning
                    else:
                        with open('full_loyalty.txt', 'a') as file:
                            file.write('\n' + 'none')
                        print('the game ended with draws and non of players won')
                        # global num_of_draws
                        num_of_draws += 1
                        return num_of_draws

        elif set.type_of_game == 'full_loyalty_more_token':
            black_nodes, red_nodes, inactive = graph.nodes_state()
            if (red_player.tokennumber > 0 or black_player.tokennumber > 0) and black_nodes + red_nodes < graph.node_number():
                if set.current_player.approach == 'alpha_beta':
                    tree_depth = 3
                    tree_search = make_tree(graph, tree_depth, 0, set.current_player.color)
                    print('tree created')
                    minimax_val, best_child = minimax(position=tree_search, depth=tree_depth, alpha=-float('Inf'),
                                                      beta=float('Inf'), player=set.current_player.color)
                    print('minimax is done with value:', minimax_val)

                    # choosing the next move by exchange the current graph with the best child
                    graph = best_child.root.data
                    # get one token from the player who make the move
                    set.current_player.token_number -= 1
                    if set.current_player.color == 'red':
                        set.red_player_token = set.current_player.token_number
                    elif set.current_player.color == 'black':
                        set.black_player_token = set.current_player.token_number
                    for node in graph.vertices:
                        print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token', node.redtoken,
                              'state:', node.state)
                    print('red players token:', red_player.tokennumber)
                    print('black players token:', black_player.tokennumber)

                elif set.current_player.approach == 'MCTS':
                    initialState = State(graph=graph, curr_player=set.current_player.color,
                                         red_player_token=red_player.tokennumber,
                                         black_player_token=black_player.tokennumber)
                    if set.flmt_strategy == 'naive':
                        mcts = MCTS(iterationLimit=100)
                    elif set.flmt_strategy == 'advanced':
                        mcts = MCTS(iterationLimit=1000)

                    action = mcts.search(initialState=initialState)
                    graph = action.graph  # best_child.state.graph

                    set.current_player.token_number -= action.token_capacity
                    if set.current_player.color == 'red':
                        set.red_player_token = set.current_player.token_number
                    elif set.current_player.color == 'black':
                        set.black_player_token = set.current_player.token_number

                    for node in graph.vertices:
                        print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token', node.redtoken,
                              'state:', node.state)
                    print('red players token:', red_player.tokennumber)
                    print('black players token:', black_player.tokennumber)

                elif set.current_player.approach == 'dummy':
                    valid_graph = []
                    valid_token = []
                    give_one_token_graph = []
                    children, token_capacity = graph.next_position_of_graph(player=set.current_player.color,
                                                                            player_remaining_token=set.current_player.token_number)
                    if set.flmt_strategy == 'naive':
                        deactive_nodes, num_of_deactive_nodes = graph.deactive_nodes()
                        for idx, node in enumerate(deactive_nodes):
                            if token_capacity[idx] <= set.current_player.token_number:
                                valid_graph.append(children[idx])
                                valid_token.append(token_capacity[idx])
                            else:
                                give_one_token_graph.append(children[idx])
                                # valid_token.append(token_capacity[idx])
                        if len(valid_graph) > 0:
                            rand = random.randint(0, len(valid_graph) - 1)
                            graph = valid_graph[rand]
                            set.current_player.token_number -= valid_token[rand]
                        else:
                            rand = random.randint(0, len(give_one_token_graph) - 1)
                            graph = give_one_token_graph[rand]
                            set.current_player.token_number -= 1

                    elif set.flmt_strategy == 'advanced':
                        if len(children) == 0:
                            if set.current_player.tokennumber > 0:
                                raise TypeError('in dummy strategy : current player has tokens but '
                                                'there is no possible action ')
                        else:
                            rand = random.randint(0, len(children) - 1)
                            graph = children[rand]
                            set.current_player.token_number -= token_capacity[rand]

                    if set.current_player.color == 'red':
                        set.red_player_token = set.current_player.token_number
                    elif set.current_player.color == 'black':
                        set.black_player_token = set.current_player.token_number
                    for node in graph.vertices:
                        print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token', node.redtoken,
                              'state:', node.state)
                    print('red player token num ', red_player.tokennumber)
                    print('black player token num ', black_player.tokennumber)

                if set.current_player.color == 'black':
                    if red_player.tokennumber != 0:
                        black_player.turn = False
                        red_player.turn = True
                        set.current_player = red_player
                        set.opponent_player = black_player
                elif set.current_player.color == 'red':
                    if black_player.tokennumber != 0:
                        red_player.turn = False
                        black_player.turn = True
                        set.current_player = black_player
                        set.opponent_player = red_player

            else:
                cond, winner = graph.determine_winner()

                if cond:
                    print('winner is:', winner)
                    if winner == 'black':
                        with open('full_loyalty_more_token.txt', 'a') as file:
                            file.write('\n' + winner)
                        num_of_black_winning += 1
                        return num_of_black_winning
                    elif winner == 'red':
                        with open('full_loyalty_more_token.txt', 'a') as file:
                            file.write('\n' + winner)
                        num_of_red_winning += 1
                        return num_of_red_winning
                    else:
                        with open('full_loyalty_more_token.txt', 'a') as file:
                            file.write('\n' + 'none')
                        print('the game ended with draws and non of players won')
                        # global num_of_draws
                        num_of_draws += 1
                        return num_of_draws

        elif set.type_of_game == 'different_loyalty_variant':
            if set.dlv_strategy == 'naive':
                black_nodes, red_nodes, inactive = graph.nodes_state()
                if (red_player.tokennumber > 0 or black_player.tokennumber > 0) and black_nodes+red_nodes <graph.node_number():
                    if set.current_player.approach == 'alpha_beta':
                        tree_depth = 3
                        tree_search = make_tree(graph, tree_depth, 0, set.current_player.color)
                        print('tree created')
                        minimax_val, best_child = minimax(position=tree_search, depth=tree_depth, alpha=-float('Inf'),
                                                          beta=float('Inf'), player=set.current_player.color)
                        print('minimax is done with value:', minimax_val)

                        # choosing the next move by exchange the current graph with the best child
                        graph = best_child.root.data
                        # get one token from the player who make the move
                        set.current_player.token_number -= 1
                        if set.current_player.color == 'red':
                            set.red_player_token = set.current_player.token_number
                        elif set.current_player.color == 'black':
                            set.black_player_token = set.current_player.token_number
                        for node in graph.vertices:
                            print('threshold:', node.threshold, 'token:', node.blacktoken + node.redtoken, 'state:',
                                  node.state)
                        print('red players token:', red_player.tokennumber)
                        print('black players token:', black_player.tokennumber)

                    elif set.current_player.approach == 'MCTS':
                        initialState = State(graph=graph, curr_player=set.current_player.color,
                                             red_player_token=red_player.tokennumber,
                                             black_player_token=black_player.tokennumber)
                        mcts = MCTS(iterationLimit=100)
                        best_child = mcts.search(initialState=initialState)
                        graph = best_child.state.graph  # action.graph

                        set.current_player.token_number -= 1
                        if set.current_player.color == 'red':
                            set.red_player_token = set.current_player.token_number
                        elif set.current_player.color == 'black':
                            set.black_player_token = set.current_player.token_number

                        for node in graph.vertices:
                            print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token',
                                  node.redtoken,
                                  'state:', node.state)
                        print('red players token:', red_player.tokennumber)
                        print('black players token:', black_player.tokennumber)

                    elif set.current_player.approach == 'dummy':
                        children = graph.next_position_of_graph(player=set.current_player.color,
                                                                player_remaining_token=set.current_player.token_number)
                        if len(children) != 0:  # in the case which there is no inactive nodes
                            rand = random.randint(0, len(children) - 1)
                            graph = children[rand]
                            set.current_player.token_number -= 1
                            if set.current_player.color == 'red':
                                set.red_player_token = set.current_player.token_number
                            elif set.current_player.color == 'black':
                                set.black_player_token = set.current_player.token_number
                            for node in graph.vertices:
                                print('threshold:', node.threshold, 'token:', node.blacktoken + node.redtoken, 'state:', node.state)

                        print('red player token num ', red_player.tokennumber)
                        print('black player token num ', black_player.tokennumber)

                    if set.current_player.color == 'black':
                        # print('turns to red')
                        black_player.turn = False
                        red_player.turn = True
                        set.current_player = red_player
                        set.opponent_player = black_player
                    elif set.current_player.color == 'red':
                        # print('turn to black')
                        red_player.turn = False
                        black_player.turn = True
                        set.current_player = black_player
                        set.opponent_player = red_player

                else:
                    cond, winner = graph.determine_winner()

                    if cond:
                        print('winner is:', winner)
                        if winner == 'black':
                            with open('diff_loyalty.txt', 'a') as file:
                                file.write('\n' + winner)
                            num_of_black_winning += 1
                            return num_of_black_winning
                        elif winner == 'red':
                            with open('diff_loyalty.txt', 'a') as file:
                                file.write('\n' + winner)
                            num_of_red_winning += 1
                            return num_of_red_winning
                        else:
                            with open('diff_loyalty.txt', 'a') as file:
                                file.write('\n' + 'none')
                            print('the game ended with draws and non of players won')
                            # global num_of_draws
                            num_of_draws += 1
                            return num_of_draws

            elif set.dlv_strategy == 'advanced':

                black_nodes, red_nodes, inactive = graph.nodes_state()
                if (red_player.tokennumber > 0 or black_player.tokennumber > 0) and black_nodes + red_nodes < graph.node_number():

                    if set.current_player.approach == 'alpha_beta':
                        tree_depth = 3
                        tree_search = make_tree(graph, tree_depth, 0, set.current_player.color)
                        print('tree created')
                        minimax_val, best_child = minimax(position=tree_search, depth=tree_depth, alpha=-float('Inf'),
                                                          beta=float('Inf'), player=set.current_player.color)
                        print('minimax is done with value:', minimax_val)

                        # choosing the next move by exchange the current graph with the best child
                        graph = best_child.root.data
                        # get one token from the player who make the move
                        set.current_player.token_number -= 1
                        if set.current_player.color == 'red':
                            set.red_player_token = set.current_player.token_number
                        elif set.current_player.color == 'black':
                            set.black_player_token = set.current_player.token_number
                        for node in graph.vertices:
                            print('threshold:', node.threshold, 'token:', node.blacktoken + node.redtoken, 'state:',
                                  node.state)
                        print('red players token:', red_player.tokennumber)
                        print('black players token:', black_player.tokennumber)

                    elif set.current_player.approach == 'MCTS':
                        if not ((red_player.tokennumber == 0 and set.current_player.color == 'red') or
                                (black_player.tokennumber == 0 and set.current_player.color == 'black')):
                            initialState = State(graph=graph, curr_player=set.current_player.color,
                                                 red_player_token=red_player.tokennumber,
                                                 black_player_token=black_player.tokennumber)
                            mcts = MCTS(iterationLimit=250)
                            idx, best_child = mcts.search(initialState=initialState)
                            # dlv_flag determines when we use node_loyalty_variant method for updating the
                            # experimental_loyalty (DLV_FLAG = TRUE)of nodes and when we use node_loyalty method which
                            # doesnt update experimental_loyalty and it is used in mcts tree(DLV_FLAG = FALSE)

                            # we should reproduce the root children because the diffusing of neighbors effects on the
                            # experimental loyalty which doesnt consider in MCTS

                            # DLV_FLAG_NEIGHBORS determines when diffusion of nodes change the loyalty of neighbor(true)
                            # and when it shouldn't change it(false),among the mcts tree it does not change the experimental
                            # loyalty of nodes

                            # DLV_FLAG_NEIGHBORS = true =====> advanced_dlv_diffusion()
                            # DLV_FLAG_NEIGHBORS = false =====> token_diffusion_to_neighbors()
                            #
                            next_position, experimental_loyalty_values, token_capacity = graph.next_position_of_graph(player=set.current_player.color, player_remaining_token=set.current_player.token_number, dlv_flag=True, dlv_flag_neighbors=True)#[idx]
                            graph = next_position[idx]

                            # graph = best_child.graph  # action.graph

                            # we call node_loyalty_variant to update the nodes experimental loyalty
                            # for node in graph.vertices:
                            #     if node.state == set.current_player.color:
                            #         graph.node_loyalty_variant(node)

                            set.current_player.token_number -= best_child.token_capacity  # token_capacity[idx]
                            if set.current_player.color == 'red':
                                set.red_player_token = set.current_player.token_number
                            elif set.current_player.color == 'black':
                                set.black_player_token = set.current_player.token_number

                            for node in graph.vertices:
                                print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token',
                                      node.redtoken,
                                      'state:', node.state)
                            print('red players token:', red_player.tokennumber)
                            print('black players token:', black_player.tokennumber)

                    elif set.current_player.approach == 'dummy':
                        children = graph.next_position_of_graph(player=set.current_player.color,
                                                                player_remaining_token=set.current_player.token_number)
                        if len(children) != 0:  # in the case which there is no inactive nodes
                            rand = random.randint(0, len(children) - 1)
                            graph = children[rand]
                            set.current_player.token_number -= 1
                            if set.current_player.color == 'red':
                                set.red_player_token = set.current_player.token_number
                            elif set.current_player.color == 'black':
                                set.black_player_token = set.current_player.token_number
                            for node in graph.vertices:
                                print('threshold:', node.threshold, 'token:', node.blacktoken + node.redtoken, 'state:',
                                      node.state)

                        print('red player token num ', red_player.tokennumber)
                        print('black player token num ', black_player.tokennumber)

                    if set.current_player.color == 'black':
                        # print('turns to red')
                        black_player.turn = False
                        red_player.turn = True
                        set.current_player = red_player
                        set.opponent_player = black_player
                        set.dlv_player_approach = 'loyalty_guess_not_learn'  # 'loyalty_guess_learn'
                    elif set.current_player.color == 'red':
                        # print('turn to black')
                        red_player.turn = False
                        black_player.turn = True
                        set.current_player = black_player
                        set.opponent_player = red_player
                        # set.dlv_player_approach = 'loyalty_guess_learn'  # 'loyalty_guess_not_learn'

                else:
                    cond, winner = graph.determine_winner()

                    if cond:
                        print('winner is:', winner)
                        if winner == 'black':
                            with open('diff_loyalty.txt', 'a') as file:
                                file.write('\n' + winner)
                            num_of_black_winning += 1
                            return num_of_black_winning
                        elif winner == 'red':
                            with open('diff_loyalty.txt', 'a') as file:
                                file.write('\n' + winner)
                            num_of_red_winning += 1
                            return num_of_red_winning
                        else:
                            with open('diff_loyalty.txt', 'a') as file:
                                file.write('\n' + 'none')
                            print('the game ended with draws and non of players won')
                            # global num_of_draws
                            num_of_draws += 1
                            return num_of_draws

        elif set.type_of_game == 'harder_reactivation':

            if set.hra_strategy == 'naive':

                black_nodes, red_nodes, inactive = graph.nodes_state()
                if (red_player.tokennumber > 0 or black_player.tokennumber > 0) and black_nodes + red_nodes < graph.node_number():

                    if set.current_player.approach == 'alpha_beta':
                        tree_depth = 3
                        tree_search = make_tree(graph, tree_depth, 0, set.current_player.color)
                        print('tree created')
                        minimax_val, best_child = minimax(position=tree_search, depth=tree_depth, alpha=-float('Inf'),
                                                          beta=float('Inf'), player=set.current_player.color)
                        print('minimax is done with value:', minimax_val)

                        # choosing the next move by exchange the current graph with the best child
                        graph = best_child.root.data
                        # get one token from the player who make the move
                        set.current_player.token_number -= 1
                        if set.current_player.color == 'red':
                            set.red_player_token = set.current_player.token_number
                        elif set.current_player.color == 'black':
                            set.black_player_token = set.current_player.token_number
                        for node in graph.vertices:
                            print('threshold:', node.threshold, 'token:', node.blacktoken + node.redtoken, 'state:',
                                  node.state)
                        print('red players token:', red_player.tokennumber)
                        print('black players token:', black_player.tokennumber)

                    elif set.current_player.approach == 'MCTS':
                        if not ((red_player.tokennumber == 0 and set.current_player.color == 'red') or
                                (black_player.tokennumber == 0 and set.current_player.color == 'black')):
                            initialState = State(graph=graph, curr_player=set.current_player.color,
                                                 red_player_token=red_player.tokennumber,
                                                 black_player_token=black_player.tokennumber)
                            mcts = MCTS(iterationLimit=1000)
                            best_child = mcts.search(initialState=initialState)
                            graph = best_child.graph
                            set.current_player.token_number -= best_child.token_capacity  # token_capacity[idx]
                            if set.current_player.color == 'red':
                                set.red_player_token = set.current_player.token_number
                            elif set.current_player.color == 'black':
                                set.black_player_token = set.current_player.token_number

                            for node in graph.vertices:
                                print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token',
                                      node.redtoken,
                                      'state:', node.state)
                            print('red players token:', red_player.tokennumber)
                            print('black players token:', black_player.tokennumber)

                    elif set.current_player.approach == 'dummy':
                        valid_graph = []
                        valid_token = []
                        give_one_token_graph = []
                        children, token_capacity = graph.next_position_of_graph(player=set.current_player.color,
                        player_remaining_token=set.current_player.token_number)
                        # deactive_nodes = graph.deactive_opposite_nodes(set.current_player.color)
                        for idx, val in enumerate(token_capacity):
                            if val <= set.current_player.token_number:
                                valid_graph.append(children[idx])
                                valid_token.append(token_capacity[idx])
                            else:
                                give_one_token_graph.append(children[idx])
                                # valid_token.append(token_capacity[idx])
                        if len(valid_graph) > 0:
                            rand = random.randint(0, len(valid_graph) - 1)
                            graph = valid_graph[rand]
                            set.current_player.token_number -= valid_token[rand]
                        elif set.current_player.token_number>0:
                            rand = random.randint(0, len(give_one_token_graph) - 1)
                            graph = give_one_token_graph[rand]
                            set.current_player.token_number -= 1
                        for node in graph.vertices:
                            print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token',
                                  node.redtoken,
                                  'state:', node.state)
                        print('red players token:', red_player.tokennumber)
                        print('black players token:', black_player.tokennumber)

                    elif set.current_player.approach == 'maximum_threshold':
                        valid_graph = []
                        valid_token = []
                        give_one_token_graph = []
                        children, token_capacity = graph.next_position_of_graph(player=set.current_player.color,
                        player_remaining_token=set.current_player.token_number)
                        tc = token_capacity
                        temp = 0
                        imax = np.argmax(token_capacity)
                        while token_capacity[imax] > set.current_player.token_number :
                            token_capacity[imax] = -1
                            if (token_capacity[np.argmax(token_capacity)])>0:
                                imax = np.argmax(token_capacity)
                            else:
                                imax = None
                                break
                        if imax!=None:
                            graph = children[imax]
                            set.current_player.token_number -= token_capacity[imax]
                        elif set.current_player.token_number >0:
                            ids=[]
                            nodes = graph.deactive_opposite_nodes(set.current_player.color)
                            for node in nodes:
                                ids.append(node.id)
                            imax = np.argmax(tc)
                            graph.vertices[ids[imax]].redtoken = set.current_player.token_number
                            set.current_player.token_number = 0


                        for node in graph.vertices:
                            print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token',
                                  node.redtoken,
                                  'state:', node.state)
                        print('red players token:', red_player.tokennumber)
                        print('black players token:', black_player.tokennumber)

                    elif set.current_player.approach == 'minimum_threshold':
#                         children, token_capacity = graph.next_position_of_graph(player=set.current_player.color,
#                         player_remaining_token=set.current_player.token_number)
#                         temp = 0
#                         imin = np.argmin(token_capacity)
#                         while token_capacity[imin] > set.current_player.token_number:
#                             token_capacity[imin] = 1000
#                             imin = np.argmax(token_capacity)
#                         graph = children[imin]
#                         set.current_player.token_number -= token_capacity[imin]
# #############################################################
                        children, token_capacity = graph.next_position_of_graph(player=set.current_player.color,
                                                                                player_remaining_token=set.current_player.token_number)
                        tc = token_capacity
                        temp = 0
                        imin = np.argmin(token_capacity)
                        while token_capacity[imin] > set.current_player.token_number:
                            token_capacity[imin] = 1000
                            if (token_capacity[np.argmin(token_capacity)]) < 1000:
                                imin = np.argmin(token_capacity)
                            else:
                                imin = None
                                break
                        if imin != None:
                            graph = children[imin]
                            set.current_player.token_number -= token_capacity[imin]
                        elif set.current_player.token_number > 0:
                            ids = []
                            nodes = graph.deactive_opposite_nodes(set.current_player.color)
                            for node in nodes:
                                ids.append(node.id)
                            imin = np.argmin(tc)
                            graph.vertices[ids[imin]].redtoken = set.current_player.token_number
                            set.current_player.token_number = 0
                        for node in graph.vertices:
                            print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token',
                                  node.redtoken,
                                  'state:', node.state)
                        print('red players token:', red_player.tokennumber)
                        print('black players token:', black_player.tokennumber)

                    if set.current_player.color == 'black':
                        # print('turns to red')
                        black_player.turn = False
                        red_player.turn = True
                        set.current_player = red_player
                        set.opponent_player = black_player
                        # set.dlv_player_approach = 'loyalty_guess_not_learn'  # 'loyalty_guess_learn'
                        set.mcts_approach = 'no_heuristic'

                    elif set.current_player.color == 'red':
                        # print('turn to black')
                        red_player.turn = False
                        black_player.turn = True
                        set.current_player = black_player
                        set.opponent_player = red_player
                        set.mcts_approach = 'use_heuristic'

                        # set.dlv_player_approach = 'loyalty_guess_learn'  # 'loyalty_guess_not_learn'

                else:
                    cond, winner = graph.determine_winner()

                    if cond:
                        print('winner is:', winner)
                        if winner == 'black':
                            with open('p2p_red_starts_MCvsMC.txt', 'a') as file:
                                file.write('\n' + winner)
                            num_of_black_winning += 1
                            return num_of_black_winning
                        elif winner == 'red':
                            with open('p2p_red_starts_MCvsMC.txt', 'a') as file:
                                file.write('\n' + winner)
                            num_of_red_winning += 1
                            return num_of_red_winning
                        else:
                            with open('p2p_red_starts_MCvsMC.txt', 'a') as file:
                                file.write('\n' + 'none')
                            print('the game ended with draws and non of players won')
                            # global num_of_draws
                            num_of_draws += 1
                            return num_of_draws


if __name__ == '__main__':
    for j in [3]:
        for i in range(1):
            if j == 0:
                type = 'random_graph'
                data_name = 'random_graph'
            if j == 1:
                type = 'small_world'
                data_name = None
            elif j == 2:
                type = 'scale_free'
                data_name = None
            elif j == 3:
                type = 'real_ds'
                data_name = 'p2p'
            with open('p2p_red_starts_MCvsMC.txt', 'a') as file:
                file.write(data_name)


            data, initial_token_num = set.create_data(type, data_name)
            graph = set.create_graph()
            for i in range(20):
                print(i, 'th run')
                red_player = Player(color='red', token_number=initial_token_num, turn=True, approach='MCTS')
                black_player = Player(color='black', token_number=initial_token_num, turn=False, approach='MCTS')
                set.black_player_token = initial_token_num
                set.red_player_token = initial_token_num
                if red_player.turn:
                    set.current_player = red_player
                    set.opponent_player = black_player
                elif black_player.turn:
                    set.current_player = black_player
                    set.opponent_player = red_player

                for node in graph.vertices:
                    print(node.id, ':', node.threshold, node.neighbors)
                print('type of game :', set.type_of_game)
                print('type of dataset : ')
                print('node_number:', graph.node_number())
                print('edge number :', graph.edge_number())
                print('number of tokens for each player', black_player.tokennumber, red_player.tokennumber)
                print('black strategy:', black_player.approach)
                print('red strategy:', red_player.approach)
                start_game(graph)
