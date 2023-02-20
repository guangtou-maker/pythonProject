
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QObject
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("")
window.resize(500, 500)
window.move(400, 200)



window.show()



sys.exit(app.exec())
