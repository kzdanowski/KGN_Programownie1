import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns



# Tworzenie Series z danych słownikowych

data_dict = {'a': 10, 'b': 20, 'c': 30}
series_from_dict = Series(data_dict)        
print("Series z danych słownikowych:")
print(series_from_dict)
print(series_from_dict[0])
print(series_from_dict['a'])
print("\n")

# Uwaga.
# Można podać indeksy podczas tworzenia Series
s = pd.Series([10, 20, 30], index=[1, 2, 3])

# Wtedy może pojawić się niejasność przy dostępie do elementów
# - s[1] może oznaczać pierwszy element (o indeksie 0)
#  lub element o indeksie 1 (wartość 10)

# Aby to ujednoznacznić, używamy .loc (dla etykiet indeksów) 
#oraz .iloc (dla pozycji indeksów):  

print(s.loc[1])   # 10
print(s.iloc[0])  # 10

# Tworzenie Series z listy
data_list = [100, 200, 300, 400]
series_from_list = Series(data_list)
print("Series z listy:")
print(series_from_list)
print("\n")

# Tworzenie Series z wartości skalarnych
scalar_value = 500
series_from_scalar = Series(scalar_value, index=['x', 'y', 'z'])
print("Series z wartości skalarnych:")
print(series_from_scalar)   
print("\n")

# Tworzenie Series z pliku CSV
# (Zakładamy, że plik 'P1W12_data1.csv' istnieje w tym samym katalogu co skrypt)
# Przykładowa zawartość pliku 'data.csv':   
# Name,Age,City
# Alice,30,New York     
# Bob,25,Los Angeles
# Charlie,35,Chicago

df_csv = pd.read_csv('P1W12_data1.csv')
series_from_csv = Series(df_csv['Age'])
print("Series z pliku CSV:")
print(series_from_csv)
print("\n")    






# Tworzenie DataFrame z danych słownikowych
data = {
    'Kraj': ['Belgia', 'Indie', 'Brazylia'],
    'Stolica': ['Bruksela', 'New Delhi', 'Brasília'],
    'Populacja': [11908000, 1366000000, 213993437]
}       

df = DataFrame(data)
print("DataFrame z danych słownikowych:")
print(df)
print("\n")

# Tworzenie DataFrame z listy słowników
data_list = [
    {'Kraj': 'Belgia', 'Stolica': 'Bruksela', 'Populacja': 11908000},
    {'Kraj': 'Indie', 'Stolica': 'New Delhi', 'Populacja': 1366000000},
    {'Kraj': 'Brazylia', 'Stolica': 'Brasília', 'Populacja': 213993437}
]

df_list = DataFrame(data_list)
print("DataFrame z listy słowników:")
print(df_list)    


# Pobieranie danych z Federal Reserve
# Economic Data (FRED) i Yahoo Finance

import pandas_datareader.data as web
gs = web.get_data_fred('GS10')
import yfinance as yf
aapl = yf.download("AAPL", start="2025-01-01", end="2025-12-31")

aapl.info()
aapl.plot(y="Close")
# <Axes: xlabel='Date'>
plt.show()