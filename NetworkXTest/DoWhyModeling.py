import networkx as nx
import matplotlib.pyplot as plt
# Directed Graphs is more of what want, especially for causal modeling
DG = nx.DiGraph()

DG.add_weighted_edges_from([("Hacked", "Bug", 0.5),
                            ("Malware", "Bug", 0.75),
                            ("Hacked", "Outcome", 0.8),
                            ("Malware", "Outcome", 0.7),
                            ("Bug", "Outcome", 0.75),
                            ("Physical", "Outcome", 0.3),
                            ("Misuse", "Outcome", 0.5),
                            ("Error", "Outcome", 0.4),
                            ("Environment", "Outcome", 0.6),
                            ("Social", "Outcome", 0.2)
                            ])
print(DG.out_degree("Hacked", weight='weight'))
print(DG.degree("Bug", weight='weight')) # total weight of edges for node 1
print(list(DG.successors("Hacked")))
print(list(DG.neighbors("Bug")))

# Writes the gml file for us easily
nx.write_gml(DG, "test.gml")

#Drawing the graph with the Network X draw library
options = {
    'node_size': 1000000
}
nx.draw(DG, with_labels=True)

plt.savefig("DirectedGraph.png")