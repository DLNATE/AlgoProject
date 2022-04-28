# напиши здесь код для второго экрана приложения
from instr import *
from final_win import *
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
from PyQt5.QtCore import Qt, QTimer, QTime

class SecondWin(QWidget):
    def connects(self):
        self.Btn1.clicked.connect(self.timer_1)
        self.Btn2.clicked.connect(self.timer_2)
        self.Btn3.clicked.connect(self.timer_3)
        self.Btn4.clicked.connect(self.next_window)
    def next_window(self):
        self.lol = 1
        if str(self.line2.text()) == "" or self.line2.text() == str():
            self.emt = QMessageBox()
            self.emt.setText("Вы не ввели Возраст!")
            self.emt.setWindowTitle('Сообщение')
            self.emt.show()
        elif self.test1_result.text() == "":
            self.emt1 = QMessageBox()
            self.emt1.setText("Вы не ввели Результаты!\n        Теста 1")
            self.emt1.setWindowTitle('Сообщение')
            self.emt1.show()
        elif self.test2_result.text() == "":
            self.emt11 = QMessageBox()
            self.emt11.setText("Вы не ввели Результаты!\n       Теста 2")
            self.emt11.setWindowTitle('Сообщение')
            self.emt11.show()
        elif self.test3_result.text() == "":
            self.emt111 = QMessageBox()
            self.emt111.setText("Вы не ввели Результаты!\n       Теста 3")
            self.emt111.setWindowTitle('Сообщение')
            self.emt111.show()
        else:
            self.finalwin = FinalWin(self.line2.text(), self.test1_result.text(), self.test2_result.text(), self.test3_result.text(), self.teme)
            self.hide()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.setFixedSize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self, teme):
        self.Layout = QVBoxLayout()
        self.Layout2 = QVBoxLayout()
        self.Text1 = QLabel('Введите Ф.И.О.:')
        self.Text2 = QLabel('Полных лет:')
        self.Text3 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
        self.Text4 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счётчик приседаний.')
        self.Text5 = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.')
        self.Btn1 = QPushButton('Начать первый тест')
        self.Btn2 = QPushButton('Начать делать приседания')
        self.Btn3= QPushButton('Начать финальный тест')
        self.Btn4 = QPushButton('Отправить результаты')
        self.line1 = QLineEdit(teme['user.name'])
        
        self.line2 = QLineEdit(teme['user.age'])
        self.test1_result = QLineEdit()
        self.test2_result = QLineEdit()
        self.test3_result = QLineEdit()
        self.Layout.addWidget(self.Text1, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.line1, alignment= Qt.AlignLeft)

        self.Layout.addWidget(self.Text2, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.line2, alignment= Qt.AlignLeft)
        
        self.Layout.addWidget(self.Text3, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.Btn1, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.test1_result, alignment= Qt.AlignLeft)
        self.Text22 = QLabel("00:00:15")
        self.Text22.setStyleSheet('font-size: 30px')
        self.Layout.addWidget(self.Text22, alignment= Qt.AlignRight)
        
        self.Layout.addWidget(self.Text4, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.Btn2, alignment= Qt.AlignLeft)

        self.Layout.addWidget(self.Text5, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.Btn3, alignment= Qt.AlignLeft)

        self.Layout.addWidget(self.test2_result, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.test3_result, alignment= Qt.AlignLeft)
        
        self.Layout.addWidget(self.Btn4, alignment= Qt.AlignCenter)
        



        
        self.setLayout(self.Layout)
        if self.teme['user.theme'] == 'dark':
            self.setStyleSheet('background: black')
            self.Text1.setStyleSheet('color: white')
            self.Text2.setStyleSheet('color: white')
            self.Text22.setStyleSheet('color: white')
            self.Text3.setStyleSheet('color: white')
            self.Text4.setStyleSheet('color: white')
            self.Text5.setStyleSheet('color: white')
            self.line1.setStyleSheet('background: rgb(250,250,250)')
            self.line2.setStyleSheet('background: rgb(250,250,250)')
            self.test1_result.setStyleSheet('background: rgb(250,250,250)')
            self.test2_result.setStyleSheet('background: rgb(250,250,250)')
            self.test3_result.setStyleSheet('background: rgb(250,250,250)')
            self.Btn1.setStyleSheet('background: rgb(0, 0, 153); padding: 5px 15px')
            self.Btn2.setStyleSheet('background: rgb(0, 0, 153); padding: 5px 15px')
            self.Btn3.setStyleSheet('background: rgb(0, 0, 153); padding: 5px 15px')
            self.Btn4.setStyleSheet('background: rgb(0, 0, 153); padding: 5px 15px')
            
            

    def __init__(self, teme):
        super().__init__()
        self.teme = teme
        self.set_appear()
        self.initUI(self.teme)
        self.connects()
        self.show()
        
    def timer_1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
        if self.teme['user.theme'] == 'dark':
            self.Text22.setStyleSheet('color: white')
    def timer_2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
        if self.teme['user.theme'] == 'dark':
            self.Text22.setStyleSheet('color: white')
    def timer_3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)
        if self.teme['user.theme'] == 'dark':
            self.Text22.setStyleSheet('color: white')
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.Text22.setText(time.toString("hh:mm:ss"))
        
        
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.Text22.setText(time.toString("hh:mm:ss"))
        
        
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        if time.toString("hh:mm:ss") == "00:00:45":
            if self.teme['user.theme'] == 'dark':
                self.Text22.setStyleSheet('color: white')
            else:
                self.Text22.setStyleSheet("color: rgb(0,0,0)")

        if time.toString("hh:mm:ss") == "00:00:15":
            self.Text22.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:59":
           
            self.Text22.setStyleSheet("color: rgb(0,250,0)")