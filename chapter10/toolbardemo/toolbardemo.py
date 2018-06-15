# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolbardemo.ui'
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 181, 16))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionPlus = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon images/plus.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlus.setIcon(icon)
        self.actionPlus.setObjectName(_fromUtf8("actionPlus"))
        self.actionMinus = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon images/minus.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMinus.setIcon(icon1)
        self.actionMinus.setObjectName(_fromUtf8("actionMinus"))
        self.actionDivide = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon images/divide.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDivide.setIcon(icon2)
        self.actionDivide.setObjectName(_fromUtf8("actionDivide"))
        self.actionMultiply = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon images/multiply.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMultiply.setIcon(icon3)
        self.actionMultiply.setObjectName(_fromUtf8("actionMultiply"))
        self.actionEqual = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon images/equal.ICO")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEqual.setIcon(icon4)
        self.actionEqual.setObjectName(_fromUtf8("actionEqual"))
        self.toolBar.addAction(self.actionPlus)
        self.toolBar.addAction(self.actionMinus)
        self.toolBar.addAction(self.actionMultiply)
        self.toolBar.addAction(self.actionDivide)
        self.toolBar.addAction(self.actionEqual)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "TextLabel", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionPlus.setText(_translate("MainWindow", "Plus", None))
        self.actionPlus.setToolTip(_translate("MainWindow", "Plus", None))
        self.actionMinus.setText(_translate("MainWindow", "Minus", None))
        self.actionMinus.setToolTip(_translate("MainWindow", "Minus", None))
        self.actionDivide.setText(_translate("MainWindow", "Divide", None))
        self.actionDivide.setToolTip(_translate("MainWindow", "Divide", None))
        self.actionMultiply.setText(_translate("MainWindow", "Multiply", None))
        self.actionMultiply.setToolTip(_translate("MainWindow", "Multiply", None))
        self.actionEqual.setText(_translate("MainWindow", "Equal", None))
        self.actionEqual.setToolTip(_translate("MainWindow", "Equal", None))

import tmpresource_rc
