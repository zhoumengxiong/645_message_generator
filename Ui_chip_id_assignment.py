# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\MyProjects\ChaoKongQiComCommand\chip_id_assignment.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chip_id_assignment(object):
    def setupUi(self, chip_id_assignment):
        chip_id_assignment.setObjectName("chip_id_assignment")
        chip_id_assignment.resize(589, 303)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        chip_id_assignment.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/resources/windows_704px_1210167_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        chip_id_assignment.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(chip_id_assignment)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_mac = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.le_mac.setFont(font)
        self.le_mac.setMaxLength(10000)
        self.le_mac.setObjectName("le_mac")
        self.gridLayout.addWidget(self.le_mac, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 1)
        chip_id_assignment.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chip_id_assignment)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 26))
        self.menubar.setObjectName("menubar")
        chip_id_assignment.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(chip_id_assignment)
        self.statusbar.setObjectName("statusbar")
        chip_id_assignment.setStatusBar(self.statusbar)

        self.retranslateUi(chip_id_assignment)
        QtCore.QMetaObject.connectSlotsByName(chip_id_assignment)

    def retranslateUi(self, chip_id_assignment):
        _translate = QtCore.QCoreApplication.translate
        chip_id_assignment.setWindowTitle(_translate("chip_id_assignment", "智芯D版抄控器修改MAC报文生成工具"))
        self.label.setText(_translate("chip_id_assignment", "MAC地址输入框："))
        self.le_mac.setPlaceholderText(_translate("chip_id_assignment", "输入12位MAC地址"))
        self.label_2.setText(_translate("chip_id_assignment", "生成的报文如下:"))
import apprcc_rc
