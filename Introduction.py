# Unit-I Fundamental Concepts: Definitions, examples of problems in graph theory, adjacency and incidence matrices, isomorphisms, paths, walks, cycles, components, cut-edges, cut-vertices, bipartite graphs, eulerian graphs, vertex degrees, reconstruction conjecture, extremal problems, degree sequences, directed graphs, de Bruijn cycles, Orientations and tournaments. 

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import isomorphism
from networkx.generators.classic import complete_graph

# 1. Definitions & Graph Example
g = nx.Graph()
g.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3)])
print("Graph Nodes:", g.nodes())
print("Graph Edges:", g.edges())

# 2. Adjacency & Incidence Matrices
print("\nAdjacency Matrix:")
print(nx.adjacency_matrix(g).todense())

print("\nIncidence Matrix:")
incidence_matrix = nx.incidence_matrix(g, oriented=False).todense()
print(incidence_matrix)

# 3. Isomorphism
h = nx.Graph()
h.add_edges_from([(3, 4), (4, 5), (5, 3), (5, 6)])
mapping = isomorphism.GraphMatcher(g, h)
print("\nAre g and h isomorphic?", mapping.is_isomorphic())

# 4. Paths, Walks, Cycles
print("\nAll Simple Paths from 0 to 3:", list(nx.all_simple_paths(g, 0, 3)))
print("Cycle basis of graph:", nx.cycle_basis(g))

# 5. Components
print("\nConnected Components:", list(nx.connected_components(g)))

# 6. Cut-Edges and Cut-Vertices
print("\nBridges (Cut-Edges):", list(nx.bridges(g)))
print("Articulation Points (Cut-Vertices):", list(nx.articulation_points(g)))

# 7. Bipartite Graph
B = nx.complete_bipartite_graph(2, 3)
print("\nIs Bipartite:", nx.is_bipartite(B))

# 8. Eulerian Graph
print("\nIs Eulerian:", nx.is_eulerian(g))

# 9. Vertex Degrees
print("\nVertex Degrees:", dict(g.degree()))

# 10. Degree Sequences
degree_sequence = sorted([d for n, d in g.degree()], reverse=True)
print("Degree Sequence:", degree_sequence)

# 11. Directed Graph
DG = nx.DiGraph()
DG.add_edges_from([(0, 1), (1, 2), (2, 0)])
print("\nDirected Graph Edges:", DG.edges())

# 12. de Bruijn Cycles
print("\nde Bruijn Graph for (k=2, n=3):")
db_graph = nx.de_bruijn_graph(2, 3)
print(db_graph.edges())

# 13. Orientations & Tournaments
tournament = nx.generators.tournament.random_tournament(5)
print("\nIs Tournament Strongly Connected?", nx.is_strongly_connected(tournament))

# 14. Extremal Problem Example (Turán graph: avoids K4 in a graph with n=7, r=3)
T = nx.complete_multipartite_graph(3, 2, 2)
print("\nTurán Graph (Extremal Example) Edges:", T.edges())

# 15. Reconstruction Conjecture (Conceptual)
print("\nReconstruction Conjecture is a theoretical concept — not algorithmically proven.")

# Optional: Draw a graph
nx.draw(g, with_labels=True)
plt.title("Graph Visualization")
plt.show()
