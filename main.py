import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords
from string import punctuation
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('essays.csv')
text = df.iloc[4]['text']

words = word_tokenize(text.lower())

punctuation_list = list(punctuation)
punctuation_list.extend(["''", "``"])

stemmer = RSLPStemmer()

stopwords = set(stopwords.words('portuguese') + punctuation_list)
words_filtered = [stemmer.stem(word) for word in words if word not in stopwords]

edges_list = []
for i in range(len(words_filtered)-1):
    edges_list.append([words_filtered[i], words_filtered[i+1]])

G = nx.Graph()
G.add_nodes_from(words_filtered)
G.add_edges_from(edges_list)

nx.draw(G, with_labels=True, font_size='x-small')
plt.show()
