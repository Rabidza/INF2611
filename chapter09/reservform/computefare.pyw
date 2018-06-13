import sys
from reservform import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.classTypes = ["First Class", "Second Class", "Business Class", "Economic Class"]
        self.addcontent()
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.computefare)

    def addcontent(self):
        for i in self.classTypes:
            self.ui.comboBox.addItem(i)

    def computefare(self):
        dateselected = self.ui.calendarWidget.selectedDate()
        dateinstring = str(dateselected.toPyDate())
        noOfPersons = self.ui.spinBox.value()
        chosenclass = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        self.ui.Enteredinfo.setText("Date of Journey: " + dateinstring + ", Number of persons: " + str(noOfPersons) + " and Class selected: " + chosenclass)

        fare = 0
        if chosenclass == "First Class":
            fare = 40
        if chosenclass == "Second Class":
            fare = 30
        if chosenclass == "Business Class":
            fare = 20
        if chosenclass == "Economic Class":
            fare = 10

        total = fare * noOfPersons
        self.ui.Fareinfo.setText("Fare for " + chosenclass + " is " + str(fare) + "$. Total fare is " + str(total) + '$')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
