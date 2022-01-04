import numpy as np
import networkx as nx
import math

n_nodes = 6
values = np.loadtxt("CA-GrQc/values.txt")
# values = [3, 2, 1, 1, 1, 1]

thresholds = np.zeros((2, n_nodes))
for i in range(n_nodes):
    thresholds[0, i] = np.random.randint(3)+1
    thresholds[1, i] = np.random.randint(3)+1
# thresholds[0, :] = [1, 2, 2, 1, 3, 1]
# thresholds[1, :] = [3, 1, 3, 2, 1, 3]


def find_activated(position):
    p = np.zeros((2, n_nodes))
    activated = set()

    player = 0
    for i in range(len(position)):
        node_index = position[i][0]
        p[player, node_index] += position[i][1]
        if p[player, node_index] >= thresholds[player, node_index] or p[1-player, node_index] >= thresholds[1-player, node_index]:
            activated.add(node_index)
        player = 1 - player

    return activated


def calculate_payoff(position):
    payoff = np.zeros(2)
    p = np.zeros((2, n_nodes))
    activated = set()

    player = 0
    for i in range(len(position)):
        node_index = position[i][0]
        p[player, node_index] += position[i][1]
        if p[player, node_index] >= thresholds[player, node_index] and node_index not in activated:
            activated.add(node_index)
            payoff[player] += values[node_index]
        player = 1 - player

    return payoff[0] - payoff[1]


def mini_max(g, position, depth, alpha, beta, is_maximizing):
    activated = find_activated(position)
    sum_budget = 0
    for p in position:
        sum_budget += p[1]

    if depth == 0 or len(position) >= 2*n_nodes or len(activated) == n_nodes or sum_budget == 2*n_nodes:
        payoff = calculate_payoff(position)
        g.node[position]["v"] = payoff
        return payoff

    budget = 0
    l = len(position)-2
    while l >= 0:
        budget += position[l][1]
        l -= 2

    remained_budget = n_nodes - budget

    if remained_budget >= 3:
        for i in range(n_nodes):
            if i not in activated:
                new_node = position + ((i, 1),)
                g.add_edge(position, new_node)
                g.node[new_node]['v'] = float('NaN')

                new_node = position + ((i, 2),)
                g.add_edge(position, new_node)
                g.node[new_node]['v'] = float('NaN')

                new_node = position + ((i, 3),)
                g.add_edge(position, new_node)
                g.node[new_node]['v'] = float('NaN')
    elif remained_budget >= 2:
        for i in range(n_nodes):
            if i not in activated:
                new_node = position + ((i, 1),)
                g.add_edge(position, new_node)
                g.node[new_node]['v'] = float('NaN')

                new_node = position + ((i, 2),)
                g.add_edge(position, new_node)
                g.node[new_node]['v'] = float('NaN')
    elif remained_budget >= 1:
        for i in range(n_nodes):
            if i not in activated:
                new_node = position + ((i, 1),)
                g.add_edge(position, new_node)
                g.node[new_node]['v'] = float('NaN')

    else:
        new_node = position + ((0, 0),)
        g.add_edge(position, new_node)
        g.node[new_node]['v'] = float('NaN')

    if is_maximizing:
        max_val = -math.inf
        for edge in g.edges(position):
            val = mini_max(g, edge[1], depth-1, alpha, beta, False)
            max_val = max(max_val, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        g.node[position]["v"] = max_val
        return max_val
    else:
        min_val = math.inf
        for edge in g.edges(position):
            val = mini_max(g, edge[1], depth-1, alpha, beta, True)
            min_val = min(min_val, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        g.node[position]["v"] = min_val
        return min_val


def alpha_beta(position, player, depth):
    g = nx.DiGraph()
    g.add_node(position, v=float('NaN'))
    if player == 1:
        is_maximizing = True
    else:
        is_maximizing = False
    mini_max(g, position, depth, -math.inf, math.inf, is_maximizing)
    for edge in g.edges(position, data=True):
        if g.node[position]["v"] == g.node[edge[1]]["v"]:
            node = edge[1][-1]
            n_created_nodes = g.number_of_nodes()
            # g.clear()
            return node, g


print("thresholds:")
print(thresholds[0, :])
print(thresholds[1, :])
print("-----------------------------")

state = ()
depth = 2*n_nodes
n, g = alpha_beta(state, 1, depth)
position = state
for i in range(depth):
    for edge in g.edges(position):
        if g.node[position]['v'] == g.node[edge[1]]['v']:
            position = edge[1]
            print(position[-1])
            break

print("-----------------------------")
print(calculate_payoff(position))
