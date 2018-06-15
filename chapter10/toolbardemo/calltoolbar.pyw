import sys
from toolbardemo import *


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.actionPlus, QtCore.SIGNAL("triggered()"), self.plusmessage)
        self.connect(self.ui.actionMinus, QtCore.SIGNAL("triggered()"), self.minusmessage)
        self.connect(self.ui.actionMultiply, QtCore.SIGNAL("triggered()"), self.multiplymessage)
        self.connect(self.ui.actionDivide, QtCore.SIGNAL("triggered()"), self.dividemessage)
        self.connect(self.ui.actionEqual, QtCore.SIGNAL("triggered()"), self.equalmessage)

    def plusmessage(self):
        self.ui.label.setText("You have selected Plus ")

    def minusmessage(self):
        self.ui.label.setText("You have selected Minus ")

    def multiplymessage(self):
        self.ui.label.setText("You have selected Multiply ")

    def dividemessage(self):
        self.ui.label.setText("You have selected Divide ")

    def equalmessage(self):
        self.ui.label.setText("You have selected Equal ")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
