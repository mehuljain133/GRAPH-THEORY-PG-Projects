# Unit-II Trees: Trees and forests, characterizations of trees, spanning trees, radius and diameter, enumeration of trees, Cayley’s formula, Prüfer code, counting spanning trees, deletion-contraction, the matrix tree theorem, graceful labelling, minimum spanning trees (Kruskal’s algorithm), shortest paths (Dijkstra’s algorithm)

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx.algorithms.tree import tree_all_pairs_lowest_common_ancestors

print("### UNIT-II TREES: All in one demo ###\n")

# 1. Trees and Forests
print("1. Tree Example:")
T = nx.Graph()
T.add_edges_from([(0, 1), (0, 2), (1, 3), (1, 4)])
print("Nodes:", T.nodes())
print("Edges:", T.edges())
print("Is Tree?", nx.is_tree(T))

F = nx.Graph()
F.add_edges_from([(0, 1), (2, 3)])
print("\nForest Example:")
print("Is Forest? (all components are trees):", all(nx.is_tree(T.subgraph(c)) for c in nx.connected_components(F)))

# 2. Characterizations of Trees
print("\n2. Characterizations of Trees:")
print("Number of edges =", T.number_of_edges())
print("Number of nodes =", T.number_of_nodes())
print("Edges = Nodes - 1 ? ", T.number_of_edges() == T.number_of_nodes() - 1)
print("Is connected? ", nx.is_connected(T))
print("A tree is connected and edges = nodes-1? ", nx.is_tree(T))

# 3. Spanning Trees
G = nx.cycle_graph(5)
print("\n3. Spanning Trees of a cycle graph with 5 nodes:")
spanning_trees = list(nx.spanning_trees(G))
print(f"Number of spanning trees: {len(spanning_trees)}")

# 4. Radius and Diameter
print("\n4. Radius and Diameter of tree T:")
print("Radius:", nx.radius(T))
print("Diameter:", nx.diameter(T))

# 5. Enumeration of Trees & Cayley’s formula
n = 4
print("\n5. Number of labeled trees with n =", n)
cayley_count = n ** (n - 2)
print("Cayley's formula:", cayley_count)

# 6. Prüfer Code
print("\n6. Prüfer Code of tree T:")
prufer = nx.prufer_sequence(T)
print("Prüfer sequence:", prufer)

print("Decode Prüfer sequence back to tree:")
decoded_tree = nx.from_prufer_sequence(prufer)
print("Decoded edges:", decoded_tree.edges())

# 7. Counting Spanning Trees - Matrix Tree Theorem
print("\n7. Counting spanning trees using Matrix Tree Theorem (Kirchhoff's theorem):")
L = nx.laplacian_matrix(G).todense()
# Delete one row and column
L_minor = np.delete(np.delete(L, 0, axis=0), 0, axis=1)
det = round(np.linalg.det(L_minor))
print("Number of spanning trees in G:", det)

# 8. Deletion-Contraction Illustration
print("\n8. Deletion-Contraction example:")
def deletion_contraction(graph, edge):
    G_del = graph.copy()
    G_del.remove_edge(*edge)
    G_contr = nx.contracted_edge(graph, edge, self_loops=False)
    return G_del, G_contr

edge = (0, 1)
print(f"Deleting and contracting edge {edge} in graph G")
G_del, G_contr = deletion_contraction(G, edge)
print("Edges after deletion:", G_del.edges())
print("Edges after contraction:", G_contr.edges())

# 9. Graceful Labelling (example check)
print("\n9. Graceful labelling - Check if path graph is graceful:")
P = nx.path_graph(4)
def is_graceful(G):
    n = G.number_of_nodes()
    labels = list(range(n))
    edges = G.edges()
    # We brute force check one labelling for demonstration
    used_edge_labels = set()
    for u, v in edges:
        diff = abs(labels[u] - labels[v])
        if diff == 0 or diff > n - 1 or diff in used_edge_labels:
            return False
        used_edge_labels.add(diff)
    return True
print("Is path graph graceful?", is_graceful(P))

# 10. Minimum Spanning Tree (Kruskal’s algorithm)
print("\n10. Minimum Spanning Tree using Kruskal's algorithm:")
W = nx.Graph()
W.add_weighted_edges_from([(0,1,2), (0,2,1), (1,2,3), (1,3,4), (2,3,5)])
mst = nx.minimum_spanning_tree(W, algorithm='kruskal')
print("MST edges with weights:")
for u, v, w in mst.edges(data='weight'):
    print(f"({u},{v}) with weight {w}")

# 11. Shortest Paths (Dijkstra’s algorithm)
print("\n11. Shortest paths using Dijkstra's algorithm from node 0:")
lengths = nx.single_source_dijkstra_path_length(W, 0)
print(lengths)

# Optional: Draw MST
nx.draw(mst, with_labels=True)
plt.title("Minimum Spanning Tree")
plt.show()
