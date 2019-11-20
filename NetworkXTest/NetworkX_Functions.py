import networkx as nx
G = nx.Graph()
""""
G.add_edge('A', 'B', weight=4)
G.add_edge('B', 'D', weight=2)
G.add_edge('A', 'C', weight=3)
G.add_edge('C', 'D', weight=4)
print(nx.shortest_path(G, 'A', 'D', weight='weight'))
"""

# Can add nodes individually or through a list
G.add_node(1)
G.add_nodes_from([2, 3])

# Can do the same for edges
G.add_edges_from([(1, 2), (1, 3)])
e = (2, 3)
G.add_edge(*e) # unpack edge tuple*

# Note the difference between adding a string and multiple chars
G.add_node("spam")        # adds node "spam"
G.add_nodes_from("spam")  # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'm')

# We can see how many nodes and which edges are currently present in our graph
print(G.number_of_nodes())
print(G.number_of_edges())

print(list(G.nodes))
print(list(G.edges))
print(list(G.adj[1]), "\n") # or list(G.neighbors(1))

G[1][3]['color'] = "blue"
G.edges[1, 2]['color'] = "red"

# Can easily remove nodes just like how we add them
G.remove_node(2)
G.remove_nodes_from("spam")
G.remove_edge(1, 3)
print(list(G.nodes))
print(list(G.edges), "\n")

# Directed Graphs is more of what want, especially for causal modeling
DG = nx.DiGraph()
DG.clear()
DG.add_weighted_edges_from([("Asia", "Cancer", 0.5), ("Wealth", "Asia", 0.75)])
print(DG.out_degree("Asia", weight='weight'))
print(DG.degree("Asia", weight='weight')) # total weight of edges for node 1
print(list(DG.successors("Asia")))
print(list(DG.neighbors("Asia")))

# Writes the gml file for us easily
nx.write_gml(DG, "test.gml")