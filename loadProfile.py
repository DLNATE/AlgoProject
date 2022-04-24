from ctypes import alignment
from itertools import count
import json
from instr import *
import os.path 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
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
    def profileInit(self,profile):
        self.helloTxt.deleteLater()
        self.newProfileBtn.deleteLater()
        self.goGuest.deleteLater()
        self.secondLayout.deleteLater()
        self.profileUserName = QLineEdit()
        self.profileUserName.setPlaceholderText('Введите название профиля')
        self.profileUserName.setFixedWidth(240)
        self.userNameLine = QLineEdit()
        self.userNameLine.setPlaceholderText('Введите свое имя')
        self.userNameLine.setFixedWidth(240)
        self.userAgeLine = QLineEdit()
        self.userAgeLine.setPlaceholderText('Введите свой возраст')
        self.userAgeLine.setFixedWidth(240)
        self.profilecreateBtn = QPushButton('Создать')
        self.profileUserName.setMaxLength(10)
        self.mainLayout.addWidget(self.profileUserName, alignment= Qt.AlignCenter)
        self.mainLayout.addWidget(self.userNameLine, alignment= Qt.AlignCenter)
        self.mainLayout.addWidget(self.userAgeLine, alignment= Qt.AlignCenter)
        self.mainLayout.addWidget(self.profilecreateBtn, alignment= Qt.AlignCenter)
        self.userData['profile.name'] = self.profileUserName.text()
        self.userData['user.name'] = self.userNameLine.text()
        self.userData['user.age'] = self.userAgeLine.text()
        self.mainLayout = QVBoxLayout() 
    def newProfileInit(self):
        self.profileInit(self.userData)
    def creatProfile(self, profileName):
        with open('src/'+profileName+'.json', 'w')as profile:
            json.dump(data, profile)
        with open('src/'+profileName+'.json', 'r')as profile:
            self.userData = json.load(profile)
        self.newProfileInit()
    def set_appear(self):
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
        
    def connects(self):
        self.newProfileBtn.clicked.connect(lambda: self.creatProfile('1'))
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.connects()
        self.show()