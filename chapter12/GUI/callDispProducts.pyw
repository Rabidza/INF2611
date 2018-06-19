import sys
from DispProducts import *
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
    recno = 0

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("SELECT * FROM products")
        self.record = self.model.record(0)
        self.ui.prodid.setText(str(self.record.value("prod_id")))
        self.ui.prodname.setText(str(self.record.value("prod_name")))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))
        QtCore.QObject.connect(self.ui.FirstButton, QtCore.SIGNAL("clicked()"),
                               self.dispFirst)
        QtCore.QObject.connect(self.ui.PreviousButton, QtCore.SIGNAL("clicked()"),
                               self.dispPrevious)
        QtCore.QObject.connect(self.ui.LastButton, QtCore.SIGNAL("clicked()"),
                               self.dispLast)
        QtCore.QObject.connect(self.ui.NextButton, QtCore.SIGNAL("clicked()"),
                               self.dispNext)

    def dispFirst(self):
        MyForm.recno = 0
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("prod_id")))
        self.ui.prodname.setText(str(self.record.value("prod_name")))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

    def dispPrevious(self):
        MyForm.recno -= 1
        if MyForm.recno < 0:
            MyForm.recno = self.model.rowCount() - 1
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("prod_id")))
        self.ui.prodname.setText(str(self.record.value("prod_name")))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

    def dispLast(self):
        MyForm.recno = self.model.rowCount() - 1
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("prod_id")))
        self.ui.prodname.setText(str(self.record.value("prod_name")))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))

    def dispNext(self):
        MyForm.recno += 1
        if MyForm.recno > self.model.rowCount() - 1:
            MyForm.recno = 0
        self.record = self.model.record(MyForm.recno)
        self.ui.prodid.setText(str(self.record.value("prod_id")))
        self.ui.prodname.setText(str(self.record.value("prod_name")))
        self.ui.qty.setText(str(self.record.value("quantity")))
        self.ui.price.setText(str(self.record.value("price")))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
