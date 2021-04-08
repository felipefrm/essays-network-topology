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


for i in range(1,11):
    medias = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for index in range(len(df)):
        if df.iloc[index]['final_score'] >= i*100 and df.iloc[index]['final_score'] < i*100 + 100:
            medias[0] = medias[0] + df.iloc[index]['final_score']
            medias[1] = medias[1] + 1
            medias[2] = medias[2] + df.iloc[index]['nodes']
            medias[3] = medias[3] + df.iloc[index]['edges']
            medias[4] = medias[4] + df.iloc[index]['out_degrees']
            medias[5] = medias[5] + df.iloc[index]['clustering_coefficient']
            medias[6] = medias[6] + df.iloc[index]['shortest_path_lenght']
            medias[7] = medias[7] + df.iloc[index]['shortest_path_lenght_inverse_weighted']
            medias[8] = medias[8] + df.iloc[index]['assortativity']
            medias[9] = medias[9] + df.iloc[index]['density']
            medias[10] = medias[10] + df.iloc[index]['degree_centrality']
            medias[11] = medias[11] + df.iloc[index]['betweenness_centrality']
            medias[12] = medias[12] + df.iloc[index]['closeness_centrality']
            medias[13] = medias[13] + df.iloc[index]['pagerank']
    
    df_save.loc[i] = [medias[0]/medias[1],medias[2]/medias[1],medias[3]/medias[1],medias[4]/medias[1],medias[5]/medias[1],medias[6]/medias[1],medias[7]/medias[1],medias[8]/medias[1],medias[9]/medias[1],medias[10]/medias[1],medias[11]/medias[1],medias[12]/medias[1],medias[13]/medias[1]]

df_save.to_csv(r'data/medias.csv', header=True, index=False)
# file1 = open('media.txt','a')
# file1.write(str(medias[0]/medias[1]) +', '+str(medias[1]) +', '+str(medias[2]/medias[1])+', '+str(medias[3]/medias[1])+', '+str(medias[4]/medias[1])+', '+str(medias[5]/medias[1])+', '+str(medias[6]/medias[1])+', '+str(medias[7]/medias[1])+', '+str(medias[8]/medias[1])+', '+str(medias[9]/medias[1])+', '+str(medias[10]/medias[1])+', '+str(medias[11]/medias[1])+', '+str(medias[12]/medias[1])+', '+str(medias[13]/medias[1])+'\n')
# file1.close()