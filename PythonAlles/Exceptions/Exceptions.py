# Wenn ein Fehler auftaucht aber das Programm trotzdem weiter laufen soll

try:
    print(5/0)
except ZeroDivisionError:
    print("Man kann nicht durch null Teilen")

try:
    with open("Datei.xyz", "r") as file:
        print(file)
except FileNotFoundError:
    print("Die Datei kann nicht geöffnent werden")


try:
    print(5/0)  
    with open("Datei.xyz", "r") as file:
        print(file)
except ZeroDivisionError:
        print("Man kann nicht durch null Teilen")
except FileNotFoundError:
        print("Die Datei kann nicht geöffnent werden")


def do_something():
    print(5/0)

try:
    do_something()
except ZeroDivisionError:
        print( "Man kann nicht durch null Teilen" )    



class InvalidEmailError(Exception):
    pass

def send_mail(email, subject, content):
    if not "@" in email:
        raise InvalidEmailError()

try:
    send_mail("hallo", "Betreff", "Inhalt")
except InvalidEmailError:
    print("Email falsch")