
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import *
import sys


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("测试")
        self.resize(400, 400)
        self.move(200, 200)
        self.qt_object()

    def setup_ui(self):
        pass

    def qt_object(self):
        obj = QObject()
        # 给QT对象设置一个对象名称，一般这个名称是唯一的
        obj.setObjectName("notice")
        # 给QT对象设置一个动态的属性和值
        obj.setProperty("notice", "error")
        print(obj.objectName())
        print(obj.property("notice"))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
