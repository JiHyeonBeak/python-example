import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
window = MyWindow()
window.title("안녕히계세요!")
window.show()
app.exec_()