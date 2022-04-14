
from flask import Flask, render_template, request
app = Flask(__name__)

class item():
    def __init__(self, name, anzahl):
        self.name = name
        self.anzahl = anzahl

@app.route('/')
def hello():
    items = [
        {"name" : "Apfel" , "Anzahl" : 5},
        {"name" : "Computer" , "Anzahl" : 1},
        {"name": "Birne", "Anzahl": 4}
            ]

    for item in items:
        item["Anzahl"] = item["Anzahl"] * 2

    person = ("Max" , "Mustermann")
    return render_template("start.html" , person = person , items = items)


@app.route('/kontakt')
def kontakt():
    vorname = request.args.get("vorname")
    nachname = request.args.get("nachname")
    age =request.args.get("age")
    mail = request.args.get("mail")
    if mail == None:
        mail = ' '
    if not '@' in mail:
        fehler = True
        fehlerM = 'Falsche Mail'
        mail = mail
    return render_template("kontakt.html", bla = vorname, nachname = nachname, age = age, mail = mail, fehler = fehler, fehlerM = fehlerM)

@app.route('/test')
def test():
    return render_template("test.html")

@app.route('/anmeldedaten')
def anmeldedaten():
    name = request.args.get("name")
    age =request.args.get("age")
    return render_template("anmeldedaten.html" , name = name, age = age)

@app.route('/wechselkurs')
def test123():

    wechselkurs = request.args.get("wechselkurs")
    VON = request.args.get("VON")
    IN = request.args.get("IN")

    Tabelle = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 50, 100, 200, 500]
    a = 0
    d = {}
    if wechselkurs == None:
        wechselkurs = 1

    c = float(wechselkurs)
    for i in range(1, len(Tabelle) + 1):
        d[Tabelle[a]] = round(Tabelle[a] * float(c), 2)
        a = a + 1
    print(wechselkurs)
    print(d)
    return render_template("wechselkurs.html", wechselkurs = wechselkurs, VON = VON, IN = IN, d = d)

print("Hallo")




#i