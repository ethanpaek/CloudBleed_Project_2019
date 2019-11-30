import networkx as nx
import matplotlib.pyplot as plt
from random import random
# Directed Graphs is more of what want, especially for causal modeling
DG = nx.DiGraph()

DG.add_weighted_edges_from([("Hacked", "Bug", random()),
                            ("Malware", "Bug", random()),
                            ("Bug", "Data Breach", random()),
                            ("Physical", "Data Breach", random()),
                            ("Misuse", "Data Breach", random()),
                            ("Error", "Data Breach", random()),
                            ("Environment", "Data Breach", random()),
                            ("Social", "Data Breach", random())
                            ])
print(DG.out_degree("Bug", weight='weight')) # total weight of edges directing out of "Bug" node
print(DG.degree("Bug", weight='weight')) # total weight of edges coming in and out of "Bug" node
print(list(DG.successors("Hacked")))
print(list(DG.neighbors("Bug")))

# Writes the gml file for us easily
nx.write_gml(DG, "InstrumentalTest.gml")

#Drawing the graph with the Network X draw library
options = {
    'node_size': 1000000
}
nx.draw(DG, with_labels=True)

plt.savefig("DirectedGraphWithInstrumentals.png")