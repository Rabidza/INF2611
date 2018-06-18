import sys
from groupbx import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.CalculateButton, QtCore.SIGNAL("clicked()"),
                               self.calculatebill)

    def calculatebill(self):
        bill = 0
        if self.ui.vanilla.isChecked():
            bill += 5
        if self.ui.blacksunday.isChecked():
            bill += 10
        if self.ui.chocolatechips.isChecked():
            bill += 20
        if self.ui.strawberry.isChecked():
            bill += 15
        if self.ui.DrinksBox.isChecked():
            if self.ui.coffee.isChecked():
                bill += 5
            if self.ui.colddrink.isChecked():
                bill += 10
            if self.ui.juice.isChecked():
                bill += 15
        self.ui.label.setText("The bill is: " + str(bill) + '$')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
