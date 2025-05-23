# Unit-III Matching and Covers: Matchings, maximal and maximum matchings, M-augmenting paths, Hall's theorem and consequences, Min-max theorems, maximum matchings and vertex covers, independent sets and edge covers,Connectivity, vertex cuts, Edge-connectivity. 

import networkx as nx
import matplotlib.pyplot as plt

print("### UNIT-III MATCHING AND COVERS ###\n")

# 1. Matchings: Maximal and Maximum
G = nx.Graph()
edges = [(1, 4), (1, 5), (2, 5), (2, 6), (3, 6)]
G.add_edges_from(edges)
print("Graph edges:", G.edges())

max_matching = nx.max_weight_matching(G, maxcardinality=True)
print("\n1. Maximum Matching (Max Cardinality):", max_matching)

# Maximal matching example (greedy)
def maximal_matching_greedy(graph):
    matched = set()
    matching = set()
    for u, v in graph.edges():
        if u not in matched and v not in matched:
            matching.add((u,v))
            matched.add(u)
            matched.add(v)
    return matching

maximal = maximal_matching_greedy(G)
print("Maximal Matching (greedy):", maximal)

# 2. M-Augmenting paths (illustration using max matching)
print("\n2. M-Augmenting Paths:")
def find_augmenting_path(graph, matching):
    # BFS-based search for augmenting path (simplified)
    # Here just show we can check for augmenting paths using networkx functions
    # NetworkX does not have direct augmenting path finder; max_weight_matching uses it internally.
    print("Augmenting path finding is algorithmic part of max matching - shown by max_weight_matching")

find_augmenting_path(G, max_matching)

# 3. Hall's Theorem and Consequences
print("\n3. Hall's Theorem Check (Bipartite Matching):")

B = nx.Graph()
# Bipartite sets U and V
U = {1, 2, 3}
V = {4, 5, 6}
B.add_nodes_from(U, bipartite=0)
B.add_nodes_from(V, bipartite=1)
B.add_edges_from(edges)

def hall_condition(graph, left_set):
    # For each subset S of left_set, |N(S)| >= |S|
    from itertools import chain, combinations
    def neighbors(s):
        n = set()
        for u in s:
            n |= set(graph.neighbors(u))
        return n
    # Powerset of left_set except empty set
    for r in range(1, len(left_set)+1):
        for subset in combinations(left_set, r):
            if len(neighbors(subset)) < len(subset):
                return False
    return True

print("Does bipartite graph satisfy Hall's condition?", hall_condition(B, U))

# 4. Min-Max Theorems (Kőnig's theorem)
print("\n4. Kőnig's Theorem: Maximum matching size = Minimum vertex cover size in bipartite graphs")
max_match_size = len(nx.bipartite.maximum_matching(B, top_nodes=U))//2
min_vertex_cover = nx.bipartite.minimum_vertex_cover(B, top_nodes=U)
print("Maximum Matching Size:", max_match_size)
print("Minimum Vertex Cover Size:", len(min_vertex_cover))

# 5. Independent Sets and Edge Covers
print("\n5. Independent Sets and Edge Covers:")
independent_set = nx.maximum_independent_set(G)
print("Maximum Independent Set:", independent_set)

edge_cover = nx.min_edge_cover(G)
print("Minimum Edge Cover edges:", edge_cover)

# 6. Connectivity: Vertex cuts and Edge-connectivity
print("\n6. Connectivity:")
print("Node connectivity of G:", nx.node_connectivity(G))
print("Edge connectivity of G:", nx.edge_connectivity(G))

# Vertex cuts example
cut_nodes = list(nx.minimum_node_cut(G))
print("Minimum vertex cut set:", cut_nodes)

# Edge cuts example
cut_edges = list(nx.minimum_edge_cut(G))
print("Minimum edge cut set:", cut_edges)

# Visualization
pos = nx.spring_layout(G)
plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=max_matching, edge_color='red', width=3)
plt.title("Graph with Maximum Matching (red edges)")
plt.show()
