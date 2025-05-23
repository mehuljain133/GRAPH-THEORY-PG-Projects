# Unit-IV Connectivity and Paths: Blocks, k-connected graphs, Menger’s theorem, line graphs, network flow problems, flows and source/sink cuts, Ford-Fulkerson algorithm, Max-flow min-cut theorem

import networkx as nx
import matplotlib.pyplot as plt

print("### UNIT-IV: Connectivity and Paths ###\n")

# Sample graph
G = nx.Graph()
edges = [(1,2), (2,3), (3,4), (4,1), (2,4), (3,5), (5,6)]
G.add_edges_from(edges)
print("Graph edges:", G.edges())

# 1. Blocks - biconnected components
print("\n1. Blocks (Biconnected components):")
blocks = list(nx.biconnected_components(G))
print("Biconnected components:", blocks)

# 2. k-connected graphs
k = 2
print(f"\n2. Is graph {k}-connected?")
is_k_connected = nx.is_k_edge_connected(G, k) and nx.is_k_node_connected(G, k)
print(is_k_connected)

# 3. Menger’s theorem (vertex connectivity)
print("\n3. Menger’s theorem example (vertex connectivity between 1 and 5):")
vertex_connectivity = nx.node_connectivity(G, s=1, t=5)
print("Vertex connectivity (min vertex cut size) between 1 and 5:", vertex_connectivity)

# 4. Line Graph
print("\n4. Line Graph of G:")
L = nx.line_graph(G)
print("Line graph nodes:", L.nodes())
print("Line graph edges:", L.edges())

# 5. Network Flow Problems - create directed graph with capacities
DG = nx.DiGraph()
DG.add_edge('s', 'a', capacity=10)
DG.add_edge('s', 'b', capacity=5)
DG.add_edge('a', 'b', capacity=15)
DG.add_edge('a', 't', capacity=10)
DG.add_edge('b', 't', capacity=10)
print("\n5. Network flow graph edges with capacities:")
for u,v,data in DG.edges(data=True):
    print(f"{u}->{v} capacity={data['capacity']}")

# 6. Ford-Fulkerson Max Flow
print("\n6. Ford-Fulkerson max flow from 's' to 't':")
flow_value, flow_dict = nx.maximum_flow(DG, 's', 't', flow_func=nx.algorithms.flow.edmonds_karp)
print("Max flow value:", flow_value)
print("Flow per edge:", flow_dict)

# 7. Max-flow min-cut theorem
print("\n7. Min-cut corresponding to max flow:")
cut_value, (reachable, non_reachable) = nx.minimum_cut(DG, 's', 't')
print("Min-cut value:", cut_value)
print("Reachable nodes from source in residual graph:", reachable)
print("Non-reachable nodes:", non_reachable)

# Visualization: original graph
plt.figure(figsize=(8,6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='black', node_size=500)
plt.title("Original Graph G")
plt.show()

# Visualization: flow graph with capacities
plt.figure(figsize=(8,6))
pos = nx.spring_layout(DG)
edge_labels = {(u, v): d['capacity'] for u, v, d in DG.edges(data=True)}
nx.draw(DG, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=600, arrowsize=20)
nx.draw_networkx_edge_labels(DG, pos, edge_labels=edge_labels)
plt.title("Flow Network with Capacities")
plt.show()
