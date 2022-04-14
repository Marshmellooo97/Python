
class Student():
    def name(self):
        print(self.firstname + " " + self.lastname)

erik = Student()
erik.firstname = "Erik"
erik.lastname = "Mustermann"

monika = Student()
monika.firstname = "Monika"
monika.lastname = "Müller"

erik.name()
monika.name()


class Student():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.__term = 1

    def increase_term(self):            # __ Kann keiner drauf zu greifen
        if self.__term >= 9:
            return
        self.__term = self.__term + 1

    def get_term(self):
        return self.__term

    def name(self):
        print(self.firstname + " " + self.lastname + " (Semester: " + str(self.__term) + ")")

erik = Student("Erik" , "Mustermann")
erik.increase_term()

print(erik.get_term())
erik.name()


class PhoneBook():
    def __init__(self):
        self.__entries = {}

    def add(self, name, phone_number):
        self.__entries[name] = phone_number

    def get(self, name):
        if name in self.__entries:
            return self.__entries[name]
        else:
            return None

    def __str__(self):
        return "PhoneBook(" + str(self.__entries) + ")"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.__entries)

book = PhoneBook()
book.add("Mustermann" , "+4912345")
book.add("Müller" , "+491234567")
print(book)
print(len(book))


# vererbung
class Student():
    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

    def name(self):
        return self.firstname + " " + self.surname

class WorkingStudent(Student):  # Vererbung wird alles von oben vererbt
    def __init__(self, firstname, surname, company):
        super().__init__(firstname, surname)
        self.company = company

    def name(self):
        return super().name() + " (" + self.company + ")"

students = [
    WorkingStudent("Max" , "Müller" , "ABCD GmbH"),
    Student("Monika", "Mustermann"),
    Student("Erik", "Müller"),
    WorkingStudent("Franziska", "Mustermann", "XYZ GmbH")
]
for studenttt in students:
    print(studenttt.name())



import math

class Ball():
    def __init__(self, radius):
        self.radius = radius

    def surface(self):
        print(self.radius**2 * math.pi *4)

    def volume(self):
        print(4 / 3 * math.pi * self.radius ** 3)


b = Ball(4)
b.surface()
b.volume()


class Account():
    def __init__(self, geld, pin):
        self.geld = geld
        self.pin = pin

    def display(self):
        print(self.geld)

    def pay_in(self, Gelderhalten):
        self.geld = self.geld + Gelderhalten

    def withdraw(self, Geldminus, pin):
        if pin == self.pin:
            if self.geld >= Geldminus:
                self.geld = self.geld - Geldminus
            else:
                print("Es kann maximal " + str(self.geld) + " € abgebucht werden.")


Kunde111 = Account(500, "1234")
Kunde111.display()
Kunde111.pay_in(40)
Kunde111.display()
Kunde111.withdraw(25, "1234")
Kunde111.display()
Kunde111.withdraw(60, "1234")
Kunde111.display()


class Train():
    def __init__(self, route, start):
        self.route = route
        self.standort = start

    def show_station(self):
        print(self.route[self.standort])

    def move(self):
        if self.standort < len(self.route) - 1:
            self.standort += 1
        else:
            print("Endstation")

    def move_back(self):
        if self.standort > 0:
            self.standort = self.standort - 1

    def bypass_station(self, station):
        if station in self.route:
            self.route.remove(station)
            self.standort = 0


orientexpress = Train(["Paris", "Budapest", "Bukarest", "Istanbul"], 0)
orientexpress.bypass_station("Budapest")
orientexpress.move()
orientexpress.show_station()





















