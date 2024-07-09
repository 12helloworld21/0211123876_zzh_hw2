from PyQt5 import QtWidgets, QtGui, QtCore
from monitor.main_dialog import Ui_Dialog
from monitor.monitorframe import MonitorDialog
from monitor.Face_frame import Face_Dialog
from monitor.injure_detection_frame import injure_Dialog
import data.resources_rc

class MainDialog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel(self)#QLabel是Qt中用于显示文本或图像的控件
        self.setCentralWidget(self.label)#将之前创建的QLabel（即self.label）设置为窗口的中心部件
        self.pixmap = QtGui.QPixmap(":1.jpeg")#背景图，QPixmap是用于处理图像的类
        # 设置QLabel的尺寸
        self.label.resize(self.width(), self.height())
        self.label.setScaledContents(True)
        # 将背景图片设置为QLabel的内容
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))
        # 监听窗口大小变化事件
        self.resizeEvent = self.on_resize
        self.ui = Ui_Dialog()#！！！！！！！！！！！！！！！实例化一个Ui_Dialog类，该类用于设置对话框（Dialog）的用户界面
        self.ui.setupUi(self)#调用Ui_Diaolog类的setupUi函数



    def on_resize(self, event):
        self.label.resize(self.width(), self.height())
        self.label.setPixmap(self.pixmap.scaled(self.label.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation))

    def goin(self):
        self.monitorframe = MonitorDialog()
        self.monitorframe.show()

    def face_detect(self):
        self.monitorframe = Face_Dialog()
        self.monitorframe.show()

    def dehicle_injure_detection(self):
        self.monitorframe = injure_Dialog()
        self.monitorframe.show()
