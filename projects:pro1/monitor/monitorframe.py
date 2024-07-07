from PyQt5 import QtCore
from PyQt5.Qt import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog
from monitor.mfui import Ui_Dialog
from monitor.Video import Video

class MonitorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.th1 = Video('data/vd3.mp4')
        # 绑定信号与槽函数
        #将 Video 实例 self.th1 的 send 信号连接到当前对话框的 showimg 槽函数。
        #这意味着每当 self.th1 发出 send 信号时，都会调用 showimg 方法来处理接收到的数据。
        self.th1.send.connect(self.showimg)
        self.th1.start()


    def showimg(self, h, w, c, b, th_id,num):
        imgae = QImage(b, w, h, w * c, QImage.Format_BGR888)
        pix = QPixmap.fromImage(imgae)
        if th_id == 1:
            # 自动缩放
            width = self.ui.video1.width()
            height = self.ui.video1.height()
            scale_pix = pix.scaled(width, height, Qt.KeepAspectRatio)
            self.ui.video1.setPixmap(scale_pix)
            # str(num) 类型转换
            self.ui.carnum.setText(str(num))


