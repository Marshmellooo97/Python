import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("C:/Users/justi/Documents/Codes/Pyton/Kursmaterialien-2019/Kursmaterialien/data/astronauts.csv")
# bei excel Tabellen  df = pd.read_csv("C:/......csv" , delimiter = ";")
print(df)
df.head()
print(len(df))
print(df["Name"])  # auf eine Spalte zugreifen
print(df.iloc[0])   # auf eine zeile "0" zugreifen
entry = df.iloc[0]
print(entry["Name"])    # Nur der Name wird ausgeben

print("Absatz")
for row in df.iterrows():
    pos = row[0]
    d = row[1]
    print(pos)
    print(d["Name"])
    break

#Daten Filtern
print(df["Year"] < 1990) # Abfrage kleiner als 1990 Antwort True oder False
print(df[df["Year"] < 1960]) # Alle die kleiner sind werden aus der Liste entfernt

# Sotieren
df2 = df.sort_values("Name", ascending= False)    # Daten Sotieren nach Name ascending = Sotierung absteigend
print(df2)
for name in df2["Name"]:
    print(name)

#Ecxel einlesen

df = pd.read_excel("C:/Users/justi/Documents/Codes/Pyton/Kursmaterialien-2019/Kursmaterialien/18 - DataScience - Stack/daten.xlsx")
print(df)
year = df["Jahr"]
sales = df["Umsatz"]
print(year)

plt.plot(year, sales)
plt.show()


# Aufgabe

name = "Anna"
gender = "F"
state = "CA"
# x =  jahre   y =  wie oft der name














































#