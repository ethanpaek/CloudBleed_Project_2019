import networkx as nx
import matplotlib.pyplot as plt
from random import random
# Directed Graphs is more of what want, especially for causal modeling
DG = nx.DiGraph()

DG.add_weighted_edges_from([("action.Hacking", "action.Bugs", random()),
                            ("action.Malware", "action.Bugs", random()),
                            ("action.Hacking", "action.Impact", random()),
                            ("action.Malware", "action.Impact", random()),
                            ("action.Bugs", "action.Impact", random()),
                            ("action.Physical", "action.Impact", random()),
                            ("action.Misuse", "action.Impact", random()),
                            ("action.Error", "action.Impact", random()),
                            ("action.Environmental", "action.Impact", random()),
                            ("action.Social", "action.Impact", random())
                            ])
print(DG.out_degree("action.Bugs", weight='weight')) # total weight of edges directing out of "Bug" node
print(DG.degree("action.Bugs", weight='weight')) # total weight of edges coming in and out of "Bug" node
print(list(DG.successors("action.Hacking")))
print(list(DG.neighbors("action.Bugs")))

# Writes the gml file for us easily
nx.write_gml(DG, "test.gml")

#Drawing the graph with the Network X draw library
options = {
    'node_size': 1000000
}
nx.draw(DG, with_labels=True)

plt.savefig("DirectedGraph.png")