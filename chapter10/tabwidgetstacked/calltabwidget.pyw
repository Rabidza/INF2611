import sys
from tabwidgetstacked import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("Food")
        self.ui.comboBox.addItem("Drinks")
        self.ui.comboBox.addItem("Ice Creams")
        QtCore.QObject.connect(self.ui.comboBox, QtCore.SIGNAL("activated(int)"),
                               self.ui.stackedWidget, QtCore.SLOT("setCurrentIndex(int)"))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
