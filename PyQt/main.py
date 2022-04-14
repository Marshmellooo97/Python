import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Studierendenverwaltung")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculate.clicked.connect(self.calculate_bmi)

    def calculate_bmi(self):
        gr = self.ui.height.value()  # gewicht abfragen
        gw = self.ui.weigth.value()  # größe abfragen
        if gr == 0:
            self.ui.result.setText("Größe eingeben")
        else:
            bmi = gw / gr**2
            self.ui.result.setText(str(round(bmi, 2)))
        #bmi = gw in kg / gr in meter **2
        #self.ui.input.setText("!!!!")       # Im Textfeld soll "!!!!" drin stehen

    def on_button_click(self):
        text = self.ui.input.text()             # Textfeld lesen
        print("on_button_click()" + text )

window = MainWindow()
window.show()
sys.exit(app.exec_())

#button = QtWidgets.QPushButton(window) #Butten erstellen
#button.setText("Klick mich")
#button.show()
#checkbox = QtWidgets.QCheckBox(window)  # Checkbox anlegen
#checkbox.setText("Checkbox")
#checkbox.setGeometry(30, 100, 200,100)          #Position x nach rechts y breite höhe
#checkbox.show()