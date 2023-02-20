
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QEvent
import sys


class App(QApplication):
    def notify(self, object, event):
        if object.inherits("QPushButton") and event.type() == 2:
            print(object, event.type())
            print("按钮被点击了")
        return super().notify(object, event)




if __name__ == "__main__":
    app = App(sys.argv)
    window = QWidget()
    btn = QPushButton(window)
    btn.move(100, 100)
    btn.setText("按钮")
    window.show()
    sys.exit(app.exec())
