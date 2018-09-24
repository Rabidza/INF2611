import sys
from PyQt4 import QtSql, QtGui
from teachersPet import *
from editStudent import Ui_Dialog as StudentDialog
from editBehaviour import Ui_Dialog as BehaviourDialog
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
    def __init__(self, parent=None, ):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.displayDashboard()
        self.displayStudents()
        QtCore.QObject.connect(self.ui.actionExit_Application, QtCore.SIGNAL('triggered()'), self.exitApplication)
        QtCore.QObject.connect(self.ui.btnAddStudent, QtCore.SIGNAL('clicked()'), self.addStudent)
        QtCore.QObject.connect(self.ui.btnEditStudent, QtCore.SIGNAL('clicked()'), self.editStudent)
        QtCore.QObject.connect(self.ui.btnEditStudentBehaviour, QtCore.SIGNAL('clicked()'), self.editBehaviour)

    def displayDashboard(self):
        # top 3 marks
        self.modelTop3Marks = QtSql.QSqlQueryModel(self)
        self.modelTop3Marks.setQuery("""
            SELECT
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

        # bottom 3 marks
        self.modelBot3Marks = QtSql.QSqlQueryModel(self)
        self.modelBot3Marks.setQuery("""
            SELECT
                    FirstName   AS 'Name'     ,
                    LastName    AS 'Last Name',
                    AverageMark AS 'Average Mark'
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
                                students.StudentID = marks.StudentID
                        ORDER BY
                                AverageMark ASC LIMIT 3) joinedtable
            ORDER BY
                    AverageMark ASC;
                    """)
        self.ui.tableViewBot3Marks.setModel(self.modelBot3Marks)

        # top 3 merits
        self.modelTop3Merits = QtSql.QSqlQueryModel(self)
        self.modelTop3Merits.setQuery("""
            SELECT
                    FirstName AS 'Name',
                    Lastname  AS 'Last Name' MeritCount AS 'Merit Count'
            FROM
                    (
                        SELECT
                                FirstName,
                                LastName ,
                                MeritCount
                        FROM
                                Students
                        INNER JOIN
                                Merits
                        ON
                                students.StudentID = merits.StudentID
                        ORDER BY
                                MeritCount DESC LIMIT 3) joinedtable
            ORDER BY
                    MeritCount DESC;)
                   """)
        self.ui.tableViewTop3Merits.setModel(self.modelTop3Merits)

        # top 3 demerits
        self.modelTop3Demerits = QtSql.QSqlQueryModel(self)
        self.modelTop3Demerits.setQuery("""
            SELECT
                    FirstName   AS 'Name'     ,
                    LastName    AS 'Last Name',
                    DemeritCount AS 'Demerit Count'
            FROM
                    (
                            SELECT
                                    FirstName,
                                    LastName ,
                                    MeritCount
                            FROM
                                    Students
                            INNER JOIN
                                    Demerits
                            ON
                                    students.StudentID = demerits.StudentID
                            ORDER BY
                                    DemeritCount DESC LIMIT 3) joinedtable
            ORDER BY
                    DemeritCount DESC;
            """)
        self.ui.tableViewTop3Demerits.setModel(self.modelTop3Merits)

    # load students table view with students from database
    def displayStudents(self):
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("""
            SELECT
                    StudentID    AS 'Student ID'   ,
                    firstName    AS 'First Name'   ,
                    lastName     AS 'Last Name'    ,
                    DateOfBirth  AS 'Date of Birth',
                    SpecialNotes AS 'Special Notes'
            FROM
                    Students
                        """)
        self.ui.tableView.setModel(self.model)

    def exitApplication(self):
        sys.exit(app.exec_())

    def addStudent(self):
        editDialog = EditStudentDialog()
        editDialog.exec_()

    def editStudent(self):
        selectedIndex = self.ui.tableView.selectedIndexes()
        studentId = self.model.data(selectedIndex[0])
        editDialog = EditStudentDialog(studentId)
        QtCore.QObject.connect(editDialog, QtCore.SIGNAL('accepted()'), self.displayStudents)
        editDialog.exec_()

    def editBehaviour(self):
        selectedIndex = self.ui.tableView.selectedIndexes()
        studentId = self.model.data(selectedIndex[0])
        editDialog = EditBehaviourDialog(studentId,
                                         self.model.data(selectedIndex[1]) + " " +
                                         self.model.data(selectedIndex[2]))
        editDialog.exec_()


class EditStudentDialog(QtGui.QDialog):
    isEdit = False

    def __init__(self, studentId=0, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = StudentDialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnSave, QtCore.SIGNAL('clicked()'), self.saveStudent)
        QtCore.QObject.connect(self.ui.btnClose, QtCore.SIGNAL('clicked()'), self.closeDialog)
        QtCore.QObject.connect(self.ui.btnDelete, QtCore.SIGNAL('clicked()'), self.deleteStudent)


    def deleteStudent(self):
        self.model.setQuery("""
            DELETE
            FROM
                   Students
            WHERE
                   studentID = %d
            """ % (int(self.ui.lineEditStudentID.text())))

    def closeDialog(self):
        self.reject()

        if studentId != 0:
            self.isEdit = True
        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("""
            SELECT *
            FROM
                   Students
            WHERE
                   StudentID = %d
            """ % studentId)
        self.student = self.model.record(0)
        self.ui.lineEditStudentID.setText(str(studentId))
        self.ui.lineEditStudentName.setText(self.student.value("firstName"))
        self.ui.lineEditStudentLastName.setText(self.student.value("lastName"))
        self.ui.dateEdit.setDate(self.student.value("dateOfBirth").date())
        self.ui.textEditSpecialNotes.setText(str(self.student.value("specialNotes")))
        self.ui.lineEditPrimaryName.setText(str(self.student.value("primaryContactName")))
        self.ui.lineEditPrimaryNumber.setText(str(self.student.value("primaryContactNumber")))
        self.ui.lineEditSecondaryName.setText(str(self.student.value("secondaryContactName")))
        self.ui.lineEditSecondaryNumber.setText(str(self.student.value("secondaryContactNumber")))

    def saveStudent(self):
        if self.isEdit:
            self.model.setQuery("""
                UPDATE
                        Students
                SET
                        firstName              = '%s',
                        lastName               = '%s',
                        dateOfBirth            = '%s',
                        specialNotes           = '%s',
                        primaryContactName     = '%s',
                        primaryContactNumber   = '%s',
                        secondaryContactName   = '%s',
                        secondaryContactNumber = '%s'
                WHERE
                        StudentID = %d
            """ % (self.ui.lineEditStudentName.text(),
                   self.ui.lineEditStudentLastName.text(),
                   self.ui.dateEdit.text(),
                   self.ui.textEditSpecialNotes.toPlainText(),
                   self.ui.lineEditPrimaryName.text(),
                   self.ui.lineEditPrimaryNumber.text(),
                   self.ui.lineEditSecondaryName.text(),
                   self.ui.lineEditSecondaryNumber.text(),
                   int(self.ui.lineEditStudentID.text())))
        else:
            self.model.setQuery("""
            INSERT INTO
                Students
                (
                        firstName           ,
                        lastName            ,
                        dateOfBirth         ,
                        specialNotes        ,
                        primaryContactName  ,
                        primaryContactNumber,
                        secondaryContactName,
                        secondaryContactNumber
                )
                VALUES
                (
                        %d  ,
                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s',
                        '%s'
                )
            """ % (int(self.ui.lineEditStudentID.text()),
                self.ui.lineEditStudentName.text(),
                self.ui.lineEditStudentLastName.text(),
                self.ui.dateEdit.text(),
                self.ui.textEditSpecialNotes.toPlainText(),
                self.ui.lineEditPrimaryName.text(),
                self.ui.lineEditPrimaryNumber.text(),
                self.ui.lineEditSecondaryName.text(),
                self.ui.lineEditSecondaryNumber.text()))
            self.model.setQuery("""
                INSERT INTO
                    Merits
                    (
                            studentID,
                            meritCount
                    )
                    VALUES
                    (
                            %d,
                            0
                    )
            """ % (int(self.ui.lineEditStudentID.text())))
            self.model.setQuery("""
                INSERT INTO Demerits
                   (studentID
                        , meritCount
                   )
                   values
                   (%d
                        , 0
                   )
                """ % (int(self.ui.lineEditStudentID.text())))
        self.accept()


class EditBehaviourDialog(QtGui.QDialog):
    stu_ID = 0

    def __init__(self, studentId, studentFullName, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = BehaviourDialog()
        self.ui.setupUi(self)
        self.stu_Id = studentId

        QtCore.QObject.connect(self.ui.btnSave, QtCore.SIGNAL('clicked()'), self.saveBehaviour)
        QtCore.QObject.connect(self.ui.btnClose, QtCore.SIGNAL('clicked()'), self.closeDialog)

        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("""SELECT MeritCount FROM Merits WHERE StudentID = %d""" % studentId)
        self.student = self.model.record(0)
        self.ui.spinBoxMerits.setValue(int(self.student.value("MeritCount")))

        self.model = QtSql.QSqlQueryModel(self)
        self.model.setQuery("""SELECT DemeritCount FROM Demerits WHERE StudentID = %d """ % studentId)
        self.student = self.model.record(0)
        self.ui.spinBoxDemerits.setValue(int(self.student.value("DemeritCount")))
        self.ui.labelStudentName.setText(studentFullName)

    def saveBehaviour(self):
        self.model.setQuery("""
            UPDATE Merits SET MeritCount = %d WHERE StudentID = %d 
            """ % (int(self.ui.spinBoxMerits.value()), self.stu_Id))

        self.model.setQuery("""
            UPDATE Demerits SET DemeritCount = %d
            WHERE StudentID = %d 
            """ % (int(self.ui.spinBoxDemerits.value()), self.stu_Id))

        self.accept()

    def closeDialog(self):
        self.reject()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if not createConnection():
        sys.exit(1)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
