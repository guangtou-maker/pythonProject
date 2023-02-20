
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QObject, Qt
import sys


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("测试")
        self.resize(400, 400)
        self.move(200, 200)
        self.setup_ui()

    def setup_ui(self):
        obj = QObject()
        # 设置父对象
        obj.setParent()
        # 获取父对象
        obj.parent()
        # 获取所有直接子对象
        obj.children()
        obj.findChild(object, "notice", Qt.FindChildOption())
        '''
        获取某一个指定名称和类型的子对象，参数：
        1、类型
        2、名称
        3、查询选项         
        '''


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = Window()
    # window.show()

    qwd = QWidget()
    label = QLabel()
    label.setText("ceshi")
    label.setParent(qwd)

    button = QPushButton()
    button.setText("btn")
    button.setParent(qwd)
    button.move(100, 100)

    for sub_widget in qwd.findChildren(QLabel):
        sub_widget.setStyleSheet("background-color:cyan")

    qwd.show()

    sys.exit(app.exec())
