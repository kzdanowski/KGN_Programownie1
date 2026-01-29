import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych z pliku CSV
titanic_df = sns.load_dataset('titanic')
# Wyświetlenie pierwszych kilku wierszy danych
print("Pierwsze kilka wierszy danych Titanic:")
print(titanic_df.head())
print("\n")
input()

# Informacje o DataFrame
print("Informacje o DataFrame Titanic:") 
print(titanic_df.shape)  
print(titanic_df.columns)  
print(titanic_df.info())
print("\n")
input()

# Podstawowe statystyki opisowe
print("Podstawowe statystyki opisowe dla danych Titanic:")
print(titanic_df.describe())
print("\n")
input()

# Sprawdzenie brakujących wartości
print("Liczba brakujących wartości w każdej kolumnie:")     
print(titanic_df.isnull().sum())
print("\n")
input()

# Ile osób przeżyło, a ile nie
survival_counts = titanic_df['survived'].value_counts()
print("Liczba przeżyłych i zmarłych pasażerów:")
print(survival_counts)
print("\n")
input()

survival_rate = titanic_df["survived"].mean() * 100
print("Przeżywalność:", survival_rate, "%")

print(titanic_df.groupby("sex")["survived"].mean() * 100)


# Wykres liczby przeżyłych i zmarłych pasażerów
# plt.figure(figsize=(8, 5))
# sns.countplot(x='survived', data=titanic_df)
# plt.title('Liczba przeżyłych i zmarłych pasażerów Titanica')
# plt.xlabel('Przeżył (1) / Nie przeżył (0)')
# plt.ylabel('Liczba pasażerów')
# plt.show()

# Braki
print("Liczba brakujących wartości w każdej kolumnie:")
print(titanic_df.isnull().sum())
print("\n")
input()

# Średnia wartość wieku pasażerów którzy przeżyli
mean_age_survived = titanic_df[titanic_df['survived'] == 1]['age'].mean()
print(f"Średnia wartość wieku pasażerów którzy przeżyli: {mean_age_survived}")  
input()

# Cena biletu dla pasażerów którzy przeżyli
mean_fare_survived = titanic_df[titanic_df['survived'] == 1]['fare'].mean()
print(f"Średnia cena biletu dla pasażerów którzy przeżyli: {mean_fare_survived}")  
print(f"Korelacja między ceną biletu a przeżyciem: {titanic_df['fare'].corr(titanic_df['survived'])}")
input() 



# Uzupełnianie braków w kolumnie 'age' średnią wartością wieku
titanic_df['age'].fillna(titanic_df['age'].mean(), inplace=True)
print("Liczba brakujących wartości w kolumnie 'age' po uzupełnieniu:")
print(titanic_df['age'].isnull().sum()) 

# Tworzenie Series z kolumny 'age'
age_series = Series(titanic_df['age'])
print("Series z kolumny 'age':")
print(age_series)
print("\n")
# Podstawowe statystyki opisowe dla wieku
print("Statystyki opisowe dla wieku:")
print(age_series.describe())
print("\n")
# Wykres rozkładu wieku pasażerów
plt.figure(figsize=(10, 6))
sns.histplot(age_series.dropna(), bins=30, kde=True)
plt.title('Rozkład wieku pasażerów Titanica')
plt.xlabel('Wiek')
plt.ylabel('Liczba pasażerów')
plt.show()
# Tworzenie Series z kolumny 'fare'
fare_series = Series(titanic_df['fare'])

print("Series z kolumny 'fare':")
print(fare_series)
print("\n")
# Podstawowe statystyki opisowe dla opłaty za bilet
print("Statystyki opisowe dla opłaty za bilet:")
print(fare_series.describe())
print("\n")
# Wykres rozkładu opłaty za bilet
plt.figure(figsize=(10, 6))
sns.histplot(fare_series.dropna(), bins=30, kde=True)
plt.title('Rozkład opłaty za bilet na Titanica')
plt.xlabel('Opłata za bilet')
plt.ylabel('Liczba pasażerów')
plt.show()
# Analiza zależności między wiekiem a opłatą za bilet
plt.figure(figsize=(10, 6))
sns.scatterplot(x=age_series, y=fare_series)


plt.title('Zależność między wiekiem a opłatą za bilet')
plt.xlabel('Wiek')
plt.ylabel('Opłata za bilet')
plt.show()
# Obliczenie korelacji między wiekiem a opłatą za bilet
correlation = age_series.corr(fare_series)
print(f"Korelacja między wiekiem a opłatą za bilet: {correlation}") 
