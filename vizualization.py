import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/network_data.csv')

corr = df.corr()
sns.heatmap(corr, annot=True, annot_kws={"fontsize":5})
sns.set_theme(color_codes=True)
plt.title("Matriz de Correlação")
plt.savefig("vizualization/correlation.png")

scores = list(df.columns[:6])
properties = list(df.columns[6:])

for score in scores:

    fig, axs = plt.subplots(6, 2, figsize=(10, 18)) 
    fig.subplots_adjust(0.125, 0.1, 0.9, 0.9, 0.4, 0.4)
    
    for prop, ax in zip(properties, axs.ravel()):

        sns.regplot(ax=ax, data=df, x=df[score], y=df[prop], line_kws={"color":"yellow"})
        ax.set(xlabel=score, ylabel=prop)
        plt.rcParams.update({'figure.max_open_warning': 0})
        fig.savefig(f"vizualization/{score}.png")
