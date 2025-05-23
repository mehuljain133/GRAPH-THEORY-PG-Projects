# Unit-VI Planar Graphs: Planar graphs, Euler's formula, Kuratowski's theorem, five and four color theorems.

import networkx as nx
import matplotlib.pyplot as plt

print("### UNIT-VI: Planar Graphs ###\n")

# 1. Planar Graph Example
G = nx.Graph()
# A planar graph (cube graph)
G.add_edges_from([(1,2),(2,3),(3,4),(4,1),(1,5),(2,6),(3,7),(4,8),(5,6),(6,7),(7,8),(8,5)])
print("Graph edges:", G.edges())

# Check if planar
is_planar, embedding = nx.check_planarity(G)
print("1. Is the graph planar?", is_planar)

# 2. Euler's formula: V - E + F = 2 for connected planar graphs
V = G.number_of_nodes()
E = G.number_of_edges()
if is_planar:
    F = embedding.faces_count()
    print(f"\n2. Euler's formula check: V - E + F = {V} - {E} + {F} = {V - E + F}")
else:
    print("\nGraph is not planar; Euler's formula for planar graphs not applicable.")

# 3. Kuratowski's theorem: Detect K5 or K3,3 subdivision (minor)
print("\n3. Kuratowski's theorem (checking for K5 or K3,3 minors):")
# NetworkX does not have direct Kuratowski minor detection, but planarity check finds a Kuratowski subgraph if non-planar
# So let's test a non-planar graph:
K33 = nx.complete_bipartite_graph(3,3)
is_planar_k33, _ = nx.check_planarity(K33)
print("Is K3,3 planar?", is_planar_k33)
K5 = nx.complete_graph(5)
is_planar_k5, _ = nx.check_planarity(K5)
print("Is K5 planar?", is_planar_k5)

# 4. Five color theorem (illustration)
print("\n4. Five color theorem example: Coloring planar graph with <=5 colors")
coloring_5 = nx.coloring.greedy_color(G, strategy='largest_first')
num_colors_5 = max(coloring_5.values()) + 1
print("Number of colors used (should be <=5):", num_colors_5)

# 5. Four color theorem (hard to prove, but can color planar graphs)
print("\n5. Four color theorem example: Coloring planar graph with <=4 colors using greedy")
coloring_4 = nx.coloring.greedy_color(G, strategy='smallest_last')
num_colors_4 = max(coloring_4.values()) + 1
print("Number of colors used (hopefully <=4):", num_colors_4)

# Visualize planar graph and its coloring
pos = nx.planar_layout(G)
plt.figure(figsize=(8,6))
nx.draw(G, pos, with_labels=True, node_color=[coloring_5[n] for n in G.nodes()], cmap=plt.cm.Set3, node_size=600)
plt.title("Planar Graph Colored (Five Color Theorem)")
plt.show()
