#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
print(np.arange(10))
print(np.arange(10) * 3)
print(np.array([1, 2, 3, 4, 5, 10]).mean())     #.mean = durschnittswert berechnen
print(np.array([1, 2, 3, 4, 5, 10]).min())      #.min = minimaler wert
print(np.array([1, 2, 3, 4, 5, 10]).max())      #.max = maximaler wert
print(np.array([1, 2, 3, 4, 5, 10]).std())      #.std = standard abweichung

xs = np.arange(10)
ys = xs ** 2

plt.plot(xs, ys)
#plt.show()

a = np.array([1, 2, 3, 4])
b = np.array([False, True, True, False])
print(a[b])         #Filtermöglichkeit nur wo true drin steht
print(a[a >= 3])    # Filtermöglickeit gibt an ob ein Element größergleich 3 ist

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(a.reshape(2,4))       #  zwei zeilen mit spalten mit 4 einträgen
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.reshape(6))
print(b.shape)          # Wie viele zeilen spalten hat das array?

class MyArray():
    def __init__(self, liste):
        self.liste = liste

    def __mul__(self, other):
        nliste = []
        for element in self.liste:
            nliste.append(element* other)
        return MyArray(nliste)

a = MyArray([1, 2, 3])
b = a.__mul__(2) # ist das gleiche wie b = a * 2 da eine def __mul__ gibt
b = a * 2
print(a.liste)
print(b.liste)




















































#