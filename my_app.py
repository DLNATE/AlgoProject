# напиши здесь код основного приложения и первого экрана
from instr import *
import json
import os.path
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
            self.theme = self.userData
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
            if self.userData['user.theme'] == 'dark':
                self.darkTheme.setChecked(True)
            self.setLayout(self.mainLayout)
        def connects(self):
            self.startBtn.clicked.connect(self.next_window)
            self.darkTheme.clicked.connect(self.changeDarkTheme)
            self.lightTheme.clicked.connect(self.changeLightTheme)
        def __init__(self, profile):
            super().__init__()
            self.userData = profile
            self.set_appear()
            self.initUI()
            self.connects()
            self.show()
    if os.path.exists('src/') == False:
        os.mkdir('src/')
    data = {
        'user.name' : '',
        'user.age' : '',
        'user.theme' : 'light',
        'profile.name' : ''
    }
    firstOpen = ''
    path = 'src/'
    profilesCount = len(os.listdir(path))
    profiles = os.listdir(path)
    if profilesCount == 0:
        firstOpen = True
    class ProfileWin(QWidget):
        def saveProfile(self):
            self.userData['profile.name'] = self.profileUserName.text()
            self.userData['user.name'] = self.userNameLine.text()
            self.userData['user.age'] = self.userAgeLine.text()
            with open('src/'+self.userData['profile.name']+'.json', 'w')as file:
                json.dump(self.userData, file)
        def profileInit(self,profile):
            self.helloTxt.deleteLater()
            self.newProfileBtn.deleteLater()
            self.goGuest.deleteLater()
            self.secondLayout.deleteLater()
            self.profileUserName = QLineEdit()
            self.profileUserName.setPlaceholderText('Введите название профиля')
            self.profileUserName.setFixedWidth(240)
            self.userNameLine = QLineEdit()
            self.userNameLine.setPlaceholderText(txt_name)
            self.userNameLine.setFixedWidth(240)
            self.userAgeLine = QLineEdit()
            self.userAgeLine.setPlaceholderText(txt_age)
            self.userAgeLine.setFixedWidth(240)
            self.profilecreateBtn = QPushButton('Создать')
            self.profileUserName.setMaxLength(10)
            self.mainLayout.addWidget(self.profileUserName, alignment= Qt.AlignCenter)
            self.mainLayout.addWidget(self.userNameLine, alignment= Qt.AlignCenter)
            self.mainLayout.addWidget(self.userAgeLine, alignment= Qt.AlignCenter)
            self.mainLayout.addWidget(self.profilecreateBtn, alignment= Qt.AlignCenter)
            self.profilecreateBtn.clicked.connect(self.saveProfile)
            self.profilecreateBtn.clicked.connect(self.runMainWindow)
        def set_appear(self):
            self.userData = data
            self.setWindowTitle('loadProfile')
            self.setFixedSize(win_width, win_height)
            self.move(win_x, win_y)
            self.setLayout(self.mainLayout)
        def initUI(self):
            self.mainLayout = QVBoxLayout()
            self.profilesLayout = QVBoxLayout()
            self.radioBtnGroup = QButtonGroup()

            if firstOpen:
                self.helloTxt = QLabel('Добро пожаловать, у вас нету профиля\nХотите создать новый или продолжите как гость?')
                self.newProfileBtn = QPushButton('Создать новый профиль')
                self.goGuest = QPushButton('Продолжить как гость')
                self.loadingLayout = QVBoxLayout()
                self.secondLayout = QHBoxLayout()
                self.loadingLayout.addWidget(self.helloTxt, alignment= Qt.AlignCenter)
                self.secondLayout.addWidget(self.newProfileBtn)
                self.secondLayout.addWidget(self.goGuest)
                self.loadingLayout.addLayout(self.secondLayout)
                self.mainLayout.addLayout(self.loadingLayout)
                self.newProfileBtn.clicked.connect(lambda: self.profileInit(self.userData))
                self.goGuest.clicked.connect(self.runMainWindow)
            else:
                if profilesCount == 1:
                    with open("src/"+profiles[0], 'r')as firstProfile:
                        self.firstProfile = json.load(firstProfile)
                        self.firstProfileBtn = QRadioButton(self.firstProfile['profile.name'])
                    self.profilesLayout.addWidget(self.firstProfileBtn)
                    self.radioBtnGroup.addButton(self.firstProfileBtn)
                elif profilesCount == 2:
                    with open("src/"+profiles[0], 'r')as firstProfile:
                        self.firstProfile = json.load(firstProfile)
                        self.firstProfileBtn = QRadioButton(self.firstProfile['profile.name'])
                    with open("src/"+profiles[1], 'r')as secondProfile:
                        self.secondProfile = json.load(secondProfile)
                        self.secondProfileBtn = QRadioButton(self.secondProfile['profile.name'])
                    self.profilesLayout.addWidget(self.firstProfileBtn)
                    self.profilesLayout.addWidget(self.secondProfileBtn)
                    self.radioBtnGroup.addButton(self.firstProfileBtn)
                    self.radioBtnGroup.addButton(self.secondProfileBtn)
                elif profilesCount == 3:
                    with open("src/"+profiles[0], 'r')as firstProfile:
                        self.firstProfile = json.load(firstProfile)
                        self.firstProfileBtn = QRadioButton(self.firstProfile['profile.name'])
                    with open("src/"+profiles[1], 'r')as secondProfile:
                        self.secondProfile = json.load(secondProfile)
                        self.secondProfileBtn = QRadioButton(self.secondProfile['profile.name'])
                    with open("src/"+profiles[2], 'r')as thirdProfile:
                        self.thirdProfile = json.load(thirdProfile)
                        self.thirdProfileBtn = QRadioButton(self.thirdProfile['profile.name'])
                    self.profilesLayout.addWidget(self.firstProfileBtn)
                    self.profilesLayout.addWidget(self.secondProfileBtn)
                    self.profilesLayout.addWidget(self.thirdProfileBtn)
                    self.radioBtnGroup.addButton(self.firstProfileBtn)
                    self.radioBtnGroup.addButton(self.secondProfileBtn)
                    self.radioBtnGroup.addButton(self.thirdProfileBtn)
                self.mainLayout.addLayout(self.profilesLayout)
        def runMainWindow(self):
            self.hide()
            self.mw = MainWin(self.userData)
        def connects(self):
            pass
        def __init__(self):
            super().__init__()
            self.initUI()
            self.set_appear()
            self.connects()
            self.show()
    profileWin = ProfileWin()
    mainApp.exec_()
if __name__ == '__main__':
    main()