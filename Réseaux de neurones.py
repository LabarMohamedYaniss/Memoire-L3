#Réseaux de neurones
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import pandas as pd  
df = pd.ExcelFile(r'C:\Users\HP\Desktop\Cours2\Test\BDD3.xlsx')
print(df.sheet_names)
y= df[['1h','2h','3h','4h','5h','6h','7h','8h','9h','10h','11h','12h','13h','14h','15h','16h','17h','18h','19h','20h','21h','22h','23h','24h']].values
X=df[['1h','2h','3h','4h','5h','6h','7h','8h','9h','10h','11h','12h','13h','14h','15h','16h','17h','18h','19h','20h','21h','22h','23h','24h']].values
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,y,test_size=0.2)
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()
# Première couche
model.add(Dense(10, input_dim=24,activation="relu"))

# Couches cachées

model.add(Dense(20,activation="relu"))


# Sortie du modèle
model.add(Dense(24))

model.compile(optimizer='adam',loss='mean_squared_error',metrics=["mape"])
model.fit(X_train,Y_train,batch_size=364,epochs=200)
performance = model.evaluate(X_test,Y_test,verbose=0)[1]
print("La performance du modèle est : {} % MAPE".format(performance))