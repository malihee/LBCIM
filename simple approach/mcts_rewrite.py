from __future__ import division
import time
import math
import random
import setting as set
import heuristics as hs
from random import uniform
from test_tree import make_tree
from minimax import minimax
import numpy


def randomPolicy(state):
    while not state.isTerminal():
        # print('into while')
        try:
            # print('aftre try')
            # print('random_policy')
            actions = state.getPossibleActions()  # input is False because its expansion of
            # print('actions')
            if set.mcts_approach == 'use_heuristic':
                # print('into use heu')
                best_action = []
                greedy_prob = .7
                action_hs_val = []
                heuristic_value = -9999
                for action in actions:
                    if action.player == 'black':
                        # print('black token:', action.b_token)
                        # action_hs_val.append(hs.linear_combination(action.graph, action.player, action.b_token))
                        temp = hs.linear_combination(action.graph, action.player, action.b_token)
                        action_hs_val.append(temp)
                    elif action.player == 'red':
                        # print('red token:', action.r_token)
                        # action_hs_val.append(hs.linear_combination(action.graph, action.player, action.r_token))
                        temp = hs.linear_combination(action.graph, action.player, action.r_token)
                        action_hs_val.append(temp)

                    if temp > heuristic_value:
                        heuristic_value = temp
                        best_action = [action]
                    elif temp == heuristic_value:
                        best_action.append(action)
                if greedy_prob > random.random():
                    action = random.choice(best_action)
                else:
                    action = random.choice(actions)
                # print('out of useheu')
            elif set.mcts_approach == 'no_heuristic':
                action = random.choice(actions)
        except IndexError:
            for node in state.graph.vertices:
                print('threshold:', node.threshold, 'black token:', node.blacktoken, 'red token',
                      node.redtoken, 'state:', node.state)
            raise Exception("Non-terminal state has no possible actions: " + str(state))
        # print('before state')
        state = state.takeAction(action)
        # print('after state')
    return state.getReward()


class treeNode():
    def __init__(self, state, parent):
        self.state = state
        self.isTerminal = state.isTerminal()
        self.isFullyExpanded = self.isTerminal
        self.parent = parent
        self.numVisits = 0
        self.totalReward = 0
        self.children = {}


class mcts():
    def __init__(self, timeLimit=None, iterationLimit=None, explorationConstant=1 / math.sqrt(2),
                 rolloutPolicy=randomPolicy):
        if timeLimit != None:
            if iterationLimit != None:
                raise ValueError("Cannot have both a time limit and an iteration limit")
            # time taken for each MCTS search in milliseconds
            self.timeLimit = timeLimit
            self.limitType = 'time'
        else:
            if iterationLimit == None:
                raise ValueError("Must have either a time limit or an iteration limit")
            # number of iterations of the search
            if iterationLimit < 1:
                raise ValueError("Iteration limit must be greater than one")
            self.searchLimit = iterationLimit
            self.limitType = 'iterations'
        self.explorationConstant = explorationConstant
        self.rollout = rolloutPolicy

    def search(self, initialState):
        self.root = treeNode(initialState, None)
        # print('fcccsdsadas', self.root.state.graph.node_number())
        # ######### Minimax first level expand #############
        if set.mcts_approach == 'use_heuristic':
            actionss = self.root.state.getPossibleActions()
            minimax_val = []
            # best_child = []
            for idx, action in enumerate(actionss):
                tree_depth = 2
                # tree_search = make_tree(action.graph, tree_depth, 0, set.opponent_player.color, action.r_token, action.b_token)
                # minimax_val.append(minimax(position=tree_search,
                #                            depth=tree_depth,
                #                            alpha=-float('Inf'),
                #                            beta=float('Inf'),
                #                            player=set.opponent_player.color))
            # print('minimax vals:', minimax_val)
            # sort_index = list(numpy.argsort(minimax_val))
            # sort_index.reverse()
            # slice =numpy.floor(len(actions)/2)
            # indice_of_the_best = sort_index[:int(numpy.ceil(len(actionss) / 2))]
            actions = []
            # for i in indice_of_the_best:
            #     actions.append(actionss[i])
        elif set.mcts_approach == 'no_heuristic':
            actions = []

        # ##################################################

        if self.limitType == 'time':
            timeLimit = time.time() + self.timeLimit / 1000
            while time.time() < timeLimit:
                self.executeRound(actions)
        else:
            for i in range(self.searchLimit):
                self.executeRound(actions)
        # if set.mcts_approach == 'no_heuristic':
        bestChild = self.getBestChild(self.root, 0)
        # if set.mcts_approach == 'use_heuristic':
        #     bestChild = self.getBestChildEdit(self.root, 0, minimax_val)
        return self.getAction(self.root, bestChild, actions)
        # return bestChild

    def minimax_expand(self):
        actions = self.root.state.getPossibleActions()
        minimax_val = []
        best_child = []
        for idx, action in enumerate(actions):
            tree_depth = 2
            tree_search = make_tree(action.graph, tree_depth, 0, set.current_player.color)
            print('tree created')
            minimax_val[idx], best_child[idx] = minimax(position=tree_search, depth=tree_depth, alpha=-float('Inf'),
                                                        beta=float('Inf'), player=set.opponent_player.color)
        sort_index = list(numpy.argsort(minimax_val))
        sort_index.reverse()
        # slice =numpy.floor(len(actions)/2)
        action = actions[sort_index[:int(numpy.ceil(len(actions) / 2))]]
        return action

    def executeRound(self, action):
        node = self.selectNode(self.root, action)
        reward = self.rollout(node.state)
        self.backpropogate(node, reward)

    def selectNode(self, node, action):
        while not node.isTerminal:
            if node.isFullyExpanded:
                node = self.getBestChild(node, self.explorationConstant)
            else:
                return self.expand(node, action)
        return node

    def expand(self, node, actions):
        # if set.mcts_approach == 'no_heuristic':
        actions = node.state.getPossibleActions()
        # print(type(actions))
        # i=0
        # for action in actions:
        for i in range(len(actions)):
            # if action not in node.children.keys():
            if i not in node.children.keys():
                # print('i is :', i)
                newNode = treeNode(node.state.takeAction(actions[i]), node)
                # node.children[action] = newNode
                node.children[i] = newNode
                if len(actions) == len(node.children):
                    node.isFullyExpanded = True
                return newNode
            # i+=1
        raise Exception("Should never reach here")

    def backpropogate(self, node, reward):
        while node is not None:
            node.numVisits += 1
            node.totalReward += reward
            node = node.parent

    def getBestChild(self, node, explorationValue):
        bestValue = float("-inf")
        bestNodes = []

        for idx, child in enumerate(node.children.values()):
            nodeValue = child.totalReward / child.numVisits + explorationValue * math.sqrt(2 * math.log(node.numVisits)
                                                                                           / child.numVisits)
            if nodeValue > bestValue:
                bestValue = nodeValue
                bestNodes = [child]
            elif nodeValue == bestValue:
                bestNodes.append(child)
        return random.choice(bestNodes)

    def getBestChildEdit(self, node, explorationValue, minimax_val):
        bestValue = float("-inf")
        bestNodes = []
        alpha = .1
        for idx, child in enumerate(node.children.values()):
            q = (1-alpha)*(child.totalReward/child.numVisits) + alpha * minimax_val[idx]
            nodeValue = q + explorationValue * math.sqrt(2 * math.log(node.numVisits) / child.numVisits)
            if nodeValue > bestValue:
                bestValue = nodeValue
                bestNodes = [child]
            elif nodeValue == bestValue:
                bestNodes.append(child)
        return random.choice(bestNodes)

    def getAction(self, root, bestChild, actions):
        # if set.mcts_approach == 'no_heuristic':
        actions = root.state.getPossibleActions()
        for act, node in root.children.items():
                if node is bestChild:
                    return actions[act]
