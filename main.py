import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from PNL import *

df = pd.read_csv('essays.csv')
text = df.iloc[4]['text']

words = preprocessing_text(text)
words_link = [[words[i], words[i+1]] for i in range(len(words)-1)]

G = nx.DiGraph()

G.add_nodes_from(words)
G.add_edges_from(words_link)

# links_weight = Counter(words_link)  # Contains frequencies of each directed edge.
# links_weight = [[link, words_link.count(link)] for link in words_link]

links_weight = dict((','.join(links), words_link.count(links)) for links in words_link) # peso das arestas
# words_link = [list(item) for item in set(tuple(row) for row in words_link)]

# print(len(links_weight))
# print(len(words_link))
# print(len(list(G.edges)))

for u, v, d in G.edges(data=True):
    d['weight'] = links_weight[f'{u},{v}']

print(G.out_degree('escol'))    # deveria ser 9
print(G.in_degree('escol'))     # deveria ser 9

print(G.out_degree(G.nodes()))      # tem que considerar o peso das arestas
print(G.in_degree(G.nodes()))       # tem que considerar o peso das arestas
print(nx.clustering(G))             # tem que considerar o peso das arestas

nx.draw(G, with_labels=True, font_size='x-small')
plt.show()
