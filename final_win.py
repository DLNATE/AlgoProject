# напиши здесь код третьего экрана приложения
from instr import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QLineEdit,
    QPushButton
)
class FinalWin(QWidget):
    def clicked(self):
        pass
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.setFixedSize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        pass
    def connects(self):
        pass
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        