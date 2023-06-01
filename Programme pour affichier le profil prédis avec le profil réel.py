#Programme pour affichier le profil prédis avec le profil réel
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

y1 = 11394.82629108 
y2 = 15535.06103286 
t1 = 2014
t2 = 2019
t3 = 2020
a = ((y2 - y1)/(t2 - t1))

print(a)
b = y2-(a*t2)
print(b)
y3 = (a*t3) + b
print(y3)
df = pd.read_excel(r'C:\Users\PC\Desktop\BDD.xlsx')



wmax = df.set_index('Date').resample('1D').max()

dss = wmax.loc['2019-01-01':'2019-12-31', :]

db = dss.max(axis=1)

print(dss)
print(db)
f = db.max(axis=0)
f2 = db.div(f)
print(f)
print(f2)
f3 = (dss/f)
print(f3)
f4 = f3*y3
print(f4)
f5 = f4.loc['2019-10-07', :]
f6 = wmax.loc['2020-01-04', :]
f7 = f4.loc['2019-10-09', :]
f8 = f4.loc['2019-10-10', :]

ff = f4.reset_index()
print(ff)

ff['dayOfWeek'] = ff['Date'].dt.day_name()
print(ff)
fff = ff.loc[ff['dayOfWeek'].isin(['Friday'])]
ffs = ff.loc[ff['dayOfWeek'].isin(['Saturday'])]
ffo = ff.loc[~ff['dayOfWeek'].isin(['Saturday','Friday' ])]
print(fff)
print(ffs)
print(ffo)

del fff["dayOfWeek"]
del ffs["dayOfWeek"]
del ffo["dayOfWeek"]

v = fff.set_index('Date').resample('1D').max()
s = ffs.set_index('Date').resample('1D').max()
o = ffo.set_index('Date').resample('1D').max()
oo = o.loc['2019-01-13':'2019-01-17']
oo = oo.dropna(axis=0)

h = s.loc['2019-01-01':'2019-03-31', :]
h = h.dropna(axis=0)
print('separation')
print(h)
jan = s.loc['2019-01-01':'2019-01-31', :]
jan = jan.dropna(axis=0)
week = f4.loc['2019-01-15':'2019-12-21', :]
week = week.dropna(axis=0)
h4 = f4.loc['2019-01-01':'2019-12-31', :]
h8 = s.loc['2019-12-19':'2019-12-31', :]
h8 = h8.dropna(axis=0)
win = h.combine_first(h8)
real = wmax.loc['2020-01-23', :]

print(win)
win2 = win.mean()
print(win2)
print(jan)
jan2 = jan.mean()
print(jan2)
oo2 = oo.mean()



ax = real.plot()




win2.plot(ax=ax)
plt.show()



