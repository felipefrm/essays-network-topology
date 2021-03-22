import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/network_data.csv')

scores = list(df.columns[:6])
properties = list(df.columns[6:])

corr = df.corr()
sns.heatmap(corr, annot=True)
plt.savefig("vizualization/correlation.png")

for score in scores:
    for prop in properties:
        plt.rcParams.update({'figure.max_open_warning': 0})
        fig = plt.figure(figsize=(6, 4))
        if score not in 'final_score':
            plt.yticks(np.arange(0, 201, 50))
        sns.scatterplot(data=df, x=df[prop], y=df[score], hue=df[score], palette='coolwarm_r', legend = False)
        fig.savefig(f"vizualization/{score}:{prop}.png")