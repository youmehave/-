# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_win.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class User_UI_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(756, 557)
        self.layoutWidget_12 = QtWidgets.QWidget(Form)
        self.layoutWidget_12.setGeometry(QtCore.QRect(50, 100, 671, 381))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tableWidget_printData = QtWidgets.QTableWidget(self.layoutWidget_12)
        self.tableWidget_printData.setObjectName("tableWidget_printData")
        self.tableWidget_printData.setColumnCount(4)
        self.tableWidget_printData.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_printData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_printData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_printData.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_printData.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_11.addWidget(self.tableWidget_printData)
        self.verticalScrollBar_printData = QtWidgets.QScrollBar(self.layoutWidget_12)
        self.verticalScrollBar_printData.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_printData.setObjectName("verticalScrollBar_printData")
        self.horizontalLayout_11.addWidget(self.verticalScrollBar_printData)
        self.layoutWidget_13 = QtWidgets.QWidget(Form)
        self.layoutWidget_13.setGeometry(QtCore.QRect(50, 50, 671, 30))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget_13)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_printList = QtWidgets.QPushButton(self.layoutWidget_13)
        self.pushButton_printList.setObjectName("pushButton_printList")
        self.horizontalLayout_15.addWidget(self.pushButton_printList)
        self.lineEdit_findFile = QtWidgets.QLineEdit(self.layoutWidget_13)
        self.lineEdit_findFile.setObjectName("lineEdit__findFile")
        self.horizontalLayout_15.addWidget(self.lineEdit_findFile)
        self.pushButton_findFile = QtWidgets.QPushButton(self.layoutWidget_13)
        self.pushButton_findFile.setObjectName("pushButton_findFile")
        self.horizontalLayout_15.addWidget(self.pushButton_findFile)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 30, 301, 16))
        self.label.setObjectName("label")
        self.pushButton_rename = QtWidgets.QPushButton(Form)
        self.pushButton_rename.setGeometry(QtCore.QRect(500, 510, 93, 28))
        self.pushButton_rename.setObjectName("pushButton_rename")
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(610, 510, 93, 28))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget_printData.horizontalHeaderItem(0)
        item.setText(_translate("Form", "文件编号"))
        item = self.tableWidget_printData.horizontalHeaderItem(1)
        item.setText(_translate("Form", "文件名"))
        item = self.tableWidget_printData.horizontalHeaderItem(2)
        item.setText(_translate("Form", "命名日期"))
        item = self.tableWidget_printData.horizontalHeaderItem(3)
        item.setText(_translate("Form", "是否为附件"))
        self.pushButton_printList.setText(_translate("Form", "打印文件列表"))
        self.pushButton_findFile.setText(_translate("Form", "查询文件"))
        self.label.setText(_translate("Form", "输入文件编号查询文件"))
        self.pushButton_rename.setText(_translate("Form", "重命名文件"))
        self.pushButton_cancel.setText(_translate("Form", "退出"))

