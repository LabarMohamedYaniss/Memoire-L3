#K-means
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
df = pd.read_excel(r'C:\Users\PC\Desktop\BDD.xlsx')
wmax = df.set_index('Date').resample('1D').max()
df2 = wmax.loc['2018-01-01':'2018-12-31', :]
df3 = wmax.loc[:, '1h':'24h']
kmeans = KMeans(n_clusters=4).fit(df2)
centroids = kmeans.cluster_centers_
df2['kmeans_4'] = kmeans.labels_

nbjour = df2.pivot_table(index = ['kmeans_4'], aggfunc ='size')


print(nbjour)

plt.scatter(df2.index, df2['kmeans_4'], s=1)

plt.show()
