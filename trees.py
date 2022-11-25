import networkx as nx


er     = nx.erdos_renyi_graph(20, 0.2, seed = 21)
er2    = nx.erdos_renyi_graph(20, 0.1, seed = 4)
tree   = nx.random_tree(6)
clique = nx.Graph()
clique.add_nodes_from([0, 1, 2, 3])
clique.add_edges_from([
    (0, 1), (0, 2), (0, 3),
    (1, 0), (1, 2), (1, 3),
    (2, 0), (2, 1), (2, 3),
    (3, 0), (3, 1), (3, 2)
])
