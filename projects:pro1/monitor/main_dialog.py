# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(764, 602)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 50, 341, 141))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.vehicle_putton = QtWidgets.QPushButton(Dialog)
        self.vehicle_putton.setGeometry(QtCore.QRect(280, 300, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.vehicle_putton.setFont(font)
        self.vehicle_putton.setObjectName("vehicle_putton")
        self.face_detect = QtWidgets.QPushButton(Dialog)
        self.face_detect.setGeometry(QtCore.QRect(280, 380, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.face_detect.setFont(font)
        self.face_detect.setObjectName("face_detect")

        self.retranslateUi(Dialog)
        self.vehicle_putton.clicked.connect(Dialog.goin) # type: ignore
        self.face_detect.clicked.connect(Dialog.face_detect) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "欢迎使用车流量检测和人流量检测系统"))
        self.vehicle_putton.setText(_translate("Dialog", "人车流量检测"))
        self.face_detect.setText(_translate("Dialog", "人脸识别"))
