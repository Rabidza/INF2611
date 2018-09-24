# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teachersPet.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(771, 577)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 751, 531))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 351, 481))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 290, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tableViewTop3Merits = QtGui.QTableView(self.groupBox)
        self.tableViewTop3Merits.setGeometry(QtCore.QRect(90, 20, 256, 192))
        self.tableViewTop3Merits.setObjectName(_fromUtf8("tableViewTop3Merits"))
        self.tableViewTop3Demerits = QtGui.QTableWidget(self.groupBox)
        self.tableViewTop3Demerits.setGeometry(QtCore.QRect(90, 280, 256, 192))
        self.tableViewTop3Demerits.setObjectName(_fromUtf8("tableViewTop3Demerits"))
        self.tableViewTop3Demerits.setColumnCount(0)
        self.tableViewTop3Demerits.setRowCount(0)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(0, 240, 351, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 20, 371, 481))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tableViewTop3Marks = QtGui.QTableWidget(self.groupBox_2)
        self.tableViewTop3Marks.setGeometry(QtCore.QRect(110, 20, 256, 192))
        self.tableViewTop3Marks.setObjectName(_fromUtf8("tableViewTop3Marks"))
        self.tableViewTop3Marks.setColumnCount(0)
        self.tableViewTop3Marks.setRowCount(0)
        self.tableViewBot3Marks = QtGui.QTableWidget(self.groupBox_2)
        self.tableViewBot3Marks.setGeometry(QtCore.QRect(110, 280, 256, 192))
        self.tableViewBot3Marks.setObjectName(_fromUtf8("tableViewBot3Marks"))
        self.tableViewBot3Marks.setColumnCount(0)
        self.tableViewBot3Marks.setRowCount(0)
        self.line_2 = QtGui.QFrame(self.groupBox_2)
        self.line_2.setGeometry(QtCore.QRect(0, 240, 371, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableView = QtGui.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 731, 451))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.btnAddStudent = QtGui.QPushButton(self.tab_2)
        self.btnAddStudent.setGeometry(QtCore.QRect(0, 470, 75, 23))
        self.btnAddStudent.setObjectName(_fromUtf8("btnAddStudent"))
        self.btnEditStudent = QtGui.QPushButton(self.tab_2)
        self.btnEditStudent.setGeometry(QtCore.QRect(100, 470, 75, 23))
        self.btnEditStudent.setObjectName(_fromUtf8("btnEditStudent"))
        self.btnEditStudentMarks = QtGui.QPushButton(self.tab_2)
        self.btnEditStudentMarks.setGeometry(QtCore.QRect(190, 470, 75, 23))
        self.btnEditStudentMarks.setObjectName(_fromUtf8("btnEditStudentMarks"))
        self.btnTakeAttendance = QtGui.QPushButton(self.tab_2)
        self.btnTakeAttendance.setGeometry(QtCore.QRect(280, 470, 91, 23))
        self.btnTakeAttendance.setObjectName(_fromUtf8("btnTakeAttendance"))
        self.btnEditStudentBehavior = QtGui.QPushButton(self.tab_2)
        self.btnEditStudentBehavior.setGeometry(QtCore.QRect(380, 470, 131, 23))
        self.btnEditStudentBehavior.setObjectName(_fromUtf8("btnEditStudentBehavior"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionE_xit_Application = QtGui.QAction(MainWindow)
        self.actionE_xit_Application.setObjectName(_fromUtf8("actionE_xit_Application"))
        self.menu_File.addAction(self.actionE_xit_Application)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Behaviour", None))
        self.label.setText(_translate("MainWindow", "Top 3 Merits:", None))
        self.label_2.setText(_translate("MainWindow", "Top 3 Demerits:", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Marks", None))
        self.label_3.setText(_translate("MainWindow", "Top 3 Marks:", None))
        self.label_4.setText(_translate("MainWindow", "Bottom 3 Marks:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Dashboard", None))
        self.btnAddStudent.setText(_translate("MainWindow", "Add Student", None))
        self.btnEditStudent.setText(_translate("MainWindow", "Edit Student", None))
        self.btnEditStudentMarks.setText(_translate("MainWindow", "Edit Marks", None))
        self.btnTakeAttendance.setText(_translate("MainWindow", "Take Attendance", None))
        self.btnEditStudentBehavior.setText(_translate("MainWindow", "Edit Merits and Demerits", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Students", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.actionE_xit_Application.setText(_translate("MainWindow", "E&xit Application", None))

