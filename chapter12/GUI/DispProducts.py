# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DispProducts.ui'
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
        Dialog.resize(400, 223)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 47, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 110, 31, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.prodid = QtGui.QLineEdit(Dialog)
        self.prodid.setGeometry(QtCore.QRect(70, 70, 113, 20))
        self.prodid.setObjectName(_fromUtf8("prodid"))
        self.prodname = QtGui.QLineEdit(Dialog)
        self.prodname.setGeometry(QtCore.QRect(280, 70, 113, 20))
        self.prodname.setObjectName(_fromUtf8("prodname"))
        self.qty = QtGui.QLineEdit(Dialog)
        self.qty.setGeometry(QtCore.QRect(70, 110, 81, 20))
        self.qty.setObjectName(_fromUtf8("qty"))
        self.price = QtGui.QLineEdit(Dialog)
        self.price.setGeometry(QtCore.QRect(280, 110, 61, 20))
        self.price.setObjectName(_fromUtf8("price"))
        self.FirstButton = QtGui.QPushButton(Dialog)
        self.FirstButton.setGeometry(QtCore.QRect(10, 170, 75, 23))
        self.FirstButton.setObjectName(_fromUtf8("FirstButton"))
        self.PreviousButton = QtGui.QPushButton(Dialog)
        self.PreviousButton.setGeometry(QtCore.QRect(110, 170, 75, 23))
        self.PreviousButton.setObjectName(_fromUtf8("PreviousButton"))
        self.NextButton = QtGui.QPushButton(Dialog)
        self.NextButton.setGeometry(QtCore.QRect(210, 170, 75, 23))
        self.NextButton.setObjectName(_fromUtf8("NextButton"))
        self.LastButton = QtGui.QPushButton(Dialog)
        self.LastButton.setGeometry(QtCore.QRect(310, 170, 75, 23))
        self.LastButton.setObjectName(_fromUtf8("LastButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "List of Products", None))
        self.label_2.setText(_translate("Dialog", "Product ID", None))
        self.label_3.setText(_translate("Dialog", "Product Name", None))
        self.label_4.setText(_translate("Dialog", "Quantity", None))
        self.label_5.setText(_translate("Dialog", "Price", None))
        self.FirstButton.setText(_translate("Dialog", "First", None))
        self.PreviousButton.setText(_translate("Dialog", "Previous", None))
        self.NextButton.setText(_translate("Dialog", "Next", None))
        self.LastButton.setText(_translate("Dialog", "Last", None))

