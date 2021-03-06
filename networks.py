import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from PNL import *
from progress.bar import Bar
from ast import literal_eval

df = pd.read_csv('data/essays.csv')

df_save = pd.DataFrame(columns=['final_score','c1', 'c2', 'c3', 'c4', 'c5', 
'nodes', 'edges', 'out_degrees','clustering_coefficient','shortest_path_lenght',
'shortest_path_lenght_inverse_weighted', 'assortativity', 'density', 'degree_centrality',
'betweenness_centrality', 'closeness_centrality', 'pagerank'])

bar = Bar('Processing', max=len(df))
for index in range(len(df)):

    text = df.iloc[index]['text']
    nodes = preprocessing_text(text)
    edges = [[nodes[i], nodes[i+1]] for i in range(len(nodes)-1)]

    G = nx.DiGraph()

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    edges_weight = dict((','.join(edge), edges.count(edge)) for edge in edges) 
    max_weight = max(edges_weight.values())

    for u, v, d in G.edges(data=True):
        d['weight'] = edges_weight[f'{u},{v}']
        d['inverse_weight'] = 1 / edges_weight[f'{u},{v}']

    nodes_count = G.number_of_nodes()
    edges_count = G.number_of_edges()

    out_degrees = dict(G.out_degree(G.nodes(), 'weight'))
    mean_out_degrees = np.mean(list(out_degrees.values()))

    clustering_coefficient = nx.clustering(G, G.nodes())           
    mean_clustering_coefficient = np.mean(list(clustering_coefficient.values()))

    average_shortest_path_inverse_weight = nx.average_shortest_path_length(G, 'inverse_weight')

    average_shortest_path = nx.average_shortest_path_length(G)

    assortativity = nx.degree_assortativity_coefficient(G, x='out', y='out', weight='weight')
    
    density = nx.density(G)

    degree_centrality = nx.out_degree_centrality(G)
    mean_degree_centrality = np.mean(list(degree_centrality.values()))

    betweenness_centrality = nx.betweenness_centrality(G, endpoints=True)
    mean_betweenness_centrality = np.mean(list(betweenness_centrality.values()))

    closeness_centrality = nx.closeness_centrality(G)
    mean_closeness_centrality = np.mean(list(closeness_centrality.values()))

    pagerank = nx.pagerank(G, weight='weight')
    mean_pagerank = np.mean(list(pagerank.values()))

    criteria = literal_eval(df.iloc[index]['criteria_scores'])

    df_save.loc[index] = [df.iloc[index]['final_score'], criteria['Compet??ncia 1'], criteria['Compet??ncia 2'], criteria['Compet??ncia 3'], criteria['Compet??ncia 4'], criteria['Compet??ncia 5'], nodes_count, edges_count, mean_out_degrees, mean_clustering_coefficient, average_shortest_path, average_shortest_path_inverse_weight, assortativity, density, mean_degree_centrality, mean_betweenness_centrality, mean_closeness_centrality, mean_pagerank]
    
    bar.next()

df_save.to_csv(r'data/network_data.csv', header=True, index=False)

bar.finish()
