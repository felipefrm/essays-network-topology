import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from PNL import *
from progress.bar import Bar
from ast import literal_eval

df = pd.read_csv('data/network_data.csv')

df_save = pd.DataFrame(columns=['final_score','nodes', 'edges', 'out_degrees','clustering_coefficient','shortest_path_lenght',
'shortest_path_lenght_inverse_weighted', 'assortativity', 'density', 'degree_centrality',
'betweenness_centrality', 'closeness_centrality', 'pagerank'])

for i in range(10):
    means = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for index in range(len(df)):
        if df.iloc[index]['final_score'] > i*100 and df.iloc[index]['final_score'] <= i*100 + 100:
            means[1] = means[1] + 1
            means[0] = means[0] + df.iloc[index]['final_score']
            means[2] = means[2] + df.iloc[index]['nodes']
            means[3] = means[3] + df.iloc[index]['edges']
            means[4] = means[4] + df.iloc[index]['out_degrees']
            means[5] = means[5] + df.iloc[index]['clustering_coefficient']
            means[6] = means[6] + df.iloc[index]['shortest_path_lenght']
            means[7] = means[7] + df.iloc[index]['shortest_path_lenght_inverse_weighted']
            means[8] = means[8] + df.iloc[index]['assortativity']
            means[9] = means[9] + df.iloc[index]['density']
            means[10] = means[10] + df.iloc[index]['degree_centrality']
            means[11] = means[11] + df.iloc[index]['betweenness_centrality']
            means[12] = means[12] + df.iloc[index]['closeness_centrality']
            means[13] = means[13] + df.iloc[index]['pagerank']
    
    df_save.loc[i] = [means[0]/means[1],means[2]/means[1],means[3]/means[1],means[4]/means[1],means[5]/means[1],means[6]/means[1],means[7]/means[1],means[8]/means[1],means[9]/means[1],means[10]/means[1],means[11]/means[1],means[12]/means[1],means[13]/means[1]]

df_save.to_csv(r'data/means.csv', header=True, index=False)
