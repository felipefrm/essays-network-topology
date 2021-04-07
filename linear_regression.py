import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


df = pd.read_csv('data/network_data.csv').sample(frac=1)

y = df['c2']
x = df[['nodes', 'edges', 'out_degrees','clustering_coefficient','shortest_path_lenght',
'shortest_path_lenght_inverse_weighted', 'assortativity', 'density', 'degree_centrality',
'betweenness_centrality', 'closeness_centrality', 'pagerank']]

train_percentage = 0.75

separator = int(len(df) * train_percentage)

y_train = y[:separator]
x_train = x[:separator]
y_test = y[separator:]
x_test = x[separator:]

regression = linear_model.LinearRegression()

regression.fit(x_train, y_train)
predict = regression.predict(x_test)

# The coefficients
print('Coefficients: \n', regression.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(y_test, predict))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(y_test, predict))

# #Saving the results
df_prediction = pd.DataFrame(columns=['final_score','predict'])

for i in range(0, len(y_test)):
   df_prediction.loc[i] = [y_test.iloc[i], predict[i]]

df_prediction.to_csv(r'data/prediction.csv', header=True, index=False)
