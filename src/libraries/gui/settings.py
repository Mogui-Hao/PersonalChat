# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\项目\SimpleChat\ReconstructGUI\src\libraries\gui/Settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.comboBox = ComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(80, 100, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "简体中文"))
        self.comboBox.setItemText(1, _translate("Form", "繁体中文"))
        self.comboBox.setItemText(2, _translate("Form", "English"))
from qfluentwidgets import ComboBox
