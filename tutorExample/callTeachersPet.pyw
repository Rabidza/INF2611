import sys
from PyQt4 import QtSql, QtGui
from teachersPet import *
import settings


def createConnection():
    db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
    db.setHostName(settings.HOST)
    db.setDatabaseName(settings.DATABASE)
    db.setUserName(settings.USER)
    db.setPassword(settings.PASSWORD)
    db.open()
    print(db.lastError().text())
    return True


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.displayDashboard()

    def displayDashboard(self):
        # top 3 marks
        self.modelTop3Marks = QtSql.QSqlQueryModel(self)
        self.modelTop3Marks.setQuery("""SELECT
                                                FirstName AS 'Name',
                                                Lastname  AS 'Last Name' AverageMark AS 'Average Mark'
                                        FROM
                                                (
                                                        SELECT
                                                                FirstName,
                                                                LastName ,
                                                                AverageMark
                                                        FROM
                                                                Students
                                                        INNER JOIN
                                                                Marks
                                                        ON
                                                                Marks.StudentID = Students.StudentID
                                                        ORDER BY
                                                                AverageMark DESC LIMIT 3) joinedtable
                                        ORDER BY
                                                AverageMark DESC;)
                                               """)
        self.ui.tableViewTop3Marks.setModel(self.modelTop3Marks)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
