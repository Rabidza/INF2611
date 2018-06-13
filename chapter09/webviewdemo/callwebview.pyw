import sys
from PyQt4.QtCore import *
from webviewdemo import *


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.openURL)

    def openURL(self):
        if len(self.ui.siteURL.text()) != 0:
            self.ui.webView.load(QUrl(self.ui.siteURL.text()))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
