# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addinlayout.ui'
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
        Dialog.resize(346, 228)
        self.labelAddition = QtGui.QLabel(Dialog)
        self.labelAddition.setGeometry(QtCore.QRect(50, 110, 111, 16))
        self.labelAddition.setObjectName(_fromUtf8("labelAddition"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 22, 274, 83))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelFirstNumber = QtGui.QLabel(self.widget)
        self.labelFirstNumber.setObjectName(_fromUtf8("labelFirstNumber"))
        self.horizontalLayout_2.addWidget(self.labelFirstNumber)
        self.lineFirstNumber = QtGui.QLineEdit(self.widget)
        self.lineFirstNumber.setObjectName(_fromUtf8("lineFirstNumber"))
        self.horizontalLayout_2.addWidget(self.lineFirstNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelSecondNumber = QtGui.QLabel(self.widget)
        self.labelSecondNumber.setObjectName(_fromUtf8("labelSecondNumber"))
        self.horizontalLayout_3.addWidget(self.labelSecondNumber)
        self.lineSecondNumber = QtGui.QLineEdit(self.widget)
        self.lineSecondNumber.setObjectName(_fromUtf8("lineSecondNumber"))
        self.horizontalLayout_3.addWidget(self.lineSecondNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(108, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.AddButton = QtGui.QPushButton(self.widget)
        self.AddButton.setObjectName(_fromUtf8("AddButton"))
        self.horizontalLayout_4.addWidget(self.AddButton)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.labelAddition.setText(_translate("Dialog", "TextLabel", None))
        self.labelFirstNumber.setText(_translate("Dialog", "Enter First Number", None))
        self.labelSecondNumber.setText(_translate("Dialog", "Enter Second Number", None))
        self.AddButton.setText(_translate("Dialog", "Add", None))
        self.pushButton.setText(_translate("Dialog", "Cancel", None))

