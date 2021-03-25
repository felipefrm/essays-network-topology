import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/network_data.csv')

corr = df.corr()
sns.heatmap(corr, annot=True, annot_kws={"fontsize":7})
plt.title("Matriz de Correlação")
plt.savefig("vizualization/correlation.png")

scores = list(df.columns[:6])
properties = list(df.columns[6:])

for score in scores:

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(18, 10))
    axs = [ax1, ax2, ax3, ax4]

    for prop, ax in zip(properties, axs):

        sns.scatterplot(ax=ax, data=df, x=df[prop], y=df[score], hue=df[score], palette='coolwarm_r', legend = False)
        ax.set(xlabel=prop, ylabel=score)
        ax.set_title(f'{score} / {prop}')    
        plt.rcParams.update({'figure.max_open_warning': 0})
        plt.title(f"{score}")
        fig.savefig(f"vizualization/{score}.png")
