import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from PNL import *

df = pd.read_csv('essays.csv')
text = df.iloc[4]['text']

nodes = preprocessing_text(text)
edges = [[nodes[i], nodes[i+1]] for i in range(len(nodes)-1)]

G = nx.DiGraph()

G.add_nodes_from(nodes)
G.add_edges_from(edges)

edges_weight = dict((','.join(edge), edges.count(edge)) for edge in edges) # peso das arestas

for u, v, d in G.edges(data=True):
    d['weight'] = edges_weight[f'{u},{v}']

out_degrees = dict(G.out_degree(G.nodes(), 'weight'))
mean_out_degrees = np.mean(list(out_degrees.values()))
print(f'mean outdegree: {mean_out_degrees}')

in_degrees = dict(G.in_degree(G.nodes(), 'weight'))
mean_in_degrees = np.mean(list(in_degrees.values()))
print(f'mean indegree: {mean_in_degrees}')

clustering_coefficient = nx.clustering(G, G.nodes(), 'weight')           
mean_clustering_coefficient = np.mean(list(clustering_coefficient.values()))
print(f'mean clustering coefficient: {mean_clustering_coefficient}')

average_shortest_path_weight = nx.average_shortest_path_length(G, 'weight')
print(f'mean shortest path length weighted: {average_shortest_path_weight}')

average_shortest_path = nx.average_shortest_path_length(G)
print(f'mean shortest path length unweighted: {average_shortest_path}')

# nx.draw(G, with_labels=True, font_size='x-small')
# plt.show()
