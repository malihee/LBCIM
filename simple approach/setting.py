import networkx as nx
import random
import vertex as v
import graph as gr
import math
import pandas as pd
from player import Player


type_of_game = 'harder_reactivation'  # 'full_loyalty_more_token' # 'zero_loyalty_variant' #'full_loyalty_variant'
# dlv_strategy = 'advanced'  # 'naive'
hra_strategy = 'naive'
flmt_strategy = 'naive'  # 'naive'
global red_player_token
global black_player_token
mcts_approach = 'no_heuristic'


def create_data(type, data_name):
    global initial_token_num
    global dataset
    global num_of_nodes
    num_of_nodes = 0
    num_of_edges = 0
    dataset = nx.Graph()
    dataset.add_nodes_from([1,2,3])
    if type_of_game != 'zero_loyalty_variant':
        # while num_of_edges < 19 or num_of_edges > 258 or not(nx.is_connected(dataset)):
        # while not (nx.is_connected(dataset)):

            print('hi')
            # num_of_nodes = random.randint(14, 88)
            num_of_nodes = random.randint(30, 70)

            if type == 'small_world':
                dataset = nx.connected_watts_strogatz_graph(n=num_of_nodes, k=random.randint(3, 7), p=.5)
            elif type == 'random_graph':
                dataset = nx.erdos_renyi_graph(n=num_of_nodes, p=.15, seed=None, directed=False)
            elif type == 'scale_free':
                dataset = nx.barabasi_albert_graph(n=num_of_nodes, m=random.randint(1, math.floor(num_of_nodes/3)), seed=None)
            elif type == 'real_ds':
                if data_name == 'facebook':
                    df = pd.read_csv('../real datasets/facebook_combined.csv')
                    dataset = nx.from_pandas_edgelist(df, source='node_1', target='node_2', edge_attr=True)
                    communities = [c for c in sorted(
                        nx.algorithms.community.label_propagation.label_propagation_communities(dataset), key=len,
                        reverse=True)]
                    set = communities[6]
                    list = []
                    for e in set:
                        list.append(e)
                    list_of_100_node = list[:100]
                    dataset = dataset.subgraph(list_of_100_node)
                    dataset = nx.Graph(dataset)
                    print('ej:', len(dataset.edges))
                    print('nd:', len(dataset.nodes))
                    num_of_nodes = len(dataset.nodes)
                elif data_name == 'p2p':
                    df = pd.read_csv('../real datasets/p2p.csv')
                    dataset = nx.from_pandas_edgelist(df, source='node_1', target='node_2', edge_attr=True)
                    dataset = dataset.to_undirected(as_view=False)
                    communities = [c for c in sorted(
                        nx.algorithms.community.label_propagation.label_propagation_communities(dataset), key=len,
                        reverse=True)]
                    set = communities[7] # exactly 100 nodes
                    list = []
                    for e in set:
                        list.append(e)
                    list_of_100_node = list
                    dataset = dataset.subgraph(list_of_100_node)
                    dataset = nx.Graph(dataset)
                    print('ej:', len(dataset.edges))
                    print('nd:', len(dataset.nodes))
                    num_of_nodes = len(dataset.nodes)
                elif data_name == 'ca hepth':
                    df = pd.read_csv('../real datasets/ca hepth.csv')
                    dataset = nx.from_pandas_edgelist(df, source='node_1', target='node_2', edge_attr=True)
                    dataset = dataset.to_undirected(as_view=False)
                    communities = [c for c in sorted(
                        nx.algorithms.community.label_propagation.label_propagation_communities(dataset), key=len,
                        reverse=True)]
                    set = communities[1]  # exactly 112 nodes
                    list = []
                    for e in set:
                        list.append(e)
                    list_of_100_node = list
                    dataset = dataset.subgraph(list_of_100_node)
                    dataset = nx.Graph(dataset)
                    print('ej:', len(dataset.edges))
                    print('nd:', len(dataset.nodes))
                    num_of_nodes = len(dataset.nodes)
                elif data_name == 'ca GrQc':
                    df = pd.read_csv('../real datasets/ca-GrQc.csv')
                    dataset = nx.from_pandas_edgelist(df, source='node_1', target='node_2', edge_attr=True)
                    dataset = dataset.to_undirected(as_view=False)
                    communities = [c for c in sorted(
                        nx.algorithms.community.label_propagation.label_propagation_communities(dataset), key=len,
                        reverse=True)]
                    set = communities[0]  # exactly 153 nodes
                    list = []
                    for e in set:
                        list.append(e)
                    list_of_100_node = list[:100]
                    dataset = dataset.subgraph(list_of_100_node)
                    dataset = nx.Graph(dataset)
                    print('ej:', len(dataset.edges))
                    print('nd:', len(dataset.nodes))
                    num_of_nodes = len(dataset.nodes)
                # if data_name == 'HR_edges':
                #     df = pd.read_csv('../real datasets/deezer_clean_data/HR_edges.csv')
                #     dataset = nx.from_pandas_edgelist(df, source='node_1', target='node_2', edge_attr=True)
                #     print('45')
                #     dataset = dataset.subgraph(range(500, 1000))
                #     print('ej:', len(dataset.edges))
                #     print('nd:', len(dataset.nodes))
                #
                #
                # if data_name == 'HU_edges':
                #     df = pd.read_csv('../real datasets/deezer_clean_data/HU_edges.csv')
                #     dataset = nx.from_pandas_edgelist(df, source='node_1', target='node_2', edge_attr=True)
                #     dataset = dataset.subgraph(500)
                #
                # if data_name == 'RO_edges':
                #     df = pd.read_csv('../real datasets/deezer_clean_data/RO_edges.csv')
                #     dataset = nx.from_pandas_edgelist(df, source='node_1', target='node_2', edge_attr=True)
                #     dataset = dataset.subgraph(500)

            num_of_edges = len(dataset.edges)
            # if type_of_game == 'full_loyalty_more_token':
            initial_token_num = math.floor(num_of_nodes * 2/7)
            # else:
            #     initial_token_num = math.floor(num_of_nodes - num_of_edges / 2)
            print(num_of_nodes)
            print(num_of_edges)
            print(num_of_nodes - num_of_edges/2)
    else:
        while num_of_edges < 19 or num_of_edges > 258 or not(nx.is_connected(dataset)) or num_of_nodes - num_of_edges/2 <= 1:
            num_of_nodes = random.randint(14, 88)
            if type == 'small_world':
                dataset = nx.connected_watts_strogatz_graph(n=num_of_nodes, k=3, p=.7)
            elif type == 'random_graph':
                dataset = nx.erdos_renyi_graph(n=num_of_nodes, p=.15, seed=None, directed=False)
            elif type == 'scale_free':
                dataset = nx.barabasi_albert_graph(n=num_of_nodes, m=random.randint(1, 2), seed=None)
            num_of_edges = len(dataset.edges)
            if type_of_game == 'full_loyalty_more_token':
                initial_token_num = math.floor(num_of_nodes * 2/5)
            else:
                initial_token_num = math.floor(num_of_nodes - num_of_edges / 2)
            print(num_of_nodes)
            print(num_of_edges)
            print(num_of_nodes - num_of_edges/2)
    # importing networkx
    # import networkx as nx
    # importing matplotlib.pyplot
    import matplotlib.pyplot as plt

    nx.draw(dataset)
    plt.savefig("p2p.png")

    return dataset, initial_token_num


def create_graph():
    global dataset
    vertices = []
    id_ind = 0
    d = dict()
    for i in dataset.nodes:
        d[i] = id_ind
        id_ind+=1
    id_ind = 0
    for i in dataset.nodes:
        # first time players assume all nodes are full loyal(0)

        vertices.append(v.Vertex(id=id_ind, threshold=dataset.degree[i], blacktoken=0, redtoken=0, degree=dataset.degree[i],
                                 state_='deactive', neighbors=[d[n] for n in dataset.neighbors(i)], lasttoken=''))
        id_ind+=1
    graph = gr.Graph(vertices, dataset.edges, False)
    return graph


def pagerank():
    global dataset
    page_rank = nx.pagerank(dataset)
    return page_rank


def hits():
    global dataset
    hubs, authorithy = nx.hits(dataset)
    sort_hubs = {k: v for k, v in sorted(hubs.items(), key=lambda item: item[1])}
    sort_auto = {k: v for k, v in sorted(authorithy.items(), key=lambda item: item[1])}
    return sort_hubs, sort_auto


def degree_centrality():
    global dataset
    degree_centrality = nx.degree_centrality(dataset)
    return degree_centrality

@property
def current_player():
    return currentplayer


@current_player.setter
def current_player(player):
    global currentplayer
    currentplayer = player


@property
def opponent_player():
    return opponentplayer


@opponent_player.setter
def opponent_player(player):
    global opponentplayer
    opponentplayer = player

@property
def dlv_player_approach():
    global approach
    return approach


@dlv_player_approach.setter
def dlv_player_approach(appr):
    global approach
    approach = appr
