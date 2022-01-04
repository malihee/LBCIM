import networkx as nx
import random
import numpy as np


class Vertex:

    def __init__(self, id, threshold, blacktoken, redtoken, degree, state_, neighbors, lasttoken,
                 # loyalty,experimental_loyalty, total_possible_changing_state, changing_state_num
                 ):
        self.id = id
        self.threshold = threshold
        self.black_token = blacktoken
        self.red_token = redtoken
        self.degree = degree
        self.state_ = state_
        self.neighbors = neighbors
        self.last_token = lasttoken
        return

    # node Explosion ## without diffusion
    # in this method an exploded node will change its state from inactive to RED or BLACK
    # and all of its tokens changed to the winner color
    def explode(self):
        global last_token
        if self.blacktoken + self.redtoken == self.threshold:
            if self.blacktoken > self.redtoken:
                self.state = 'black'

                if self.redtoken != 0:
                    temp = self.redtoken
                    self.redtoken = 0
                    self.blacktoken = temp

            elif self.blacktoken < self.redtoken:
                self.state = 'red'
                if self.blacktoken != 0:
                    temp = self.blacktoken
                    self.blacktoken = 0
                    self.redtoken = temp

            elif self.blacktoken == self.redtoken:
                self.state = self.lasttoken
                if self.lasttoken == 'red':
                    temp = self.blacktoken
                    self.blacktoken = 0
                    self.redtoken = temp
                elif self.lasttoken == 'black':
                    temp = self.redtoken
                    self.redtoken = 0
                    self.blacktoken = temp
        else:
            raise TypeError("Maliheeee!!class: Vertex ,function: explode()"
                            "the node is not ready to explode")

        return

    # diffusion by a node
    # in this method an exploded node give one token to one neighbor
    # in the case which the node cant give a token to a neighbor we burn this token
    def token_diffusion_to_neighbors(self, neighbor, token_diffusion_num):
        import setting as set
        if set.type_of_game == 'zero_loyalty_variant':
            if self.state == 'black':
                if self.blacktoken > 0:
                    if neighbor.ready_to_explode():
                        # burn the token
                        self.blacktoken = -1  # the case which the neighbor is fiered and is waiting for diffusion
                    else:
                        neighbor.blacktoken = 1
                        self.blacktoken = -1
                else:
                    raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion_to"
                                    "neighbors for node: ", self.id, " there are no token to diffuse")

            elif self.state == 'red':
                if self.redtoken > 0:
                    if neighbor.ready_to_explode():
                        # burn the token
                        self.redtoken = -1  # the case which the neighbor is fiered and is waiting for diffusion
                    else:
                        neighbor.redtoken = 1
                        self.redtoken = -1
                else:
                    raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion"
                                    "to_neighbors there are no token to diffuse")

            elif self.state == 'deactive':
                raise TypeError("Maliheeee!! class: Vertex ,function: token_diffusion"
                                "to_neighbors the node state is deactive")

        elif set.type_of_game == 'full_loyalty_variant' or set.type_of_game == 'full_loyalty_more_token':
            if neighbor.state == 'deactive' and not neighbor.ready_to_explode():
                if self.state == 'black':
                    if self.blacktoken > 0:
                        neighbor.blacktoken = 1
                        self.blacktoken = -1
                    else:
                        raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion_to"
                                        "neighbors for node: ", self.id, " there are no token to diffuse")

                elif self.state == 'red':
                    if self.redtoken > 0:
                        neighbor.redtoken = 1
                        self.redtoken = -1
                    else:
                        raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion"
                                        "to_neighbors there are no token to diffuse")

                elif self.state == 'deactive':
                    raise TypeError("Maliheeee!! class: Vertex ,function: token_diffusion"
                                    "to_neighbors the node state is deactive")

        elif set.type_of_game == 'different_loyalty_variant':
            if set.dlv_strategy == 'naive':
                if neighbor.state == 'deactive' and not neighbor.ready_to_explode():
                    if self.state == 'black':
                        if self.blacktoken > 0:
                            neighbor.blacktoken = 1
                            self.blacktoken = -1
                        else:
                            raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion_to"
                                            "neighbors for node: ", self.id, " there are no token to diffuse")

                    elif self.state == 'red':
                        if self.redtoken > 0:
                            neighbor.redtoken = 1
                            self.redtoken = -1
                        else:
                            raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion"
                                            "to_neighbors there are no token to diffuse")

                    elif self.state == 'deactive':
                        raise TypeError("Maliheeee!! class: Vertex ,function: token_diffusion"
                                        "to_neighbors the node state is deactive")
                else:  # in dlv we should burn the token for when the neighbor is activated before because the node may
                    # deactive after diffusion and it should be empty of tokens
                    if self.state == 'black':
                        if self.blacktoken > 0:
                            self.blacktoken = -1
                        else:
                            raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion_to"
                                            "neighbors for node: ", self.id, " there are no token to diffuse")
                    elif self.state == 'red':
                        if self.redtoken > 0:
                            self.redtoken = -1
                        else:
                            raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion_to"
                                            "neighbors for node: ", self.id, " there are no token to diffuse")

            elif set.dlv_strategy == 'advanced':
                if neighbor.state == 'deactive' and not neighbor.ready_to_explode():
                    if self.state == 'black':
                        if self.blacktoken > 0:
                            neighbor.blacktoken = 1
                            self.blacktoken = -1
                        else:
                            raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion_to"
                                            "neighbors for node: ", self.id, " there are no token to diffuse")

                    elif self.state == 'red':
                        if self.redtoken > 0:
                            neighbor.redtoken = 1
                            self.redtoken = -1
                        else:
                            raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion"
                                            "to_neighbors there are no token to diffuse")

                    elif self.state == 'deactive':
                        raise TypeError("Maliheeee!! class: Vertex ,function: token_diffusion"
                                        "to_neighbors the node state is deactive")

                elif neighbor.state == 'black' or neighbor.state == 'red':
                    if self.state == 'black':
                        if neighbor.state == 'red':
                            if self.blacktoken > 0:
                                neighbor.blacktoken = 1
                                self.blacktoken = -1
                                # if neighbor.ready_to_explode():
                                    # if not neighbor.node_loyalty():
                                    #     neighbor.blacktoken = 0
                                    #     neighbor.redtoken = 0
                                    # else:
                                        #  node.state = 'deactive'  # no need tu put this , node turn to deactive state
                                        #  in the node loyalty method


                            else:
                                raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion_to"
                                                "neighbors for node: ", self.id, " there are no token to diffuse")
                    elif self.state == 'red':
                        if neighbor.state == 'black':
                            if self.redtoken > 0:
                                neighbor.redtoken = 1
                                self.redtoken = -1
                                # if neighbor.ready_to_explode():
                                    # if not neighbor.node_loyalty():
                                    #     neighbor.blacktoken = 0
                                    #     neighbor.redtoken = 0
                                    # else:
                                    #     node.state = 'deactive'  # no need tu put this , node turn to deactive state
                                    #  in the node loyalty method

                            else:
                                raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion_to"
                                                    "neighbors for node: ", self.id, " there are no token to diffuse")

        elif set.type_of_game == 'harder_reactivation':
            if set.hra_strategy == 'naive':
                if self.state == 'black':
                    if neighbor.state != self.state and not neighbor.ready_to_explode():
                        if self.blacktoken > 0:
                            # print('diffusion 215')
                            neighbor.blacktoken = token_diffusion_num
                            self.blacktoken = -token_diffusion_num
                            # print('token dif num:', token_diffusion_num, 'node black token:', self.blacktoken)
                        else:
                            # print('token dif num:', token_diffusion_num, 'node black token:', self.blacktoken)
                            raise TypeError("Maliheeee!!class: Vertex, function:token_diffusion_to"
                                            "neighbors for node: ", self.id, " there are no token to diffuse")
                    else:
                        print('it is not eligible')
                        raise TypeError('not eligible')

                elif self.state == 'red':
                    # print('diffusion 225')
                    if neighbor.state != self.state and not neighbor.ready_to_explode():
                        if self.redtoken > 0:
                            # print('diffusion 229')
                            neighbor.redtoken = token_diffusion_num
                            self.redtoken = -token_diffusion_num
                        else:
                            # print('node red token:', self.redtoken)
                            raise TypeError("Maliheeee!!class: Vertex ,function: token_diffusion"
                                            "to_neighbors there are no token to diffuse")
                    else:
                        print('redddd it is not eligible')
                        raise TypeError('not eligible')
                elif self.state == 'deactive':
                    raise TypeError("Maliheeee!! class: Vertex ,function: token_diffusion"
                                    "to_neighbors the node state is deactive")

    def calculate_number_of_diffusing_tokens(self, neighbors):
        import setting as set
        importance_sum = 0
        associated_token = []
        eligible_neighbor = []
        index = []
        # print(type(neighbors))
        if self.threshold == self.degree:
            c = 0
            for idx, node in enumerate(neighbors):
                if node.state != self.state and not node.ready_to_explode():
                    eligible_neighbor.append(node)
                    associated_token.append(1)
                    index.append(c)
                    c += 1
        elif self.threshold > self.degree:
            importance = []
            for node in neighbors:
                if node.state != self.state and not node.ready_to_explode():
                    eligible_neighbor.append(node)
                    imp = 0.4 * node.threshold + 0.6 * node.degree
                    importance.append(imp)
                    importance_sum += imp
            associated_token = [0]*len(eligible_neighbor)
            index = sorted(range(len(importance)), key=lambda k: importance[k])
            index.reverse()
            node_tokens = self.threshold
            # print(node_tokens)
            while node_tokens > 0 and len(index) > 0:
                # print(node_tokens)
                # print('aaa')
                # print(len(index))
                for idx in index:
                    if node_tokens > 0:
                        associated_token[idx] += 1
                        node_tokens -= 1

        return associated_token, eligible_neighbor, index

    # this method is used after creating the MC tree and choosing the best node to give token to.
    # when the current player wants to give its tokens to the chosen node in his turn and the neighbors estimated
    # loyalty will be updated through diffusion

    # def advanced_dlv_diffusion(self, neighbor):
    #     if neighbor.state == 'deactive' and not neighbor.ready_to_explode():
    #         if self.state == 'black':
    #             if self.blacktoken > 0:
    #                 neighbor.blacktoken = 1
    #                 self.blacktoken = -1
    #             else:
    #                 raise TypeError("Maliheeee!!class: Vertex ,function: advance dlv diffusion"
    #                                 "neighbors for node: ", self.id, " there are no token to diffuse")
    #
    #         elif self.state == 'red':
    #             if self.redtoken > 0:
    #                 neighbor.redtoken = 1
    #                 self.redtoken = -1
    #             else:
    #                 raise TypeError("Maliheeee!!class: Vertex ,function: advance dlv diffusion"
    #                                 "to_neighbors there are no token to diffuse")
    #
    #         elif self.state == 'deactive':
    #             raise TypeError("Maliheeee!! class: Vertex ,function: advance dlv diffusion"
    #                             "to_neighbors the node state is deactive")
    #
    #     elif neighbor.state == 'black' or neighbor.state == 'red':
    #         if self.state == 'black':
    #             if neighbor.state == 'red':
    #                 if self.blacktoken > 0:
    #                     neighbor.blacktoken = 1
    #                     self.blacktoken = -1
    #                     # if neighbor.ready_to_explode():
    #                     #     if not neighbor.node_loyalty():  # ##################### edited version ################
    #                     #         neighbor.blacktoken = 0
    #                     #         neighbor.redtoken = 0
    #
    #                         # else:
    #                             # neighbor.total = 1
    #                             # rand = random.uniform(0, 1)
    #                             # if rand > neighbor.loyalty:
    #
    #                             # neighbor.state = 'deactive'
    #                             # neighbor.changingstate = 1
    #                             # neighbor.loyalty_guess = neighbor.changingstate/neighbor.total
    #                 else:
    #                     raise TypeError("Maliheeee!!class: Vertex ,function: advance dlv diffusion"
    #                                     " for node: ", self.id, " there are no token to diffuse")
    #         elif self.state == 'red':
    #             if neighbor.state == 'black':
    #                 if self.redtoken > 0:
    #                     neighbor.redtoken = 1
    #                     self.redtoken = -1
    #                     # if neighbor.ready_to_explode():
    #                     #     if not neighbor.node_loyalty():  # ##################### edited version ################
    #                     #         neighbor.blacktoken = 0
    #                     #         neighbor.redtoken = 0
    #
    #                         # else:
    #                             # neighbor.total = 1
    #                             # rand = random.uniform(0, 1)
    #                             # if rand > neighbor.loyalty:
    #                             #     neighbor.state = 'deactive'
    #
    #                             #     neighbor.changingstate = 1
    #                             #     neighbor.loyalty_guess = neighbor.changingstate/neighbor.total
    #
    #                         #
    #                 else:
    #                     raise TypeError("Maliheeee!!class: Vertex ,function: advance dlv diffusion"
    #                                     " for node: ", self.id, " there are no token to diffuse")

    # node_loyalty method has been changed for the case black knows the real loyalty and red doesnt know
    def node_loyalty(self, advanced_dlv_flag):
        import setting as set
        if set.current_player.color == 'black':
            rand = random.uniform(0, 1)
            if rand > (1 - self.loyalty):  # ########### real loyalty, it should be changed ##############
                self.state = 'deactive'  # #it will turn to red in explode method
                return True
            else:
                return False
        elif set.current_player.color == 'red':
            rand = random.uniform(0, 1)
            if advanced_dlv_flag:
                if rand > (1 - self.loyalty):
                    self.state = 'deactive'  # #it will turn to black in explode method
                    return True
                else:
                    return False
            else:
                if rand > .9:
                    self.state = 'deactive'  # #it will turn to black in explode method
                    return True
                else:
                    return False

    # if the node needs one more token to explode --> so in next move it will be explode by giving token to it
    def is_going_to_explode(self):
        if self.threshold - (self.black_token + self.red_token) == 1:
            return True
        else:
            return False

    def total_token(self):
        return self.blacktoken + self.redtoken

    # check if node is ready to explode
    def ready_to_explode(self):
        if self.redtoken + self.blacktoken == self.threshold:
            return True
        elif self.redtoken + self.blacktoken < self.threshold:
            return False
        elif self.redtoken + self.blacktoken > self.threshold:
            raise TypeError("Maliheeee!!!class: Vertex ,function: ready_to_explode"
                            " sum of tokens are more than threshold")

    def is_node_token_epmty(self):
        if self.redtoken + self.blacktoken == 0:
            return True
        else:
            return False

    def is_odd(self, num):
        if num % 2 == 1:
            return True

    def is_even(self, num):
        if num % 2 == 0:
            return True

    # getter and setter for black tokens
    @property
    def blacktoken(self):
       return self.black_token

    @blacktoken.setter
    def blacktoken(self, val):
        global last_token
        # if self.state == 'deactive':
        if val == 0:
            self.black_token = val
        elif val > 0 and val + self.blacktoken + self.redtoken <= self.threshold:
            self.black_token += val
            if self.ready_to_explode():
                self.lasttoken = 'black'
                # print()
        elif val < 0 and val + self.blacktoken >= 0:
            self.black_token += val

        # elif self.black_token + self.redtoken == self.threshold:
        #     print('the node', self.id, 'should explode')

        if self.blacktoken + self.redtoken > self.threshold:
            raise TypeError("Maliheeee!!!class: Vertex ,function: blacktoken"
                            " sum of tokens are more than threshold")

    # getter and setter for red tokens
    @property
    def redtoken(self):
        return self.red_token

    @redtoken.setter
    def redtoken(self, val):
        global last_token
        # if self.state == 'deactive':
        if val == 0:
            self.red_token = val

        elif val > 0 and val + self.blacktoken + self.redtoken <= self.threshold:
            self.red_token += val
            if self.ready_to_explode():
                self.lasttoken = 'red'
                # print()

        elif val < 0 and self.redtoken + val >= 0:
            self.red_token += val
        #
        # elif self.blacktoken + self.redtoken == self.threshold:
        #     print('the node', self.id, 'should explode')

        if (self.blacktoken + self.redtoken) > self.threshold:
            raise TypeError("Maliheeee!!!class: Vertex ,function: redtoken"
                            " sum of tokens are more than threshold")
    # getter and setter for state
    @property
    def state(self):
        return self.state_

    @state.setter
    def state(self, state):
        self.state_ = state

    @property
    def lasttoken(self):
        return self.last_token

    @lasttoken.setter
    def lasttoken(self, color):
        self.last_token = color

    @property
    def inc_threshold(self):
        return self.threshold

    @inc_threshold.setter
    def inc_threshold(self, num):
        self.threshold += num
