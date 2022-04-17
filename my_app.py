# напиши здесь код основного приложения и первого экрана
from instr import *
from second_win import *
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

mainApp = QApplication([])

class MainWin(QWidget):
    def clicked(self):
        self.secondWin = SecondWin()
        self.hide()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.setFixedSize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.mainLayout = QVBoxLayout()
        self.helloText = QLabel(txt_hello)
        self.instrText = QLabel(txt_instruction)
        self.startBtn = QPushButton(txt_next)
        self.mainLayout.addWidget(self.helloText, alignment= Qt.AlignCenter)
        self.mainLayout.addWidget(self.instrText, alignment= Qt.AlignCenter)
        self.mainLayout.addWidget(self.startBtn, alignment= Qt.AlignCenter)
        self.setLayout(self.mainLayout)
    def connects(self):
        self.startBtn.clicked.connect(self.clicked)
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
startwin = MainWin()
mainApp.exec_()
