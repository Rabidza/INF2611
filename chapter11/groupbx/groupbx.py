# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupbx.ui'
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
        Dialog.resize(400, 300)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(11, 11, 171, 271))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.vanilla = QtGui.QRadioButton(self.groupBox)
        self.vanilla.setGeometry(QtCore.QRect(30, 20, 111, 17))
        self.vanilla.setObjectName(_fromUtf8("vanilla"))
        self.blacksunday = QtGui.QRadioButton(self.groupBox)
        self.blacksunday.setGeometry(QtCore.QRect(30, 50, 111, 17))
        self.blacksunday.setObjectName(_fromUtf8("blacksunday"))
        self.chocolatechips = QtGui.QRadioButton(self.groupBox)
        self.chocolatechips.setGeometry(QtCore.QRect(30, 80, 131, 17))
        self.chocolatechips.setObjectName(_fromUtf8("chocolatechips"))
        self.strawberry = QtGui.QRadioButton(self.groupBox)
        self.strawberry.setGeometry(QtCore.QRect(30, 110, 131, 17))
        self.strawberry.setObjectName(_fromUtf8("strawberry"))
        self.verticalLayout.addWidget(self.groupBox)
        self.DrinksBox = QtGui.QGroupBox(self.widget)
        self.DrinksBox.setCheckable(True)
        self.DrinksBox.setObjectName(_fromUtf8("DrinksBox"))
        self.coffee = QtGui.QRadioButton(self.DrinksBox)
        self.coffee.setGeometry(QtCore.QRect(30, 30, 82, 17))
        self.coffee.setObjectName(_fromUtf8("coffee"))
        self.colddrink = QtGui.QRadioButton(self.DrinksBox)
        self.colddrink.setGeometry(QtCore.QRect(30, 60, 101, 17))
        self.colddrink.setObjectName(_fromUtf8("colddrink"))
        self.juice = QtGui.QRadioButton(self.DrinksBox)
        self.juice.setGeometry(QtCore.QRect(30, 90, 82, 17))
        self.juice.setObjectName(_fromUtf8("juice"))
        self.verticalLayout.addWidget(self.DrinksBox)
        self.widget1 = QtGui.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(201, 13, 181, 271))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.gridLayout = QtGui.QGridLayout(self.widget1)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 148, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget1)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.CalculateButton = QtGui.QPushButton(self.widget1)
        self.CalculateButton.setObjectName(_fromUtf8("CalculateButton"))
        self.gridLayout.addWidget(self.CalculateButton, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Ice Creams", None))
        self.vanilla.setText(_translate("Dialog", "Plain Vanilla $5", None))
        self.blacksunday.setText(_translate("Dialog", "Black Sunday $10", None))
        self.chocolatechips.setText(_translate("Dialog", "Chocolate Chips $20", None))
        self.strawberry.setText(_translate("Dialog", "Strawberry $15", None))
        self.DrinksBox.setTitle(_translate("Dialog", "Drinks", None))
        self.coffee.setText(_translate("Dialog", "Coffee $5", None))
        self.colddrink.setText(_translate("Dialog", "Cold Drink $10", None))
        self.juice.setText(_translate("Dialog", "Juice $15", None))
        self.CalculateButton.setText(_translate("Dialog", "Calculate Bill", None))

