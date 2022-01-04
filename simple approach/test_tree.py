from test_node import Node


class Tree:
    def __init__(self, root, children):
        self.root = root
        self.children = children
        # self.parent = parent
        # print('level:', self.root.level)


def make_tree(data, depth, level, player, redplayertoken, blackplayertoken):
    # print('0 red token:', redplayertoken)
    # print('0 black token:', blackplayertoken)

    # this is for leaves
    if level == depth:
        # print('level:', self.root.level)
        # print('0jus red:', redplayertoken)
        # print('0jus black:', blackplayertoken)

        return Tree(Node(data=data, level=level, player=player,  red_player_token=redplayertoken,
                         black_player_token=blackplayertoken), children=None)
    # this is foe middle nodes in tree
    else:
        children_list = []
        # print('level:', self.root.level)
        next_pos, token_cap = data.next_position_of_graph(player, None)

        for idx, child in enumerate(next_pos):  # ##### give the player token num to the next_position_of_graph as input
            if player == 'black':
                if blackplayertoken - token_cap[idx] >= 0:
                    node = make_tree(data=child, depth=depth, level=level+1, player='red', redplayertoken=redplayertoken
                                     , blackplayertoken=blackplayertoken - token_cap[idx])
                # else:
                #     return
                    children_list.append(node)
            elif player == 'red':
                if redplayertoken - token_cap[idx] >= 0:
                    node = make_tree(data=child, depth=depth, level=level + 1, player='black',
                                     redplayertoken=redplayertoken - token_cap[idx],
                                     blackplayertoken=blackplayertoken)
                # else:
                #     return
                    children_list.append(node)
        # print('1jus red:', redplayertoken)
        # print('11 red token:', redplayertoken)
        # print('11 black token:', blackplayertoken)

        return Tree(Node(data=data, level=level, player=player, red_player_token=redplayertoken,
                         black_player_token=blackplayertoken), children=children_list)


