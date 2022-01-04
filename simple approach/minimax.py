import setting as set
import heuristics as hs


def minimax(position, depth, alpha, beta, player):
    # print('1 black token:', position.root.black_player_token)
    # print('1 red token:', position.root.red_player_token)
    if set.type_of_game == 'zero_loyalty_variant':
        if set.current_player.color == 'black':

            if depth == 0 or position.root.data.is_in_exploding_loop:  # or game over in position
                # if the desired player won the position
                if set.black_player.tokennumber - 2 >= 0:  # and red_player.tokennumber - 2 == 0:  # minus 3 is because of the
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
                if set.red_player.tokennumber - 2 >= 0:  # and black_player.tokennumber - 2 == 0:
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

    elif set.type_of_game == 'full_loyalty_more_token' or set.type_of_game == 'harder_reactivation':
        if set.current_player.color == 'black':

            if depth == 0 or len(position.children) == 0:  # or game over in position
                # if the desired player won the position
                if set.current_player.tokennumber - 2 >= 0:  # and red_player.tokennumber - 2 == 0:# minus 3 is because of the
                    # tree depth that is 3

                    cond, winner = position.root.data.determine_winner()
                    if winner == set.current_player.color:
                        if player == 'black':
                            score = hs.linear_combination(position.root.data, player, position.root.black_player_token)
                        elif player == 'red':
                            score = hs.linear_combination(position.root.data, player, position.root.red_player_token)
                    else:
                        # print('2 black token:', position.root.black_player_token)
                        # print('2 red token:', position.root.red_player_token)
                        if ((hs.linear_combination(position.root.data, 'black', position.root.black_player_token) +
                        hs.linear_combination(position.root.data, 'red', position.root.red_player_token)) == 0):

                             score = 0
                        else:
                            score = 100 * (hs.linear_combination(position.root.data, 'black', position.root.black_player_token) - hs.linear_combination(
                            position.root.data, 'red', position.root.red_player_token)) /\
                                (hs.linear_combination(position.root.data, 'black', position.root.black_player_token) +
                                                       hs.linear_combination(position.root.data, 'red', position.root.red_player_token))
                else:
                    if ((hs.linear_combination(position.root.data, 'black', position.root.black_player_token) +
                         hs.linear_combination(position.root.data, 'red', position.root.red_player_token)) == 0):
                        score = 0
                    else:
                        score = 100 * (hs.linear_combination(position.root.data, 'black', position.root.black_player_token)
                                   - hs.linear_combination(position.root.data, 'red', position.root.red_player_token)) \
                            / (hs.linear_combination(position.root.data, 'black', position.root.black_player_token) +
                               hs.linear_combination(position.root.data, 'red', position.root.red_player_token))

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

            if depth == 0 or len(position.children) == 0:  # or game over in position
                if set.current_player.tokennumber - 2 >= 0:  # and black_player.tokennumber - 2 == 0:
                    cond, winner = position.root.data.determine_winner()
                    if winner == set.current_player.color:
                        # score = hs.linear_combination(position.root.data, player, )
                        if player == 'black':
                            score = hs.linear_combination(position.root.data, player, position.root.black_player_token)
                        elif player == 'red':
                            score = hs.linear_combination(position.root.data, player, position.root.red_player_token)

                    else:
                        if ((hs.linear_combination(position.root.data, 'black', position.root.black_player_token) +
                             hs.linear_combination(position.root.data, 'red', position.root.red_player_token)) == 0):
                            score = 0
                        else:
                            score = 100 * (hs.linear_combination(position.root.data, 'red', position.root.red_player_token) - hs.linear_combination(
                                position.root.data, 'black', position.root.black_player_token)) \
                                    / (hs.linear_combination(position.root.data, 'black', position.root.black_player_token)
                                       + hs.linear_combination(position.root.data, 'red', position.root.red_player_token))
                else:
                    if ((hs.linear_combination(position.root.data, 'black', position.root.black_player_token) +
                         hs.linear_combination(position.root.data, 'red', position.root.red_player_token)) == 0):
                        score = 0
                    else:
                        score = 100 * (hs.linear_combination(position.root.data, 'red',position.root.red_player_token) - hs.linear_combination(
                        position.root.data, 'black', position.root.black_player_token)) \
                            / (hs.linear_combination(position.root.data, 'black', position.root.black_player_token) + hs.linear_combination(
                        position.root.data, 'red', position.root.red_player_token))
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

