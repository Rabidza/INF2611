import sys
from showrec import *
from PyQt4 import QtSql, QtGui
from chapter12 import settings


def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName(settings.HOST)
    db.setDatabaseName(settings.DATABASE)
    db.setUserName(settings.USER)
    db.setPassword(settings.PASSWORD)
    db.open()
    print(db.lastError().text())
    return True


class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = QtSql.QSqlTableModel(self)
        self.model.setTable("products")
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.ui.tableView.setModel(self.model)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
