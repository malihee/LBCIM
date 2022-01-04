import graph as graph
import setting as set
import networkx as nx
import numpy as np


def parity_heuristic(graph, player):
    if set.type_of_game == 'zero_loyalty_variant':
        red, black = graph.token_num_in_graph()
        # if set.current_player.color == 'red':
        if player == 'red':
            return red - black
        # elif set.current_player.color == 'black':
        elif player == 'black':
            return black - red
    elif set.type_of_game == 'full_loyalty_variant':
        red_nodes, black_nodes, deactive_noedes = graph.nodes_state()
        if player == 'red':
            return red_nodes - black_nodes
        # elif set.current_player.color == 'black':
        elif player == 'black':
            return black_nodes - red_nodes

    elif set.type_of_game == 'full_loyalty_more_token' or set.type_of_game == 'harder_reactivation':
        red_nodes, black_nodes, deactive_noedes = graph.nodes_state()
        if player == 'red':
            return red_nodes - black_nodes
        # elif set.current_player.color == 'black':
        elif player == 'black':
            return black_nodes - red_nodes


def paper_parity_heuristic(graph, player):

    if set.type_of_game == 'zero_loyalty_variant':
        red, black = graph.token_num_in_graph()
        # if set.current_player.color == 'red':
        if player == 'red':
            return red
        # elif set.current_player.color == 'black':
        elif player == 'black':
            return black
    elif set.type_of_game == 'full_loyalty_variant':
        red_nodes, black_nodes, deactive_noedes = graph.nodes_state()
        if player == 'red':
            red_nodes, black_nodes, deactive_noedes = graph.nodes_state()
            red_nodes, black_nodes, deactive_noedes = graph.nodes_state()
            red_nodes, black_nodes, deactive_noedes = graph.nodes_state()
            red_nodes, black_nodes, deactive_noedes = graph.nodes_state()
            return red_nodes
        # elif set.current_player.color == 'black':
        elif player == 'black':
            return black_nodes
    elif set.type_of_game == 'full_loyalty_more_token':
        red_nodes, black_nodes, deactive_noedes = graph.nodes_state()
        if player == 'red':
            return red_nodes
        # elif set.current_player.color == 'black':
        elif player == 'black':
            return black_nodes

# ############################################### full_loyalty_more_token_heu ##########################################


def majority_token(graph, player):
    score = 0
    if player == 'black':
        for node in graph.vertices:
            if node.blacktoken >= node.redtoken and node.state == 'deactive' or\
               node.redtoken > node.blacktoken and node.threshold - node.redtoken >= node.redtoken and node.state == 'deactive':
                score += 1.0

    elif player == 'red':
        for node in graph.vertices:
            if node.redtoken >= node.blacktoken and node.state == 'deactive' or\
                node.blacktoken > node.redtoken and node.threshold - node.blacktoken >= node.blacktoken and \
                    node.state == 'deactive':
                score += 1.0

    return score


# def opponent_majority_token(graph, player):
#     score = 0
#     if player == 'black':
#         for node in graph.vertices:
#             if node.redtoken > node.blacktoken and node.threshold - node.redtoken >= node.redtoken and node.state == 'deactive':
#                 score += 1.0
#             if node.redtoken > node.blacktoken and node.threshold - node.redtoken < node.redtoken:
#                 score += -1.0
#     elif player == 'red':
#         for node in graph.vertices:
#             if node.blacktoken > node.redtoken and node.threshold - node.blacktoken >= node.blacktoken and node.state == 'deactive':
#                 score += 1.0
#             if node.blacktoken > node.redtoken and node.threshold - node.blacktoken < node.blacktoken:
#                 score += -1.0
#     return score


def hubs_with_weak_neighbor(graph, player, player_token):
    # print('player token:', player_token)
    # print('into hub heu')
    hubs, authority = set.hits()
    hubs_node = list(reversed(list(hubs)))
    hubs_node = hubs_node[:int(np.floor(len(hubs_node)/3))]
    authority_node = list(reversed(list(authority)))
    authority_node = authority_node[:int(np.floor(len(authority_node)/3))]

    score = 0
    # highest_threshold = find_the_highest_threshold(graph)
    if player == 'black':
        for node in [graph.vertices[id] for id in authority_node]:
            # if node.threshold >= .6 * highest_threshold and node.state == 'deactive' \
            #     and graph.one_threshold_deactive_neighbor(node) >= .3 * node.threshold\
            #     and player_token >= node.threshold:
            if node.state == 'deactive' and player_token >= node.threshold:
                score += 1 + graph.one_threshold_deactive_neighbor(node)  # ### 1 because of the node
    elif player == 'red':
        for node in [graph.vertices[id] for id in authority_node]:
            # if node.threshold >= .6 * highest_threshold and node.state == 'deactive' \
            #         and graph.one_threshold_deactive_neighbor(node) >= .5 * node.threshold\
            #         and player_token >= node.threshold:
            if node.state == 'deactive' and player_token >= node.threshold:
                score += 1 + graph.one_threshold_deactive_neighbor(node)   # ### 1 because of the node
    # print(score)
    return score

# ################################################### mobility _ heuristic #############################################


# def mobility_heuristic(graph, player):
#     mobility_score = 0
#     for node in graph.vertices:
#         mobility_score += mobility_score_for_vertex(node, player)
#     return mobility_score
#
#
# def mobility_score_for_vertex(node, player):
#     score = 1.00
#     if player == 'black':
#         if node.is_node_token_epmty():
#             score = 1.00
#         if node.blacktoken - node.redtoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             score = 1.00
#         if node.redtoken - node.blacktoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             score = 1.00
#         if node.redtoken > node.blacktoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             score = 0
#         if node.blacktoken > node.redtoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             score = 1.00
#         if node.redtoken - node.blacktoken >= 2 and node.is_going_to_explode():
#             score = 0
#         if node.blacktoken - node.redtoken >= 2 and node.is_going_to_explode():
#             score = 1.00
#         if node.redtoken == node.blacktoken and node.is_going_to_explode():  # odd threshold
#             score = 1.00
#         if node.blacktoken - node.redtoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             score = 1.00
#         if node.redtoken - node.blacktoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             score = 0
#
#     elif player == 'red':
#         if node.is_node_token_epmty():
#             score = 1.00
#         if node.blacktoken - node.redtoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             score = 1
#         if node.redtoken - node.blacktoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             score = 1.00
#         if node.redtoken > node.blacktoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             score = 1.00
#         if node.blacktoken > node.redtoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             score = 0
#         if node.redtoken - node.blacktoken >= 2 and node.is_going_to_explode():
#             score = 1.00
#         if node.blacktoken - node.redtoken >= 2 and node.is_going_to_explode():
#             score = 0
#         if node.redtoken == node.blacktoken and node.is_going_to_explode():  # odd threshold
#             score = 1.00
#         if node.blacktoken - node.redtoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             score = 0
#         if node.redtoken - node.blacktoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             score = 1.00
#
#     return score
#
# # ################################################### stability _ heuristic ##########################################
#
#
# def stability_heuristic(graph, player):
#     maxStabilityScore = 0
#     minStabilityScore = 0
#     maxStabilityScore = evaluate_stability_heuristic_for_player(graph, player)  # current
#     if player == 'black':
#         minStabilityScore = evaluate_stability_heuristic_for_player(graph, 'red')  # opponent
#     elif player == 'red':
#         minStabilityScore = evaluate_stability_heuristic_for_player(graph, 'black')  # opponent
#     if maxStabilityScore + minStabilityScore != 0:
#         stability_score = 100 * (maxStabilityScore - minStabilityScore) / (maxStabilityScore + minStabilityScore)
#     else:
#         stability_score = 0
#     return stability_score
#
#
# def evaluate_stability_heuristic_for_player(graph, player):
#     score = 0
#     for node in graph.vertices:
#         score += stability_score_for_vertex(node, player)
#     return score
#
#
# def stability_score_for_vertex(node, player):
#     score = 0
#     if player == 'black':
#         if node.is_node_token_epmty():
#             score = 0
#         if node.blacktoken - node.redtoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             score = node.blacktoken * 1.00
#         if node.redtoken - node.blacktoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             score = node.blacktoken * -1.00
#         if node.redtoken > node.blacktoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             score = node.blacktoken * -1.00
#         if node.blacktoken > node.redtoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             score += node.blacktoken * 1.00
#         if node.redtoken - node.blacktoken >= 2 and node.is_going_to_explode():
#             score = node.blacktoken * -1.00
#         if node.blacktoken - node.redtoken >= 2 and node.is_going_to_explode():
#             score = node.blacktoken * 1.00
#         if node.redtoken == node.blacktoken and node.is_going_to_explode():  # odd threshold
#             score = node.blacktoken * 1.00
#         if node.blacktoken - node.redtoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             score = node.blacktoken * 1.00
#         if node.redtoken - node.blacktoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             score = node.blacktoken * -1.00
#
#     elif player == 'red':
#         if node.is_node_token_epmty():
#             score = 0
#         if node.blacktoken - node.redtoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             score = node.redtoken * -1.00
#         if node.redtoken - node.blacktoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             score = node.redtoken * 1.00
#         if node.redtoken > node.blacktoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             score = node.redtoken * 1.00
#         if node.blacktoken > node.redtoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             score = node.redtoken * -1.00
#         if node.redtoken - node.blacktoken >= 2 and node.is_going_to_explode():
#             score = node.redtoken * 1.00
#         if node.blacktoken - node.redtoken >= 2 and node.is_going_to_explode():
#             score = node.redtoken * -1.00
#         if node.redtoken == node.blacktoken and node.is_going_to_explode():  # odd threshold
#             score = node.redtoken * 1.00
#         if node.blacktoken - node.redtoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             score = node.redtoken * -1.00
#         if node.redtoken - node.blacktoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             score = node.redtoken * 1.00
#
#     return score
#
# ################################################### general _ heuristic #############################################
#
#
# def general_heuristic(graph, player):
#     remaining_factor = []
#     highest_threshold = find_the_highest_threshold(graph)
#     # print('highest threshold:', highest_threshold)
#     exponent = highest_threshold - 2
#     remaining_factor.append(0)  # 0 for the first element
#     for i in range(1, highest_threshold, 1):
#         remaining_factor.append(2 ** exponent)
#         exponent -= 1
#     # print('highest threshold:', highest_threshold, 'remainig factor:', remaining_factor)
#     general_score = evaluate_general_heuristic(graph, remaining_factor, player)
#     return general_score
#
#
# def find_the_highest_threshold(graph):
#     max_thrs = 0
#     for node in graph.vertices:
#         if node.threshold > max_thrs:
#             max_thrs = node.threshold
#
#     return max_thrs
#
#
# def evaluate_general_heuristic(graph, remaining_factor, player):
#     counting_factor = 3
#     total_score = 0
#     remain_to_explode_score = 0
#     total_score = total_score + count_vertices_with_majority(graph, player) * counting_factor
#     for node in graph.vertices:
#         if player == 'red':
#             if node.redtoken - node.blacktoken > (node.threshold - (node.redtoken + node.blacktoken)):
#                 who = 1
#             elif node.blacktoken - node.redtoken > (node.threshold - (node.redtoken + node.blacktoken)):
#                 who = -1
#             else:
#                 who = 0
#         elif player == 'black':
#             if node.blacktoken - node.redtoken > (node.threshold - (node.redtoken + node.blacktoken)):
#                 who = 1
#             elif node.redtoken - node.blacktoken > (node.threshold - (node.redtoken + node.blacktoken)):
#                 who = -1
#             else:
#                 who = 0
#         if who == 1:
#             remain_this_vertex = node.threshold - (node.redtoken + node.blacktoken)
#             if remain_this_vertex < 0:
#                 remain_this_vertex = 0
#                 # ######### I add this myself #######
#             # elif remain_this_vertex == node.threshold:
#             #     remain_this_vertex -= 1
#                 ##############################
#             # print('remain_this_vertex:', remain_this_vertex, 'remaining_factor', remaining_factor)
#             remain_to_explode_score = remain_to_explode_score + int(remaining_factor[remain_this_vertex]) * who
#     total_score = total_score + remain_to_explode_score
#     return total_score


# def count_vertices_with_majority(graph, player):
#     blacknodes = 0
#     rednodes = 0
#     for node in graph.vertices:
#         if node.blacktoken > node.redtoken:
#             blacknodes += 1
#         elif node.redtoken > node.blacktoken:
#             rednodes += 1
#     if player == 'red':
#         count = rednodes
#     elif player == 'black':
#         count = blacknodes
#     return count

# ################################################### hubs _ heuristic ################################################


# def hubs_heuristic(graph, player):
#
#     pagerank = set.pagerank()  # pagerank is a dictionary (keys = node.id , values = pagerank of each node)
#     hubs_score = 0
#     node_num = set.num_of_nodes
#     scores = dict()
#     pagerank = sorted(pagerank.items(), key=lambda kv: (kv[1], kv[0]))  # now majority convert to a list
#     # convert to dictionary and sort on descending order
#     pagerank = dict(list(reversed(pagerank)))
#     top_nodes_number = round(.2 * node_num)
#     top_nodes_sort_by_pagerank = {k: pagerank[k] for k in list(pagerank)[:top_nodes_number]} # it's still a dictionary
#     list_keys = [k for k in top_nodes_sort_by_pagerank]
#
#     for node in graph.vertices:
#         score = hubs_score_for_vertex(node, player)
#         hubs_score += score
#         if node.id in list_keys:
#             if score == pagerank[node.id]:
#                 hubs_score += pagerank[node.id] * node.threshold
#
#     return hubs_score


# def hubs_score_for_vertex(node, player):
#     pagerank = set.pagerank()
#     hubs_score = 0
#     if player == 'black':
#
#         if node.is_node_token_epmty():
#             hubs_score = 0
#         if node.blacktoken - node.redtoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             hubs_score = pagerank[node.id]
#         if node.redtoken - node.blacktoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             hubs_score = 1.00 * pagerank[node.id]
#         if node.redtoken > node.blacktoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             hubs_score = 0
#         if node.blacktoken > node.redtoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             hubs_score += pagerank[node.id]
#         if node.redtoken - node.blacktoken >= 2 and node.is_going_to_explode():
#             hubs_score = 0
#         if node.blacktoken - node.redtoken >= 2 and node.is_going_to_explode():
#             hubs_score = pagerank[node.id]
#         if node.redtoken == node.blacktoken and node.is_going_to_explode():  # odd threshold
#             hubs_score = pagerank[node.id]
#         if node.blacktoken - node.redtoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             hubs_score = pagerank[node.id]
#         if node.redtoken - node.blacktoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             hubs_score = 0
#
#     if player == 'red':
#
#         if node.is_node_token_epmty():
#             hubs_score = 0
#         if node.blacktoken - node.redtoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             hubs_score = 1.00 * pagerank[node.id]
#         if node.redtoken - node.blacktoken == 1 and node.is_going_to_explode() and node.is_even(node.threshold):
#             hubs_score = pagerank[node.id]
#         if node.redtoken > node.blacktoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             hubs_score = pagerank[node.id]
#         if node.blacktoken > node.redtoken and node.is_going_to_explode() and node.is_odd(node.threshold):
#             hubs_score = 0
#         if node.redtoken - node.blacktoken >= 2 and node.is_going_to_explode():
#             hubs_score = pagerank[node.id]
#         if node.blacktoken - node.redtoken >= 2 and node.is_going_to_explode():
#             hubs_score = 0
#         if node.redtoken == node.blacktoken and node.is_going_to_explode():  # odd threshold
#             hubs_score = pagerank[node.id]
#         if node.blacktoken - node.redtoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             hubs_score = 0
#         if node.redtoken - node.blacktoken > (node.threshold - (node.blacktoken + node.redtoken)):
#             hubs_score = pagerank[node.id]
#     return hubs_score


def linear_combination(graph, player, player_token):
    # alpha = .65
    # beta = .15
    # gamma = .2
    alpha = 1
    beta = 0
    gamma = 0
    delta = .1
    weight = [0.27, -0.08, 0, 0.315, .0495]
    # lc_score = weight[0]*paper_parity_heuristic(graph, player) + weight[1]*stability_heuristic(graph, player) + weight
    # [2]*mobility_heuristic() + weight[3]*hubs_heuristic(graph, player) + weight[4]*general_heuristic(graph, player)
    # print(paper_parity_heuristic(graph, player))
    # print('par', parity_heuristic(graph, player))
    # print('maj', majority_token(graph, player))
    # print('hub', hubs_with_weak_neighbor(graph, player, player_token))

    lc_score = alpha*parity_heuristic(graph, player)
               # beta*hubs_with_weak_neighbor(graph, player, player_token) +\
               # gamma*majority_token(graph, player)
    # lc_score = alpha * paper_parity_heuristic(graph, player) + beta * stability_heuristic(graph, player) + \
    # gamma * mobility_heuristic(graph, player) + delta * hubs_heuristic(graph, player)

    return lc_score

