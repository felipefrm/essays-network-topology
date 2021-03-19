import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from PNL import *

df = pd.read_csv('data/essays.csv')
df_save = pd.DataFrame(columns=['final_score','criteria_scores','out_degrees','clustering_coefficient','shortest_path_lenght','shortest_path_lenght_weighted'])

for index in range(len(df)):

    text = df.iloc[index]['text']
    nodes = preprocessing_text(text)
    edges = [[nodes[i], nodes[i+1]] for i in range(len(nodes)-1)]

    G = nx.DiGraph()

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    edges_weight = dict((','.join(edge), edges.count(edge)) for edge in edges) 

    for u, v, d in G.edges(data=True):
        d['weight'] = edges_weight[f'{u},{v}']

    out_degrees = dict(G.out_degree(G.nodes(), 'weight'))
    mean_out_degrees = np.mean(list(out_degrees.values()))
    print(f'mean outdegree: {mean_out_degrees}')

    # in_degrees = dict(G.in_degree(G.nodes(), 'weight'))
    # mean_in_degrees = np.mean(list(in_degrees.values()))
    # print(f'mean indegree: {mean_in_degrees}')

    clustering_coefficient = nx.clustering(G, G.nodes(), 'weight')           
    mean_clustering_coefficient = np.mean(list(clustering_coefficient.values()))
    print(f'mean clustering coefficient: {mean_clustering_coefficient}')

    average_shortest_path_weight = nx.average_shortest_path_length(G, 'weight')
    print(f'mean shortest path length weighted: {average_shortest_path_weight}')

    average_shortest_path = nx.average_shortest_path_length(G)
    print(f'mean shortest path length unweighted: {average_shortest_path}')

    print(index)

    df_save.loc[index] = [df.iloc[index]['final_score'], dict(df.iloc[index]['criteria_scores']) ,mean_out_degrees, mean_clustering_coefficient, average_shortest_path, average_shortest_path_weight]

# nx.draw(G, with_labels=True, font_size='x-small')
# plt.show()
# plt.savefig("Graph.png", format="PNG")

df_save.to_csv(r'data/network_data.csv', header=True)