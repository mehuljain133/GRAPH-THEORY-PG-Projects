# Unit-V Graph Coloring: Vertex colorings, bounds on chromatic numbers, Chromatic numbers of graphs constructed from smaller graphs, chromatic polynomials, properties of the chromatic polynomial, the deletion-contraction recurrence. 

import networkx as nx
import matplotlib.pyplot as plt
from sympy import symbols, simplify

print("### UNIT-V: Graph Coloring ###\n")

# 1. Vertex Coloring Example (Greedy)
G = nx.cycle_graph(5)
coloring = nx.coloring.greedy_color(G, strategy='largest_first')
print("1. Vertex coloring (greedy):", coloring)

# Chromatic number lower bound (max clique size)
cliques = list(nx.find_cliques(G))
max_clique_size = max(len(c) for c in cliques)
print("Lower bound on chromatic number (clique number):", max_clique_size)

# Chromatic number upper bound (max degree + 1)
max_degree = max(dict(G.degree()).values())
upper_bound = max_degree + 1
print("Upper bound on chromatic number (max degree + 1):", upper_bound)

# Chromatic number from coloring
chromatic_number = max(coloring.values()) + 1
print("Chromatic number found by greedy:", chromatic_number)

# 2. Chromatic Number of Combined Graphs
print("\n2. Chromatic number of combined graphs:")

# Create two graphs and combine
H1 = nx.complete_graph(3)
H2 = nx.path_graph(3)
H = nx.disjoint_union(H1, H2)

coloring_H = nx.coloring.greedy_color(H, strategy='largest_first')
chrom_num_H = max(coloring_H.values()) + 1
print("Chromatic number of combined graph:", chrom_num_H)

# 3. Chromatic Polynomial - via Deletion-Contraction recurrence

def chromatic_polynomial(G, x):
    if G.number_of_edges() == 0:
        # If no edges, chromatic polynomial = x^n (all vertices can be colored independently)
        return x ** G.number_of_nodes()
    else:
        # Pick an edge
        u, v = next(iter(G.edges()))
        G1 = G.copy()
        G1.remove_edge(u, v)          # Deletion
        G2 = nx.contracted_nodes(G.copy(), u, v, self_loops=False)  # Contraction

        return chromatic_polynomial(G1, x) - chromatic_polynomial(G2, x)

x = symbols('x')
print("\n3. Chromatic polynomial of cycle graph C4:")
C4 = nx.cycle_graph(4)
poly = chromatic_polynomial(C4, x)
print("Chromatic Polynomial P(G, x) =", simplify(poly))

# 4. Properties of chromatic polynomial:
print("\n4. Properties demonstration:")
print("- Degree =", poly.as_poly().degree())
print("- Leading coefficient =", poly.as_poly().LC())
print("- Coefficients =", poly.as_poly().all_coeffs())

# 5. Deletion-Contraction recurrence example
print("\n5. Deletion-Contraction recurrence steps on C4:")
print("P(G, x) = P(G - e, x) - P(G / e, x)")

e = next(iter(C4.edges()))
print(f"Choose edge: {e}")
G_del = C4.copy()
G_del.remove_edge(*e)
G_contr = nx.contracted_nodes(C4.copy(), e[0], e[1], self_loops=False)
print(f"P(G - e, x) = {simplify(chromatic_polynomial(G_del, x))}")
print(f"P(G / e, x) = {simplify(chromatic_polynomial(G_contr, x))}")

# Visualization
nx.draw(C4, with_labels=True, node_color='lightcoral')
plt.title("Cycle Graph C4")
plt.show()
