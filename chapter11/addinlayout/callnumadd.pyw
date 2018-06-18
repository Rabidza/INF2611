import sys
from addinlayout import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.AddButton, QtCore.SIGNAL("clicked()"),
                               self.dispsum)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"),
                               self.reject)

    # NH: The textbook says we should do the below... commented out as this overrides
    # the default Qt reject function and did not work on my machine...
    # def reject(self):
    #     self.close()

    def dispsum(self):
        if len(self.ui.lineFirstNumber.text()) != 0:
            a = int(self.ui.lineFirstNumber.text())
        else:
            a = 0
        if len(self.ui.lineSecondNumber.text()) != 0:
            b = int(self.ui.lineSecondNumber.text())
        else:
            b = 0
        sum = a + b
        self.ui.labelAddition.setText("Addition: " + str(sum))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
