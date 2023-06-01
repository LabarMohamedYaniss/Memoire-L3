#Code pour appliquer max prédis sur un model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel(r'C:\Users\PC\Desktop\BDD.xlsx')
y1 = 6492.03571429
y2 = 7278.85714286
t1 = 2008
t2 = 2009
t3 = 2019
a = ((y2 - y1)/(t2 - t1))

print(a)
b = y2-(a*t2)
print(b)
y3 = (a*t3) + b
print(y3)
v2 = 10761.110412
v3 = 10241.661999



wmax = df.set_index('Date').resample('1D').max()

dss = wmax.loc['2018-01-24':'2018-12-31', :]
db = dss.max()

print(dss)
print(db)

f2 = dss.div(db)

print(f2)
f3 = f2*v3
print(f3)
