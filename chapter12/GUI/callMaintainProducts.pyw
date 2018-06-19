import sys
from MaintainProducts import *
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
        QtCore.QObject.connect(self.ui.UpdateButton, QtCore.SIGNAL("clicked()"),
                               self.UpdateRecords)
        QtCore.QObject.connect(self.ui.CancelButton, QtCore.SIGNAL("clicked()"),
                               self.CancelChanges)
        QtCore.QObject.connect(self.ui.InsertButton, QtCore.SIGNAL("clicked()"),
                               self.InsertRecords)
        QtCore.QObject.connect(self.ui.DeleteButton, QtCore.SIGNAL("clicked()"),
                               self.DeleteRecords)
        QtCore.QObject.connect(self.ui.FilterButton, QtCore.SIGNAL("clicked()"),
                               self.FilterRecords)

    def UpdateRecords(self):
        self.model.submitAll()

    def CancelChanges(self):
        self.model.revertAll()

    def InsertRecords(self):
        self.model.insertRow(self.ui.tableView.currentIndex().row())

    def DeleteRecords(self):
        self.model.removeRow(self.ui.tableView.currentIndex().row())
        self.model.submitAll()

    def FilterRecords(self):
        self.model.setFilter("prod_name like '" + self.ui.prodname.text() + "%'")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
