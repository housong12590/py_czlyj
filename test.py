import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QToolTip)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)


app = QApplication(sys.argv)

w = MainWindow()
w.resize(400, 300)
w.show()
sys.exit(app.exec_())
