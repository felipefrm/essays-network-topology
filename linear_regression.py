import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('data/network_data.csv')
#print(df.head())
y = df['final_score']
x = df[['out_degrees','clustering_coefficient','shortest_path_lenght','shortest_path_lenght_weighted']]
w = df[['c1', 'c2', 'c3', 'c4', 'c5','out_degrees','clustering_coefficient','shortest_path_lenght','shortest_path_lenght_weighted']]

linear_regression = LinearRegression(normalize=True)
linear_regression2 = LinearRegression(normalize=True)

#Training the model
linear_regression.fit(x,y)
linear_regression2.fit(w,y)

#Predicting the final scores
pred = linear_regression.predict(x)
pred2 = linear_regression2.predict(w)

#Saving the results
df_prediction = pd.DataFrame(columns=['final_score','predict','predict_compt','out_degrees','clustering_coefficient','shortest_path_lenght','shortest_path_lenght_weighted'])

for i in range(0,len(y)):
   df_prediction.loc[i] = [y[i], pred[i], pred2[i], df.iloc[i]['out_degrees'], df.iloc[i]['clustering_coefficient'], df.iloc[i]['shortest_path_lenght'], df.iloc[i]['shortest_path_lenght_weighted']]

df_prediction.to_csv(r'data/prediction.csv', header=True, index=False)
