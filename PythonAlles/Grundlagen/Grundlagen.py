import sys

print(sys.version)

# Mathe
print("Hallo")      # Ausgeben Hallo 
Zahl = 5            # Zahl gleich 5 
print(Zahl)         # Ausgeben Zahl 
Zahl = 5 + 6           
print(Zahl)
Zahl = 5 - 6
print(Zahl)
Zahl = 5 * 6
print(Zahl)
Zahl = 5 / 6
print(Zahl)

# Ausgeben 
name = "Justin"     # Name Variable zuweisen 
alter = 22          # Alter Variable zuweisen 
print("Mein Name ist " + name + " und bin " + str(alter) + " Jahre alt")        # str(alter) da Zahl ausgeben 

# Liste
Studenten = ["S1" , "S2" , "S3" , "S4"]             # Liste 
print(Studenten)
Studenten.append ("S5")                             # Liste jemanden hinzufügen
Studenten.append ("S6")
print(Studenten)
print(len(Studenten))                               # Liste gesamtanzahl abfragen 
print(Studenten[0])                                 # Liste Nr1 Anzeigen 0=1
print(Studenten[5])
print(Studenten[0] + " und " + Studenten[5])        # Liste ausgeben Nr1 und Nr5
Studenten.pop()                                     # Löscht den letzten Eintrag "S6"
print(Studenten)
P = Studenten.pop()                                 # Löscht den letzten Eintrag "S5" und speichert ihn in P 
print(P)                                            # Gibt die Variable P aus 
a=110
b=80
print(a+b)                                  # Addition
c="110"
d="80.8"
print(int(c)+float(d))                      # Addition von String in Int+Float
age=21
print("Ich bin "+str(age) +" Jahre alt")

print("#".join(Studenten))                  # Ausgeben der Liste "xxx" verbindung zwischen den einzelnen Einträge
print(Studenten)                            # Liste einfach ausgegeben 
Studenten_String = (", ".join(Studenten))
print("In der Liste sind folgende Elemente: " + Studenten_String)   # Ausgabe liste in Variable speichern und ausgeben 
s = "Das ist ein Satz der besteht aus vielen Wörtern!"        
s = s.split(" ")            # Von string zu Liste 
print(s)
print(len(s))               # Ausgabe Liste wie viele Wörter stehen da drin 


# Schleifen abfragen 
a=13
if a < 11:
    print("Ja")
else: 
    print("Nein")

result = 5 < 6  # Abfragen = True oder False 
print( 5 <= 5 ) # kleiner gleich  
print( 5 >= 5 ) # größer gleich
print(result)   # = True
if result:      # If kennt True oder False
    print("ja")  

Wort = "Hallo" 
print("Hallo" == Wort) # Vergleicht auch str
print("Hallo" != Wort) # != Ungleich 
age=18
if age < 30 and age > 20:
    print("Zwischen 18 und 30")
else:
    age == 18 or age == 19
    print("18 oder 19")
if age != 23:
    print("er ist nicht 23")

print("S3" in Studenten)        # Ist S3 in der Liste Studenten
s = "Das ist ein Satz der besteht aus vielen Wörtern!" 
if "!" in s:
    print("Ja es ist ein ! enthalten")
else:
    print("Nein")

if "S8" not in s:
    print("S8 ist nicht in der Liste")

Sonderzeichen = "&"
if "!" == Sonderzeichen:        # Statts if if if elif übersichtlicher 
    print("!")
elif "$" == Sonderzeichen:
    print("§")
elif "&" == Sonderzeichen:
    print("&")
else: 
    print("Was anderes")

counter = 0

while counter < 10:     # solange bis bedingung erfüllt ist
    counter = counter + 1 
    print(counter)

for i in Studenten:     # Liste ausgeben 
    print(i)

for i in range(0 , 5):   # Alle Elemente ausgeben im bereich von 0-10
    print(i)

for i in range(0 , 9):  # Überspringe 3
    if i == 3:
        continue
    print(i)

for j in range(0 , 9):  # Bricht bei 3 ab 
    if j == 3:
        break
    print(j)

Summe=0
for Liste in range(0,10):
    Summe=Summe+Liste
    if Summe >= 11:
        break
    print(Summe)


import math
Wurzel= math.sqrt(12)
print(Wurzel)


import random
part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombre,"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]

print(random.randint(0,4))
print(random)
best_words = [part1,part2,part3,part4]
print(best_words)
sentence = []
#for part in best_words:
    #r = random.randint(0, len(part)-1)
    #sentence.append(part[r])
#print(" ".join(sentence))
#print(part)
#print(r)

#Spiel =[part1 , part2 , part3 , part4]
#random1 = random.randint(0,6)
#random2 = random.randint(0,5)
#random3 = random.randint(0,3)
#random4 = random.randint(0,5)
#Witz = [part1[int(random1)] + part2[int(random2)] + part3[int(random3)] + part4[int(random4)]]
#print(Witz)


def mars():
    print("Hallo Mars")
def welt():
    print("Hallo Welt")


def NameDerFunktion(MeinName, Zähler):
    for i in range(0, Zähler):
        print("DasKompletteUnterprogramm:  " + MeinName)
NameDerFunktion("Justin" , 3)       # Wird drei mal ausgeführt 

def Größer(a,b):        # ruturn gibt beim aufrufen der Funktion was zurück 
    if a > b: 
        return a
    else:
        return b 
WasIstGrößer = Größer(6,8)
print(WasIstGrößer)             # es wird zurück gegeben das 8 größer ist

with open("C:/Users/justi/Documents/Codes/Pyton/Programme/Test.txt" , "r") as file:
    for line in file:
        print(line.strip())

    for line in file:
        print(line)

with open("C:/Users/justi/Documents/Codes/Pyton/Programme/Test1.txt" , "w") as file:
    part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
    for part1 in part1:
        file.write(part1 + "\n")


with open("C:/Users/justi/Documents/Codes/Pyton/Programme/datei.csv") as file:
    for line in file:
        data = line.strip().split(";")
        print(data[0] + ":" + data[1])

import matplotlib.pyplot as plt

plt.plot([-1 , -4.5 , 16 , 23 , 15, 59])
plt.show()

#import C:/Users/justi/Documents/Codes/Spyder/Hallo.py





