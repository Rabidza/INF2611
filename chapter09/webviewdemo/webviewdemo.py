# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webviewdemo.ui'
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
        Dialog.resize(709, 599)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.siteURL = QtGui.QLineEdit(Dialog)
        self.siteURL.setGeometry(QtCore.QRect(72, 20, 531, 20))
        self.siteURL.setObjectName(_fromUtf8("siteURL"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(620, 20, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.webView = QtWebKit.QWebView(Dialog)
        self.webView.setGeometry(QtCore.QRect(10, 70, 691, 521))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Address", None))
        self.pushButton.setText(_translate("Dialog", "Go", None))

from PyQt4 import QtWebKit
