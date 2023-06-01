#Regression linéaire
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
df = pd.read_excel(r'C:\Users\PC\Desktop\BDD.xlsx')
df2 = df.set_index('Date').resample('1Y').max()
df3 = df2.max(axis=1)
df4 = pd.DataFrame(df3).reset_index()
df4.columns = ['Date', 'Max Consomation']

df4['Year'] = df4['Date'].dt.strftime('%Y')
del df4["Date"]

df4 = df4.drop(df4.index[12])

df4['Year'] = df4.Year.astype(int)
X = df4.iloc[:,1].values
y = df4.iloc[:,:-1].values
X = X.reshape(12, 1)
print(X.shape)
print(y.shape)
print(X)
print(y)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/3,random_state=0)
regressor = LinearRegression()
regressor.fit(X_train,y_train)
y_pred = regressor.predict(X_test)
print(X_test)
print(y_test)
 
print(y_pred)
plt.scatter(X_train, y_train, color='red') # plotting the observation line
 
plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line
 
plt.title("(Training set)") # stating the title of the graph
 
plt.xlabel("Years") # adding the name of x-axis
plt.ylabel("Consomation max") # adding the name of y-axis
plt.show() 

plt.scatter(X_test, y_test, color='red') 
plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line
 
plt.title("(Testing set)")
 
plt.xlabel("Years ") 
plt.ylabel("Consomation max") 
plt.show()
