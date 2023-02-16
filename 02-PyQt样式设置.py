
from PyQt6.QtWidgets import *
import sys


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("测试")
        self.resize(400, 400)
        self.move(200, 200)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setObjectName("notice")
        label.setText("xxxxx")

        label1 = QLabel(self)
        label1.setText("xxxxxxxxx")
        label1.setObjectName("notice")
        label1.setProperty("level", "success")
        label1.move(100, 100)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("./style.qss") as f:
        app.setStyleSheet(f.read())
    window = Window()
    window.show()
    sys.exit(app.exec())
