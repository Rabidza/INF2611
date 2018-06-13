# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reservform.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(445, 487)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 10, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 310, 47, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Enteredinfo = QtGui.QLabel(Dialog)
        self.Enteredinfo.setGeometry(QtCore.QRect(10, 410, 411, 16))
        self.Enteredinfo.setText(_fromUtf8(""))
        self.Enteredinfo.setObjectName(_fromUtf8("Enteredinfo"))
        self.Fareinfo = QtGui.QLabel(Dialog)
        self.Fareinfo.setGeometry(QtCore.QRect(10, 450, 411, 16))
        self.Fareinfo.setText(_fromUtf8(""))
        self.Fareinfo.setObjectName(_fromUtf8("Fareinfo"))
        self.calendarWidget = QtGui.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(110, 50, 312, 183))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.spinBox = QtGui.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(110, 260, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(110, 310, 251, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 350, 141, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Reservation Form", None))
        self.label_2.setText(_translate("Dialog", "Date of Journey", None))
        self.label_3.setText(_translate("Dialog", "Number of Persons", None))
        self.label_4.setText(_translate("Dialog", "Class", None))
        self.pushButton.setText(_translate("Dialog", "Calculate Fare", None))

