import pandas as pd # ovaj modul će nam dati tabličnu struktura podacima i sve naše cijene i promjene ćemo unositi u njega

import datetime # ovim modulom ćemo s interneta  izvuči podatke i cijene o dionici
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from tkinter import *
import requests
from tkinter import ttk
import tkinter.font as tkFont
root = Tk()
font = tkFont.Font (family= "Helvetica", size=12, weight= "bold"  )
font2 = tkFont.Font (family= "Helvetica", size=9, weight= "normal"  )
root.title("Prediktor cijene dionica")
label1=Label(root, text= "Puno ime kompanije :",borderwidth=5, relief="groove",fg= 'blue', font = font2)
label2= Label(root, text = "Primjeri: Microsoft Corporation, Intel Corporation, Tesla, Inc." )
e = Entry(root, width=35,borderwidth=5, bg= "white",fg= "blue",)
e.grid(row=0, column=1, padx=10, pady=10)
a= ""                                                
def klik ():
    global a 
    a= e.get()
    root.destroy()
    


   
gumb= Button(root,text="Kliknite za predikciju", padx=100, pady= 25,command=klik, fg= 'blue', bg='dodger blue', font = font)
if __name__=="__klik__": 
    klik()
def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['name'] == symbol:
            return x['symbol']
label1.grid(row=0,column=0)
label2.grid(row=3,columnspan=3)
gumb.grid(row=2,sticky=N+S+E+W,columnspan=2)


root.mainloop()

e=get_symbol(a)


style.use('ggplot')


df = web.DataReader(e, 'yahoo')
df = df[['Open',  'High',  'Low',  'Close', 'Volume']]
df['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
df['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0

df = df[['Close', 'HL_PCT', 'PCT_change', 'Volume']]
forecast_col = 'Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]

df['Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.title(a)
plt.xlabel('Vrijeme')
plt.ylabel('Cijena')
plt.show()


print(df.tail())
