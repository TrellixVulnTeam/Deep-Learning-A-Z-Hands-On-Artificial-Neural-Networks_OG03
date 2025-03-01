# Self Organizing Map

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Credit_Card_Applications.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

from sklearn.preprocessing import MinMaxScaler

sc = MinMaxScaler(feature_range = (0,1))#normalize(r)

X = sc.fit_transform(X)#normaliz(ing)

from minisom import MiniSom

som = MiniSom(x=10, y=10, input_len = 15, sigma = 1.0, learning_rate = 0.5)#x, y are map demensions: a map "x by y"

som.random_weights_init(X)

som.train_random(data=X, num_iteration=100)

from pylab import bone, pcolor, colorbar, plot, show

bone()
pcolor(som.distance_map().T)
colorbar()

markers = ['o', 's']

colors = ['r', 'g']


#for i in range(0, len(X)):
#    x = X[i]

for i, x in enumerate(X):
    
    w = som.winner(x)
    
    plot(w[0]+0.5, w[1]+0.5, markers[y[i]], markeredgecolor = colors[y[i]], markerfacecolor = 'None', markersize = 10, markeredgewidth = 2)
    
show()

mappings = som.win_map(X)

frauds = sc.inverse_transform(np.concatenate( (mappings[(8,1)], mappings[(6,8)]), axis=0))

#(8,1) and (6,8) are the coordinates of the "white" cells, that are "fraud(s)"
                                             

#frauds = np.concatenate( (mappings[(8,1)], mappings[(6,8)]), axis=0)#(8,1) and (6,8) are the coordinates of the "white" cells, that are "fraud(s)"
#frauds = sc.inverse_transform(frauds)