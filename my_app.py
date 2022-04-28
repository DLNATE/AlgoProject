# напиши здесь код основного приложения и первого экрана
from instr import *
import json
import sys
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
    def saveProfile(profile):
        with open('src/'+profile['profile.name']+'.json', 'w')as file:
            json.dump(profile, file)
    def deleteProfile(profile):
        os.remove('src/'+profile['profile.name']+'.json')
        os.execl(sys.executable, sys.executable, *sys.argv)
    mainApp = QApplication([])
    class MainWin(QWidget):
        def changeDarkTheme(self):
            self.userData['user.theme'] = 'dark'
            saveProfile(self.userData)
            self.setStyleSheet('background: black')
            self.darkTheme.setStyleSheet('color: white; margin-left: 100px')
            self.lightTheme.setStyleSheet('color: white; margin-left: 20px')
            self.helloText.setStyleSheet('color: white')
            self.instrText.setStyleSheet('color: white; font-size: 14px')
            self.startBtn.setStyleSheet('background: rgb(0, 0, 153); padding: 5px 15px')
        def changeLightTheme(self):
            self.userData['user.theme'] = 'light'
            saveProfile(self.userData)
            self.setStyleSheet('background: white')
            self.darkTheme.setStyleSheet('color: black; margin-left: 100px')
            self.lightTheme.setStyleSheet('color: black; margin-left: 20px')
            self.helloText.setStyleSheet('color: black')
            self.instrText.setStyleSheet('color: black; font-size: 14px')
            self.startBtn.setStyleSheet('background: white')
        def next_window(self):
            self.secondWin = SecondWin(self.userData)
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
                self.changeDarkTheme()
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
        'profile.name' : 'guest'
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
            self.profilecreateBtn.clicked.connect(lambda: self.runMainWindow(self.userData))
        def set_appear(self):
            self.userData = data
            self.setWindowTitle('loadProfile')
            self.setFixedSize(win_width, win_height)
            self.move(win_x, win_y)
            self.setLayout(self.mainLayout)
        def initUI(self):
            self.mainLayout = QVBoxLayout()
            
            self.radioBtnGroup = QButtonGroup()
            self.helloTxt = QLabel('Добро пожаловать, выберите профиль, если он есть\nИли создайте новый, еще вы можетепродолжить как гость')
            self.newProfileBtn = QPushButton('Создать новый профиль')
            self.goGuest = QPushButton('Продолжить как гость')
            self.loadingLayout = QVBoxLayout()
            self.secondLayout = QHBoxLayout()
            self.loadingLayout.addWidget(self.helloTxt, alignment= Qt.AlignCenter)
            self.newProfileBtn.clicked.connect(lambda: self.profileInit(self.userData))
            self.goGuest.clicked.connect(lambda: self.runMainWindow(self.userData))
            self.secondLayout.addWidget(self.newProfileBtn)
            self.secondLayout.addWidget(self.goGuest)
            self.loadingLayout.addLayout(self.secondLayout)
            for i in profiles:
                self.profilesLayout = QHBoxLayout()
                with open('src/'+i , 'r')as file:
                    self.profile = json.load(file)
                self.profileBtn = QRadioButton(self.profile['profile.name'])
                self.deleteProfile = QPushButton('delete')
                self.deleteProfile.setStyleSheet('margin-right: 500px')
                self.profilesLayout.addWidget(self.profileBtn, 10)
                self.profilesLayout.addWidget(self.deleteProfile, 90)
                self.radioBtnGroup.addButton(self.profileBtn)
                self.mainLayout.addLayout(self.profilesLayout)
                self.profileBtn.clicked.connect(lambda: self.runMainWindow(self.profile))
                self.deleteProfile.clicked.connect(lambda: deleteProfile(self.profile))
            
            self.mainLayout.addLayout(self.loadingLayout)
        def runMainWindow(self, data):
            saveProfile(self.userData)
            self.hide()
            self.mw = MainWin(data)
        def __init__(self):
            super().__init__()
            self.initUI()
            self.set_appear()
            self.show()
    profileWin = ProfileWin()
    mainApp.exec_()
if __name__ == '__main__':
    main()