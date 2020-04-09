import pandas as pd # ovaj modul će nam dati tabličnu struktura podacima i sve naše cijene i promjene ćemo unositi u njega.

import datetime # ovim modulom ćemo odrediti vremenski interval koji promatramo.
import matplotlib.pyplot as plt # ovaj modul je za grafove
from matplotlib import style
import pandas_datareader.data as web # ovim modulom ćemo s interneta  izvuči podatke i cijene o dionici.
import math
import numpy as np # ovaj modul će nam biti potreban također za pohranjivanje podataka.
from sklearn import preprocessing, svm # ovim svim modulima dobivamo mogućnost da istreniramo stroj.
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


style.use('ggplot')  # stil grafa.


df = web.DataReader('UNG', 'yahoo')
df = df[['Open',  'High',  'Low',  'Close', 'Volume']]               # Ovim djelom smo definirali promjenu u postotku. Podatke smo uzeli s yahoo financa te smo ih pohranili ya koristiti.
df['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
df['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0
print(df.tail())

df = df[['Close', 'HL_PCT', 'PCT_change', 'Volume']]
forecast_col = 'Close'                                      # ovdje smanjujemo količinu podataka te nepotrebene podatke mičemo tako da su veliki negativan broj te ih onda stroj smatra kao nevažnim.
df.fillna(value=-99999, inplace=True)                                
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'], 1))                       # ovdje smo label koristili pretvorili u array.
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)   # ovdje je kod kojim računalo trenira s prijašnjim podacima. Ovdje počinje koristit regresijski algoritam.
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400                                                                # cijelim ovim djelom smo s obzirom na prijašnji dan procijenili sljedeći i tako dalje.
                                                                               # tako smo dobili više dana u budućnosti koji su svi pretpostavljeni s obzirom na prijašnje.
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)         # ovime smo namjestili graf.
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()




                    








