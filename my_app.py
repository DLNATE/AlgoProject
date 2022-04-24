# напиши здесь код основного приложения и первого экрана
from instr import *
import json
import os.path as os
from loadProfile import *
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
    QPushButton,
    QRadioButton,
    QButtonGroup
)

def main():
    mainApp = QApplication([])
    class MainWin(QWidget):
        def changeDarkTheme(self):
            self.theme = 'dark'
            self.setStyleSheet('background: black')
            self.darkTheme.setStyleSheet('color: white; margin-left: 100px')
            self.lightTheme.setStyleSheet('color: white; margin-left: 20px')
            self.helloText.setStyleSheet('color: white')
            self.instrText.setStyleSheet('color: white; font-size: 14px')
            self.startBtn.setStyleSheet('background: rgb(0, 0, 153); padding: 5px 15px')
        def changeLightTheme(self):
            self.theme = 'light'
            self.setStyleSheet('background: white')
            self.darkTheme.setStyleSheet('color: black; margin-left: 100px')
            self.lightTheme.setStyleSheet('color: black; margin-left: 20px')
            self.helloText.setStyleSheet('color: black')
            self.instrText.setStyleSheet('color: black; font-size: 14px')
            self.startBtn.setStyleSheet('background: white')
        def next_window(self):
            self.secondWin = SecondWin(self.theme)
            self.hide()
        def set_appear(self):
            self.setWindowTitle(txt_title)
            self.setFixedSize(win_width, win_height)
            self.move(win_x, win_y)
        def initUI(self):
            self.theme = 'light'
            self.raidioBtnLayout = QHBoxLayout()
            self.radioBtnGroup = QButtonGroup()
            self.darkTheme = QRadioButton('Темная тема')
            self.darkTheme.setStyleSheet('margin-left: 100px')
            self.lightTheme = QRadioButton('Светлая тема')
            self.lightTheme.setStyleSheet('margin-left: 20px')
            self.lightTheme.setChecked(True)
            self.raidioBtnLayout.addWidget(self.darkTheme, 10)
            self.raidioBtnLayout.addWidget(self.lightTheme, 90)
            self.radioBtnGroup.addButton(self.darkTheme)
            self.radioBtnGroup.addButton(self.lightTheme)
            self.whoProgrammers = QMessageBox()
            self.whoProgrammers.setText(programmers)
            self.whoProgrammers.setWindowTitle('Авторы')
            self.whoProgrammers.show()
            self.mainLayout = QVBoxLayout()
            self.helloText = QLabel(txt_hello)
            self.instrText = QLabel(txt_instruction)
            self.instrText.setStyleSheet('font-size: 14px')
            self.startBtn = QPushButton(txt_next)
            self.startBtn.setStyleSheet('padding: 5px 15px')
            self.mainLayout.addLayout(self.raidioBtnLayout)
            self.mainLayout.addWidget(self.helloText, alignment= Qt.AlignCenter)
            self.mainLayout.addWidget(self.instrText, alignment= Qt.AlignCenter)
            self.mainLayout.addWidget(self.startBtn, alignment= Qt.AlignCenter)
            self.setLayout(self.mainLayout)
        def connects(self):
            self.startBtn.clicked.connect(self.next_window)
            self.darkTheme.clicked.connect(self.changeDarkTheme)
            self.lightTheme.clicked.connect(self.changeLightTheme)
        def __init__(self):
            super().__init__()
            self.set_appear()
            self.initUI()
            self.connects()
            self.show()
    mw = MainWin()
    mainApp.exec_()
if __name__ == '__main__':
    main()