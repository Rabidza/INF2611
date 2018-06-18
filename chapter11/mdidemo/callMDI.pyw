import sys
from mdidemo import *


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow)
        self.ui.mdiArea.addSubWindow(self.ui.subwindow_2)
        QtCore.QObject.connect(self.ui.showNext, QtCore.SIGNAL("clicked()"),
                               self.displayNext)
        QtCore.QObject.connect(self.ui.showPrevious, QtCore.SIGNAL("clicked()"),
                               self.displayPrevious)
        QtCore.QObject.connect(self.ui.closeAll, QtCore.SIGNAL("clicked()"),
                               self.closeAll)
        QtCore.QObject.connect(self.ui.cascadeButton, QtCore.SIGNAL("clicked()"),
                               self.cascadeArrange)
        QtCore.QObject.connect(self.ui.tileButton, QtCore.SIGNAL("clicked()"),
                               self.tileArrange)
        QtCore.QObject.connect(self.ui.SubWindowViewButton, QtCore.SIGNAL("clicked()"),
                               self.SubWindowView)
        QtCore.QObject.connect(self.ui.TabbedViewButton, QtCore.SIGNAL("clicked()"),
                               self.TabbedView)
        self.connect(self.ui.actionFirst_Window, QtCore.SIGNAL("triggered()"),
                     self.displayNext)
        self.connect(self.ui.actionSecond_Window, QtCore.SIGNAL("triggered()"),
                     self.displayPrevious)

    def displayNext(self):
        self.ui.mdiArea.activateNextSubWindow()

    def displayPrevious(self):
        self.ui.mdiArea.activatePreviousSubWindow()

    def closeAll(self):
        self.ui.mdiArea.closeAllSubWindows()

    def cascadeArrange(self):
        self.ui.mdiArea.cascadeSubWindows()

    def tileArrange(self):
        self.ui.mdiArea.tileSubWindows()

    def SubWindowView(self):
        self.ui.mdiArea.setViewMode(0)

    def TabbedView(self):
        self.ui.mdiArea.setViewMode(1)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
