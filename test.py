
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
        label.setText("xxxx")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
