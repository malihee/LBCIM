from vertex import Vertex
import networkx as nx
import copy
import random
from player import Player
import numpy as np


class Graph:
    # is_in_exploding_loop= False  # this is for checking that if graph is in exploding loop or not

    def __init__(self, vertices, edges, is_in_exploding_loop):
        self.vertices = vertices
        self.edges = edges
        self.is_in_exploding_loop = is_in_exploding_loop

    # return a list of all the positions one can catch from the current graph's positions
    def next_position_of_graph(self, player, player_remaining_token):
        import setting as set
        next_position = []
        global token_capacity
        # if set.type_of_game == 'zero_loyalty_variant':
        #     # global is_in_exploding_loop
        #
        #     if player == 'red':
        #         for position in range(len(self.vertices)):
        #             counter = 0
        #             graph = copy.deepcopy(self)
        #             # graph.is_in_exploding_loop = False
        #             # graph = Graph(self.vertices, self.edges)
        #             graph.vertices[position].redtoken = 1
        #
        #             if graph.vertices[position].ready_to_explode():
        #                 graph.vertices[position].explode()
        #                 graph.diffusion(graph.vertices[position])
        #                 # to check if it is in loop we define a new variable called this_node which keeps the node_
        #                 # id of the main node
        #                 node_id = graph.vertices[position].id
        #                 # print('node id :', node_id)
        #
        #                 (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #
        #                 while cond:
        #
        #                     for node in exploding_nodes:
        #                         if node.id == node_id:
        #                             # r, b = graph.token_num_in_graph()
        #                             # print(r, b)
        #                             counter += 1
        #                             if graph.is_one_color_token() and counter > 10:
        #                                 print('it is one color token')
        #                                 graph.is_in_exploding_loop = True
        #                                 break
        #                             if counter > 10:
        #                                 r, b = graph.token_num_in_graph()
        #                                 # print(r, b)
        #                             if counter == 100:
        #                                 graph.is_in_exploding_loop = True
        #                                 # print('it is in loop')
        #                                 break
        #
        #                         node.explode()
        #                         graph.diffusion(node)
        #                     (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #
        #                     if graph.is_in_exploding_loop or graph.is_one_color_token():
        #
        #                         break
        #
        #             next_position.append(graph)
        #
        #     elif player == 'black':
        #         for position in range(len(self.vertices)):
        #             counter = 0
        #             graph = copy.deepcopy(self)
        #             # graph.is_in_exploding_loop = False
        #             graph.vertices[position].blacktoken = 1
        #             if graph.vertices[position].ready_to_explode():
        #                 graph.vertices[position].explode()
        #                 graph.diffusion(graph.vertices[position])
        #
        #                 # to check if it is in loop we define a new variable called this_node which keeps the node_id
        #                 # of the main node
        #                 node_id = graph.vertices[position].id
        #
        #                 (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #                 r, b = graph.token_num_in_graph()
        #                 while cond:
        #                     for node in exploding_nodes:
        #                         if node.id == node_id:
        #                             counter += 1
        #                             if graph.is_one_color_token() and counter > 10:  # and r + b > 3:
        #                                 print('it is one color token')
        #                                 graph.is_in_exploding_loop = True
        #                                 break
        #
        #                             if counter == 100:
        #                                 graph.is_in_exploding_loop = True
        #                                 # print('it is in loop')
        #                                 break
        #                         node.explode()
        #                         graph.diffusion(node)
        #                     (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #                     if graph.is_in_exploding_loop or graph.is_one_color_token():
        #                         break
        #             next_position.append(graph)
        #     return next_position
        #
        # elif set.type_of_game == 'full_loyalty_variant':
        #
        #     if player == 'red':
        #         deactive_nodes, num_of_deactive_nodes = self.deactive_nodes()
        #         for node in deactive_nodes:
        #             graph = copy.deepcopy(self)
        #             for v in graph.vertices:
        #                 if v.id == node.id:
        #                     v.redtoken = 1
        #                     break
        #             if graph.vertices[node.id].ready_to_explode():
        #                 graph.vertices[node.id].explode()
        #                 graph.diffusion(graph.vertices[node.id])
        #
        #                 (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #
        #                 while cond:
        #                     for v in exploding_nodes:
        #                         v.explode()
        #                         graph.diffusion(v)
        #                     (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #             next_position.append(graph)
        #
        #     elif player == 'black':
        #         deactive_nodes, num_of_deactive_nodes = self.deactive_nodes()
        #         for node in deactive_nodes:
        #             graph = copy.deepcopy(self)
        #             for v in graph.vertices:
        #                 if v.id == node.id:
        #                     v.blacktoken = 1
        #                     break
        #             if graph.vertices[node.id].ready_to_explode():
        #                 graph.vertices[node.id].explode()
        #                 graph.diffusion(graph.vertices[node.id])
        #
        #                 (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #
        #                 while cond:
        #                     for v in exploding_nodes:
        #                         v.explode()
        #                         graph.diffusion(v)
        #                     (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #             next_position.append(graph)
        #     return next_position
        #
        # elif set.type_of_game == 'full_loyalty_more_token':
        #     import MCTS as mc
        #     if set.flmt_strategy == 'naive':
        #         token_capacity = []
        #         if player == 'red':
        #             deactive_nodes, num_of_deactive_nodes = self.deactive_nodes()
        #             for node in deactive_nodes:
        #                 graph = copy.deepcopy(self)
        #                 for v in graph.vertices:
        #                     if v.id == node.id:
        #                         if mc.flag:
        #                             v.redtoken = 1
        #                             token_capacity.append(1)
        #                         else:
        #                             node_token_capacity = node.threshold - (node.blacktoken + node.redtoken)
        #                             v.redtoken = node_token_capacity
        #                             token_capacity.append(node_token_capacity)
        #                         break
        #                 if graph.vertices[node.id].ready_to_explode():
        #                     graph.vertices[node.id].explode()
        #                     graph.diffusion(graph.vertices[node.id])
        #
        #                     (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #
        #                     while cond:
        #                         for v in exploding_nodes:
        #                             v.explode()
        #                             graph.diffusion(v)
        #                         (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #                 next_position.append(graph)
        #
        #         elif player == 'black':
        #             deactive_nodes, num_of_deactive_nodes = self.deactive_nodes()
        #             for node in deactive_nodes:
        #                 graph = copy.deepcopy(self)
        #                 for v in graph.vertices:
        #                     if v.id == node.id:
        #                         if mc.flag:
        #                             v.blacktoken = 1
        #                             token_capacity.append(1)
        #                         else:
        #                             node_token_capacity = node.threshold - (node.blacktoken + node.redtoken)
        #                             v.blacktoken = node_token_capacity
        #                             token_capacity.append(node_token_capacity)
        #                         break
        #                 if graph.vertices[node.id].ready_to_explode():
        #                     graph.vertices[node.id].explode()
        #                     graph.diffusion(graph.vertices[node.id])
        #
        #                     (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #
        #                     while cond:
        #                         for v in exploding_nodes:
        #                             v.explode()
        #                             graph.diffusion(v)
        #                         (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #                 next_position.append(graph)
        #         return next_position, token_capacity
        #
        #     elif set.flmt_strategy == 'advanced':
        #         token_capacity = []
        #         if player == 'red':
        #             deactive_nodes, num_of_deactive_nodes = self.deactive_nodes()
        #             for node in deactive_nodes:
        #                 node_token_capacity = node.threshold - (node.blacktoken + node.redtoken)
        #                 for token_num in range(min(node_token_capacity, player_remaining_token)):
        #                     graph = copy.deepcopy(self)
        #                     for v in graph.vertices:
        #                         if v.id == node.id:
        #                             v.redtoken = token_num + 1
        #                             token_capacity.append(token_num + 1)
        #                             break
        #                     if graph.vertices[node.id].ready_to_explode():
        #                         graph.vertices[node.id].explode()
        #                         graph.diffusion(graph.vertices[node.id])
        #
        #                         (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #
        #                         while cond:
        #                             for v in exploding_nodes:
        #                                 v.explode()
        #                                 graph.diffusion(v)
        #                             (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #                     next_position.append(graph)
        #
        #         elif player == 'black':
        #             deactive_nodes, num_of_deactive_nodes = self.deactive_nodes()
        #             for node in deactive_nodes:
        #                 node_token_capacity = node.threshold - (node.blacktoken + node.redtoken)
        #                 for token_num in range(min(player_remaining_token, node_token_capacity)):
        #                     graph = copy.deepcopy(self)
        #                     for v in graph.vertices:
        #                         if v.id == node.id:
        #                             v.blacktoken = token_num + 1
        #                             token_capacity.append(token_num + 1)
        #                             break
        #                     if graph.vertices[node.id].ready_to_explode():
        #                         graph.vertices[node.id].explode()
        #                         graph.diffusion(graph.vertices[node.id])
        #
        #                         (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #
        #                         while cond:
        #                             for v in exploding_nodes:
        #                                 v.explode()
        #                                 graph.diffusion(v)
        #                             (cond, exploding_nodes) = graph.any_node_to_explode(player)
        #                     next_position.append(graph)
        #         return next_position, token_capacity
        if set.type_of_game == 'harder_reactivation':
            # print('nextp 264')
            import MCTS as mc
            # global token_capacity
            if set.hra_strategy == 'naive':
                # print('next p 268')
                token_capacity = []
                if player == 'red':
                    # print('nextp 271')
                    nodes = self.deactive_opposite_nodes(player)
                    for node in nodes:
                        graph = copy.deepcopy(self)
                        if set.current_player.approach != 'dummy' and set.current_player.approach != 'maximum_threshold' and\
                            set.current_player.approach != 'minimum_threshold' and mc.flag:
                            graph.vertices[node.id].redtoken = 1
                            token_capacity.append(1)
                        else:
                            node_token_capacity = node.threshold - (node.blacktoken + node.redtoken)
                            graph.vertices[node.id].redtoken = node_token_capacity
                            token_capacity.append(node_token_capacity)
                        # print('next p 282')

                        if graph.vertices[node.id].ready_to_explode():
                            graph.vertices[node.id].explode()
                            graph.diffusion(graph.vertices[node.id])
                            # print('next p 288')

                            (cond, exploding_nodes) = graph.any_node_to_explode(player)
                            # print('next p 291')
                            # print('len en', len(exploding_nodes), 'node id :', exploding_nodes[0].id)

                            while cond:
                                # print('len expn', len(exploding_nodes), 'node id :', exploding_nodes[0].id)
                                for v in exploding_nodes:
                                    # print('296')
                                    v.explode()
                                    # print('48')
                                    graph.diffusion(v)
                                    # print('hi')
                                (cond, exploding_nodes) = graph.any_node_to_explode(player)

                            # print('next p 296')

                        next_position.append(graph)
                    #     print('304')
                    # print('after for')

                elif player == 'black':

                    nodes = self.deactive_opposite_nodes(player)
                    for node in nodes:
                        graph = copy.deepcopy(self)

                        if mc.flag:
                            graph.vertices[node.id].blacktoken = 1
                            token_capacity.append(1)
                        else:
                            node_token_capacity = node.threshold - (node.blacktoken + node.redtoken)
                            graph.vertices[node.id].blacktoken = node_token_capacity
                            token_capacity.append(node_token_capacity)

                        if graph.vertices[node.id].ready_to_explode():
                            graph.vertices[node.id].explode()
                            graph.diffusion(graph.vertices[node.id])

                            (cond, exploding_nodes) = graph.any_node_to_explode(player)

                            while cond:
                                # print('black len expn', len(exploding_nodes), 'node id :', exploding_nodes[0].id)
                                for v in exploding_nodes:
                                    # print('332')
                                    v.explode()
                                    # print('334')
                                    graph.diffusion(v)
                                    # print('bye')
                                (cond, exploding_nodes) = graph.any_node_to_explode(player)
                                # print('331')
                        next_position.append(graph)
                #         print('334')
                #     print('after for')
                # print('end of nextp')
                return next_position, token_capacity

    # check if there is any node in graph which is ready to explode
    # if there is any node return a list of nodes with the order mentioned in paper
    # return a boolean value and a list of nodes
    def any_node_to_explode(self, player):
        import setting as set
        if set.type_of_game == 'zero_loyalty_variant':
            flag = False
            exploding_nodes = []
            ordered_exp_node = []
            majority = dict()
            for node in self.vertices:
                if node.ready_to_explode():
                    flag = True
                    exploding_nodes.append(node)  # it is unordered
                    if player == 'black':
                        majority[node.id] = node.blacktoken - node.redtoken
                    elif player == 'red':
                        majority[node.id] = node.redtoken - node.blacktoken
            # sort the dictionary by the value in ascending order
            majority = sorted(majority.items(), key=lambda kv: (kv[1], kv[0]))  # now majority convert to a list
            # convert to dictionary and sort on descending order
            # refer to explosion order in paper
            majority = dict(list(reversed(majority)))
            for node_id in majority.keys():
                for node in exploding_nodes:
                    if node_id == node.id:
                        ordered_exp_node.append(node)
            if flag:
                return True, ordered_exp_node

            else:
                return False, ordered_exp_node

        elif set.type_of_game == 'full_loyalty_variant' or set.type_of_game == 'full_loyalty_more_token' or set.type_of_game == 'harder_reactivation':
            # print('in explode')

            flag = False
            exploding_nodes = []
            ordered_exp_node = []
            majority = dict()
            for node in self.vertices:
                if node.state == 'deactive' or node.state != player:
                    if node.ready_to_explode():
                        flag = True
                        exploding_nodes.append(node)  # it is unordered
                        if player == 'black':
                            majority[node.id] = node.blacktoken - node.redtoken
                        elif player == 'red':
                            majority[node.id] = node.redtoken - node.blacktoken

            # sort the dictionary by the value in ascending order
            majority = sorted(majority.items(), key=lambda kv: (kv[1], kv[0]))  # now majority convert to a list
            # convert to dictionary and sort on descending order
            # refer to explosion order in paper
            majority = dict(list(reversed(majority)))
            for node_id in majority.keys():
                for node in exploding_nodes:
                    if node_id == node.id:
                        ordered_exp_node.append(node)
            # print('396')

            if flag:
                return True, ordered_exp_node
            else:
                return False, ordered_exp_node

        # elif set.type_of_game == 'different_loyalty_variant':
        #     # if set.dlv_strategy == 'naive':
        #         flag = False
        #         exploding_nodes = []
        #         ordered_exp_node = []
        #         majority = dict()
        #         for node in self.vertices:
        #             if node.ready_to_explode():
        #                 if node.state == 'deactive' or not(node.state == player):  # this line should be commented because in advance_dlv_diffusion
        #                                 # there might be an active node which takes token from its diffusing neighbor
        #                     flag = True
        #                     exploding_nodes.append(node)  # it is unordered
        #                     if player == 'black':
        #                         majority[node.id] = node.blacktoken - node.redtoken
        #                     elif player == 'red':
        #                         majority[node.id] = node.redtoken - node.blacktoken
        #
        #         # sort the dictionary by the value in ascending order
        #         majority = sorted(majority.items(), key=lambda kv: (kv[1], kv[0]))  # now majority convert to a list
        #         # convert to dictionary and sort on descending order
        #         # refer to explosion order in paper
        #         majority = dict(list(reversed(majority)))
        #         for node_id in majority.keys():
        #             for node in exploding_nodes:
        #                 if node_id == node.id:
        #                     ordered_exp_node.append(node)
        #         if flag:
        #             return True, ordered_exp_node
        #         else:
        #             return False, ordered_exp_node
            # elif set.dlv_strategy == 'advanced':
            #
            #     return

    def is_one_color_token(self):
        red, black = self.token_num_in_graph()
        if (red == 0 and black > 0) or (black == 0 and red > 0):
            return True
        else:
            return False

    # determine the winner of game
    def determine_winner(self):
        import setting as set
        if set.type_of_game == 'zero_loyalty_variant':
            red, black = self.token_num_in_graph()

            if self.is_in_exploding_loop:
                if red == 0 and black > 0:
                    return True, 'black'
                elif black == 0 and red > 0:
                    return True, 'red'
                else:
                    return True, None
            else:
                if red > black:
                    return True, 'red'
                elif black > red:
                    return True, 'black'
                else:
                    return True, None
        elif set.type_of_game == 'full_loyalty_variant' or set.type_of_game == 'full_loyalty_more_token' or set.type_of_game == 'harder_reactivation':
            red = 0
            black = 0
            for node in self.vertices:
                if node.state == 'red':
                    red += 1
                elif node.state == 'black':
                    black += 1
            if red > black:
                return True, 'red'
            elif black > red:
                return True, 'black'
            elif red == black:
                return True, None

        # elif set.type_of_game == 'different_loyalty_variant' :
        #     if set.dlv_strategy == 'naive':
        #         red = 0
        #         black = 0
        #         for node in self.vertices:
        #             if node.state == 'red':
        #                 red += 1
        #             elif node.state == 'black':
        #                 black += 1
        #         if red > black:
        #             return True, 'red'
        #         elif black > red:
        #             return True, 'black'
        #         else:
        #             return True, None
        #     elif set.dlv_strategy == 'advanced':
        #         red = 0
        #         black = 0
        #         for node in self.vertices:
        #             if node.state == 'red':
        #                 red += 1
        #             elif node.state == 'black':
        #                 black += 1
        #         if red > black:
        #             return True, 'red'
        #         elif black > red:
        #             return True, 'black'
        #         else:
        #             red, black = self.token_num_in_graph()
        #             if red > black:
        #                 return True, 'red'
        #             elif black > red:
        #                 return True, 'black'
        #             else:
        #                 return True, None

    # return the number of node in graph
    def node_number(self):
        return len(self.vertices)

    # return the number of edges in graph
    def edge_number(self):
        return len(self.edges)

    # return deactive nodes and the number of them
    def deactive_nodes(self):

        deactive_nodes = []
        counter = 0
        for node in self.vertices:
            if node.state == 'deactive':
                deactive_nodes.append(node)
                counter += 1
        return deactive_nodes, counter

    # return the state (deactive/red/black) of nodes
    def nodes_state(self):
        # nodes_state = dict()
        # for node in self.vertices:
        #     nodes_state[node.id] = node.state
        red_nodes = 0
        black_nodes = 0
        deactive_nodes = 0
        for node in self.vertices:
            if node.state == 'red':
                red_nodes += 1
            elif node.state == 'black':
                black_nodes += 1
            elif node.state == 'deactive':
                deactive_nodes += 1

        return red_nodes, black_nodes, deactive_nodes

    # return the nodes with opposite party or deactive ones(used for advanced different loyalty variant)
    def deactive_opposite_nodes(self, player):
        nodes = []
        for node in self.vertices:
            if player == 'black':
                if node.state == 'red' or node.state == 'deactive':
                    nodes.append(node)
            elif player == 'red':
                if node.state == 'black' or node.state == 'deactive':
                    nodes.append(node)
        return nodes

    def one_threshold_deactive_neighbor(self, node):
        weak_neighbor = 0
        for n in node.neighbors:
            if (self.vertices[n].threshold == 1 and self.vertices[n].state == 'deactive') or (
                    self.vertices[n].threshold == 2 and self.vertices[n].state == 'deactive' and
                    self.vertices[n].total_token == 1):
                weak_neighbor += 1

        return weak_neighbor

    def nodes(self):
        red_nodes = []
        black_nodes = []
        deactive_nodes = []
        for node in self.vertices:
            if node.state == 'red':
                red_nodes.append(node)
            elif node.state == 'black':
                black_nodes.append(node)
            elif node.state == 'deactive':
                deactive_nodes.append(node)

        return red_nodes, black_nodes, deactive_nodes

    # return the number of red and black tokens in graph
    def token_num_in_graph(self):
        red_tokens = 0
        black_tokens = 0
        for node in self.vertices:
            black_tokens += node.black_token
            red_tokens += node.red_token
        return red_tokens, black_tokens

    # return a dictionary (keys = node.id, value = number of black token of that node)
    def nodes_with_black_tokens(self):
        nodes_with_black_tokens = dict()
        for node in self.vertices:
            if node.state == 'deactive':
                if node.blacktoken > 0:
                    nodes_with_black_tokens[node.id] = node.blacktoken
        return nodes_with_black_tokens

    # return a dictionary (keys = node.id, value = number of red token of that node)
    def nodes_with_red_tokens(self):
        nodes_with_red_tokens = dict()
        for node in self.vertices:
            if node.state == 'deactive':
                if node.redtoken > 0:
                    nodes_with_red_tokens[node.id] = node.redtoken
        return nodes_with_red_tokens

    # return a list of node's neighbors
    def get_neighbors(self, node):
        neighbors = []
        for neighbor in node.neighbors:
            for node in self.vertices:
                if node.id == neighbor:
                    neighbors.append(node)
                    break
        return neighbors

    # diffuse the tokens of fired node among its neighbors
    # input : the diffusing fired node
    def diffusion(self, node):

        import setting as set
        neighbors = self.get_neighbors(node)
        # if set.type_of_game == 'zero_loyalty_variant':
        #     if node.ready_to_explode():
        #         for neighbor in neighbors:
        #             node.token_diffusion_to_neighbors(neighbor)
        #     else:
        #         raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                         " node is not ready to explode")
        #
        #     if node.redtoken + node.blacktoken == 0:
        #         self.node_loyalty_variant(node)
        #     elif node.redtoken + node.blacktoken < 0:
        #         raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                         " after diffusion, node's tokens are less than 0 ")
        #
        #     elif node.redtoken + node.blacktoken > 0:
        #         raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                         " after diffusion, node's tokens are more than 0 ")
        # elif set.type_of_game == 'full_loyalty_variant' or set.type_of_game == 'full_loyalty_more_token':
        #     if node.ready_to_explode():
        #         for neighbor in neighbors:
        #             node.token_diffusion_to_neighbors(neighbor)
        #         self.node_loyalty_variant(node)
        #     else:
        #         raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                         " node is not ready to explode")
        #
        #     if node.redtoken + node.blacktoken < 0:
        #         raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                         " after diffusion, node's tokens are less than 0 ")
        # elif set.type_of_game == 'different_loyalty_variant':
        #     if set.dlv_strategy == 'naive':
        #         if node.ready_to_explode():
        #             for neighbor in neighbors:
        #                 node.token_diffusion_to_neighbors(neighbor)
        #             self.node_loyalty_variant(node)
        #         else:
        #             raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                             " node is not ready to explode")
        #
        #         if node.redtoken + node.blacktoken < 0:
        #             raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                             " after diffusion, node's tokens are less than 0 ")
        #     elif set.dlv_strategy == 'advanced':
        #         if node.ready_to_explode():
        #             if dlv_flag_neighbors:
        #                 if node.state != 'deactive':
        #                     for neighbor in neighbors:
        #                         node.advanced_dlv_diffusion(neighbor)
        #                     # self.node_loyalty_variant(node)
        #                 else:
        #                     raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                                     "defussing node is deactive (final step)")
        #             else:
        #                 if node.state != 'deactive':
        #                     for neighbor in neighbors:
        #                         node.token_diffusion_to_neighbors(neighbor)
        #                 else:
        #                     raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                                     "defussing node is deactive (in tree)")
        #
        #         else:
        #             raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                             " node is not ready to explode")
        #
        #         if node.redtoken + node.blacktoken < 0:
        #             raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
        #                             " after diffusion, node's tokens are less than 0 ")
        if set.type_of_game == 'harder_reactivation':
            increase_threshold_num = np.ceil(node.degree/4)  # node degree affects on the amount of threshold increasin
            # print('a')
            if set.hra_strategy == 'naive':
                # print('b')
                if node.ready_to_explode():
                    # print('c')
                    if node.state != 'deactive':
                        token_diffusion_num, eligible_neighbor, sort_idx = node.calculate_number_of_diffusing_tokens(neighbors)
                        if len(eligible_neighbor) > 0:
                        # print('cc')
                            for idx in sort_idx:
                                # print('d')
                                node.token_diffusion_to_neighbors(eligible_neighbor[idx], token_diffusion_num[idx])
                        else:
                            # burn the token
                            node.blacktoken = 0
                            node.redtoken = 0
                            # print('e')
                        # increase node's threshold after diffusing
                        node.inc_threshold = increase_threshold_num
                        # print('f')
                    else:
                        raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
                                        "defussing node is deactive (in tree)")
                else:
                    raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
                                    " node is not ready to explode")
                if node.redtoken + node.blacktoken < 0:
                    raise TypeError("Maliheeee!!!class: Graph ,function: diffusion,"
                                    " after diffusion, node's tokens are less than 0 ")

    # for zero loyalty games this function sets the node.state == deactive after diffusion
    # and for full loyalty game dont change the state ofd node after diffusion

    # def node_loyalty_variant(self, node):
    #     import setting as set
    #     # if node.blacktoken + node.redtoken == 0:
    #     if set.type_of_game == 'zero_loyalty_variant':
    #         node.state = 'deactive'
    #         if node.redtoken + node.blacktoken < 0:
    #             raise TypeError("Maliheeee!!!class: Graph ,function: node_loyalty_variant"
    #                             " after diffusion, node's tokens are less than 0 ")
    #         elif node.redtoken + node.blacktoken > 0:
    #             raise TypeError("Maliheeee!!!class: Graph ,function: node_loyalty_variant"
    #                             " after diffusion, node's tokens are more than 0 ")
    #
    #     elif set.type_of_game == 'full_loyalty_variant' or set.type_of_game == 'full_loyalty_more_token':
    #         if node.redtoken + node.blacktoken < 0:
    #             raise TypeError("Maliheeee!!!class: Graph ,function: node_loyalty_variant"
    #                             " after diffusion, node's tokens are less than 0 ")
    #         if node.state == 'deactive':
    #             raise TypeError("Maliheeee!!!class: Graph ,function: node_loyalty_variant"
    #                             "node is deactive ")
    #         return
    #
    #     # elif set.type_of_game == 'different_loyalty_variant':
    #     #
    #     #     if set.dlv_strategy == 'naive':
    #     #         rand = random.uniform(0, 1)
    #     #         if rand > node.loyalty:
    #     #             node.state = 'deactive'
    #     #         else:
    #     #             if node.redtoken + node.blacktoken < 0:
    #     #                 raise TypeError("Maliheeee!!!class: Graph ,function: node_loyalty_variant"
    #     #                                 " after diffusion, node's tokens are less than 0 ")
    #     #             return
    #     #
    #     #     elif set.dlv_strategy == 'advanced':
    #     #         red, black, deactive = self.nodes()
    #     #         if node.state == 'black':
    #     #             for nd in red:  # opposite nodes will be tested for changing state or not
    #     #                 rand = random.uniform(0, 1)
    #     #                 nd.total = 1  # num of all chance to changing it's state will be plus one
    #     #                 if rand > nd.loyalty:
    #     #                     nd.state = 'red'
    #     #                     nd.changingstate = 1  # num of times it's changing its state
    #     #                 nd.loyalty_guess = nd.changingstate / nd.total
    #     #
    #     #         if node.state == 'red':
    #     #             for nd in black:  # opposite nodes will be tested for changing state or not
    #     #                 rand = random.uniform(0, 1)
    #     #                 nd.total = 1  # num of all chance to changing it's state will be plus one
    #     #                 if rand > nd.loyalty:
    #     #                     nd.state = 'black'
    #     #                     nd.changingstate = 1  # num of times it's changing its state
    #     #                 nd.loyalty_guess = nd.changingstate / nd.total
    #     #         if node.redtoken + node.blacktoken < 0:
    #     #             raise TypeError("Maliheeee!!!class: Graph ,function: node_loyalty_variant"
    #     #                             " after diffusion, node's tokens are less than 0 ")
    #     #         # if node.state == 'deactive':
    #     #         #     raise TypeError("Maliheeee!!!class: Graph ,function: node_loyalty_variant,"
    #     #         #                     " node is deactive ")
    #     #         return
    #
    #     elif set.type_of_game == 'harder_reactivation':
    #
    #         if set.hra_strategy == 'naive':
    #             rand = random.uniform(0, 1)
    #             if rand > node.loyalty:
    #                 node.state = 'deactive'
    #             else:
    #                 if node.redtoken + node.blacktoken < 0:
    #                     raise TypeError("Maliheeee!!!class: Graph ,function: node_loyalty_variant"
    #                                     " after diffusion, node's tokens are less than 0 ")
    #                 return


