# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MaintainProducts.ui'
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
        Dialog.resize(454, 375)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 421, 281))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.prodname = QtGui.QLineEdit(Dialog)
        self.prodname.setGeometry(QtCore.QRect(120, 20, 113, 20))
        self.prodname.setObjectName(_fromUtf8("prodname"))
        self.FilterButton = QtGui.QPushButton(Dialog)
        self.FilterButton.setGeometry(QtCore.QRect(270, 20, 75, 23))
        self.FilterButton.setObjectName(_fromUtf8("FilterButton"))
        self.UpdateButton = QtGui.QPushButton(Dialog)
        self.UpdateButton.setGeometry(QtCore.QRect(10, 340, 75, 23))
        self.UpdateButton.setObjectName(_fromUtf8("UpdateButton"))
        self.CancelButton = QtGui.QPushButton(Dialog)
        self.CancelButton.setGeometry(QtCore.QRect(130, 340, 75, 23))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.InsertButton = QtGui.QPushButton(Dialog)
        self.InsertButton.setGeometry(QtCore.QRect(250, 340, 75, 23))
        self.InsertButton.setObjectName(_fromUtf8("InsertButton"))
        self.DeleteButton = QtGui.QPushButton(Dialog)
        self.DeleteButton.setGeometry(QtCore.QRect(360, 340, 75, 23))
        self.DeleteButton.setObjectName(_fromUtf8("DeleteButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Enter Product Name", None))
        self.FilterButton.setText(_translate("Dialog", "Filter", None))
        self.UpdateButton.setText(_translate("Dialog", "Update", None))
        self.CancelButton.setText(_translate("Dialog", "Cancel", None))
        self.InsertButton.setText(_translate("Dialog", "Add", None))
        self.DeleteButton.setText(_translate("Dialog", "Delete", None))

