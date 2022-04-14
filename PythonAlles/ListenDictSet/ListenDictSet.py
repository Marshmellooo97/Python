# Liste
Studenten = ["S1", "S2", "S3", "S4"]  # Liste
print(Studenten)
Studenten.append("S5")  # Liste jemanden hinzufügen
print(Studenten)
print(len(Studenten))  # Liste gesamtanzahl abfragen
print(Studenten[0] + " und " + Studenten[4])  # Liste ausgeben Nr1 und Nr5
Studenten.pop()  # Löscht den letzten Eintrag "S6"
print(Studenten)
P = Studenten.pop()  # Löscht den letzten Eintrag "S5" und speichert ihn in P
print(P)  # Gibt die Variable P aus
print("#".join(Studenten))  # Ausgeben der Liste "xxx" verbindung zwischen den einzelnen Einträge
print(Studenten)  # Liste einfach ausgegeben
Studenten_String = (", ".join(Studenten))
print("In der Liste sind folgende Elemente: " + Studenten_String)  # Ausgabe liste in Variable speichern und ausgeben
s = "Das ist ein Satz der besteht aus vielen Wörtern!"
s = s.split(" ")  # Von string zu Liste
print(s)
print(len(s))  # Ausgabe Liste wie viele Wörter stehen da drin

Studenten = ["S1", "S2", "S3", "S4", "S5", "S6", "S7"]
del Studenten[3]  # 3tes Element wird gelöscht
Studenten.remove("S2")  # S2 Wir gelöscht
print(Studenten)
print(Studenten[-1])  # Letztes Elemt wird ausgegeben
Studenten = ["S1", "S2", "S3", "S4", "S5", "S6", "S7"]

# Bereichsabfrage
print(Studenten[2:5])  # Teilliste von elemt 2 bis 5 5 nicht mehr dabei
print("Hallo Welt"[0:5])  # Geht auch bei Strings
print("Hallo Welt"[6:])  # Geht auch bei Strings

xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = []
for x in xs:
    ys.append(x * x)
print(xs)
print(ys)
xs = [1, 2, 3, 4, 5, 6, 7, 8]
ys = [x * x for x in xs]
print(xs)
print(ys)

# Dictioaries
d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SGN"}
print(d)
# zugreifen
print(d.get("Budapest"))  # Fals nein wird NONE ausgegeben
print(d["Saigon"])  # Wenn nicht erhalten dann fehler
# Hinzufügen
d["Budapest"] = "BUD"
print(d)
# Löschen
del d["Budapest"]
# Abfragen
if "Budapest" in d:
    print("JA")
else:
    print("NEIN")
print("Berlin" in d)  # False oder True
for key in d:
    value = d[key]
    # print(key)
    print(value)

print(d.items())
for key, value in d.items():
    print(key + ": " + value)

# Tupel
t = ("Max Mustermann", 22, "Informatik")
print(t[0])
Name, Alter, Fach = t
print(Fach)
# hinzufügen geht nicht / überschreiben geht nicht


students = [("Max Müller", 22), ("Monika Mustermann", 23)]
for name, age in students:
    print(name)
    print(age)

test = [1, "ha", "dsf", 5, 3, "sdf"]
print(test)
del test[3]
print(test)

# Liste in Liste
liste = [
    ["Berlin", "München", "Köln"],
    ["Budapest", "Pecs", "Sopron"]
]

liste[0][0]

Hochschule = {
    "Informatik": ["Max", "Monika"],
    "BWL": ["Erik", "Franziska"]

}
print(Hochschule["Informatik"])
print(Hochschule["BWL"])

# Set
s = {"Hallo", "Welt"}
s.add("Mars")
print(s)
s.add("Mars")  # Wird nicht erneut hinzugefügt
if "Mars" in s:
    print("ja")
text = "Hallo Welt Hallo Mars Hallo Welt"
words = set()  # Leeres Set erstellen
for word in text.split(" "):
    words.add(word)
print(words)
print(len(words))

# Queue Warteschlange
import queue

q = queue.Queue()
q.put("Hallo")
q.put("Welt")
q.put("Hallo")
q.put("Mars")
q.put("Pluto")

print(q.get())  # Erster eintrag wird entfernt und gelöscht
while not q.empty():  # Restliche elemente werden ausgegeben und gelöscht
    element = q.get()
    print(element)

q = queue.PriorityQueue()
q.put((10, "Hallo Welt"))  # Zahl = Wichtigkeit 0 ganz wichtig
q.put((15, "Mars"))  # Danach kommt der eintrag
q.put((5, "Wichtig"))

text = "A A A A A A A A A A A A B B B B B B B C C C C C D D D D"
d = {}
for word in text.split(" "):
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
pq = queue.PriorityQueue()
for word, number in d.items():
    pq.put((number, word))  # number = aufteigend sotierung -number = absteigende sotierung
print(pq.get())


def main():
    mylist = [1, 2, 3]
    mylist.append(-10)
    print(mylist)

if __name__ == "__main__":
    main()

my_list = [1, 2, 3]
# Option 1: Single Value
print(my_list)
# Option 2: List Concatenation
my_list2 = [4, 5]
# my_list += my_list2
my_list = my_list + my_list2
print(my_list)
# Option 3: Iterables
it = range(-2, 3, 1)
my_list.extend(it)
print(my_list)
# Option 4: Insert at user-defined index
my_list.insert(0, "hello")
print(my_list)
my_list.insert(-30, "hello")
print(my_list)
# Remove values
my_list.pop()
print(my_list)
while 'hello' in my_list:
    idx = my_list.index('hello')
    my_list.pop(idx)
print(my_list)
# Copy
my_list_new = my_list
print(hex(id(my_list)))
print(hex(id(my_list_new)))
my_list_new = my_list.copy()
print(hex(id(my_list)))
print(hex(id(my_list_new)))
# Reverse Liste umdrehen
my_list.reverse()
print(my_list)
print(my_list[::-1])
# Count
print(my_list.count(1))
# Sort
#my_list.append('hello')
my_list.sort(reverse=True)  # True = von großen zahlen nach kleinen sotieren
print(my_list)

#Liste anlegen
my_list_comp = [i for i in range(10)]
print(my_list_comp)



