# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabwidgetdemo.ui'
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
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(30, 20, 341, 241))
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 0);\n"
"font: 8pt \"MS Shell Dlg 2\";"))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(40, 40, 121, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 80, 121, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.tab)
        self.checkBox_3.setGeometry(QtCore.QRect(40, 130, 121, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.checkBox_8 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_8.setGeometry(QtCore.QRect(50, 30, 121, 17))
        self.checkBox_8.setObjectName(_fromUtf8("checkBox_8"))
        self.checkBox_9 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_9.setGeometry(QtCore.QRect(50, 90, 121, 17))
        self.checkBox_9.setObjectName(_fromUtf8("checkBox_9"))
        self.checkBox_10 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_10.setGeometry(QtCore.QRect(50, 150, 121, 17))
        self.checkBox_10.setObjectName(_fromUtf8("checkBox_10"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_4.setGeometry(QtCore.QRect(40, 30, 121, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox_5 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_5.setGeometry(QtCore.QRect(40, 70, 121, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_6 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_6.setGeometry(QtCore.QRect(40, 120, 121, 17))
        self.checkBox_6.setObjectName(_fromUtf8("checkBox_6"))
        self.checkBox_7 = QtGui.QCheckBox(self.tab_3)
        self.checkBox_7.setGeometry(QtCore.QRect(40, 170, 121, 17))
        self.checkBox_7.setObjectName(_fromUtf8("checkBox_7"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.checkBox.setText(_translate("Dialog", "Pizza    $25", None))
        self.checkBox_2.setText(_translate("Dialog", "Hot Dog    $5", None))
        self.checkBox_3.setText(_translate("Dialog", "Chicken Burger    $10", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Food", None))
        self.checkBox_8.setText(_translate("Dialog", "Juice    $15", None))
        self.checkBox_9.setText(_translate("Dialog", "Cold Drink    $10", None))
        self.checkBox_10.setText(_translate("Dialog", "Coffee    $5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Drinks", None))
        self.checkBox_4.setText(_translate("Dialog", "Vanilla    $5", None))
        self.checkBox_5.setText(_translate("Dialog", "Strawberry    $7", None))
        self.checkBox_6.setText(_translate("Dialog", "Pineapple    $8", None))
        self.checkBox_7.setText(_translate("Dialog", "Chocolate    $10", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Ice Creams", None))

