import sys
from menudemo import *


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect(self.ui.action_Open, QtCore.SIGNAL("triggered()"), self.openmessage)
        self.connect(self.ui.action_Page_Layout_Box, QtCore.SIGNAL("triggered()"), self.layoutmessage)
        self.connect(self.ui.action_Format_Box, QtCore.SIGNAL("triggered()"), self.formatmessage)
        self.connect(self.ui.actionCut, QtCore.SIGNAL("triggered()"), self.cutmessage)
        self.connect(self.ui.actionCopy, QtCore.SIGNAL("triggered()"), self.copymessage)

    def openmessage(self):
        self.ui.label.setText("Opening a File")

    def layoutmessage(self):
        self.ui.label.setText("You selected Page Layout option")

    def formatmessage(self):
        self.ui.label.setText("You selected Format option")

    def cutmessage(self):
        self.ui.label.setText("Cutting a text")

    def copymessage(self):
        self.ui.label.setText("Copying text")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
