# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editBehaviour.ui'
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
        Dialog.resize(662, 447)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 47, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.labelStudentName = QtGui.QLabel(Dialog)
        self.labelStudentName.setGeometry(QtCore.QRect(100, 30, 151, 16))
        self.labelStudentName.setObjectName(_fromUtf8("labelStudentName"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 611, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.spinBoxMerits = QtGui.QSpinBox(self.groupBox)
        self.spinBoxMerits.setGeometry(QtCore.QRect(450, 10, 91, 71))
        self.spinBoxMerits.setObjectName(_fromUtf8("spinBoxMerits"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 200, 611, 121))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.spinBoxDemerits = QtGui.QSpinBox(self.groupBox_2)
        self.spinBoxDemerits.setGeometry(QtCore.QRect(450, 30, 91, 71))
        self.spinBoxDemerits.setObjectName(_fromUtf8("spinBoxDemerits"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 180, 641, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.splitter = QtGui.QSplitter(Dialog)
        self.splitter.setGeometry(QtCore.QRect(490, 340, 150, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.btnSave = QtGui.QPushButton(self.splitter)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.btnClose = QtGui.QPushButton(self.splitter)
        self.btnClose.setObjectName(_fromUtf8("btnClose"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Student:", None))
        self.labelStudentName.setText(_translate("Dialog", "TextLabel", None))
        self.groupBox.setTitle(_translate("Dialog", "Merits", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Demerits", None))
        self.btnSave.setText(_translate("Dialog", "Save", None))
        self.btnClose.setText(_translate("Dialog", "Close", None))

