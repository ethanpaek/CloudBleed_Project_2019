import networkx as nx
import matplotlib.pyplot as plt
from random import random
# Directed Graphs is more of what want, especially for causal modeling
DG = nx.DiGraph()

DG.add_weighted_edges_from([("Hacked", "Bug", random()),
                            ("Malware", "Bug", random()),
                            ("Hacked", "Outcome", random()),
                            ("Malware", "Outcome", random()),
                            ("Bug", "Outcome", random()),
                            ("Physical", "Outcome", random()),
                            ("Misuse", "Outcome", random()),
                            ("Error", "Outcome", random()),
                            ("Environment", "Outcome", random()),
                            ("Social", "Outcome", random())
                            ])
print(DG.out_degree("Hacked", weight='weight'))
print(DG.degree("Bug", weight='weight')) # total weight of edges for node "Bug"
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