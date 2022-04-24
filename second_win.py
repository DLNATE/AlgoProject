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
        # self.btn_test2.clicked.connect(self.timer_sits)
        # self.btn_test3.clicked.connect(self.timer_final)
    def next_window(self):
        pass
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.setFixedSize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
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
        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.line3 = QLineEdit()
        self.line4 = QLineEdit()
        self.line5 = QLineEdit()
        self.Layout.addWidget(self.Text1, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.line1, alignment= Qt.AlignLeft)

        self.Layout.addWidget(self.Text2, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.line2, alignment= Qt.AlignLeft)

        self.Layout.addWidget(self.Text3, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.Btn1, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.line3, alignment= Qt.AlignLeft)

        self.Layout.addWidget(self.Text4, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.Btn2, alignment= Qt.AlignLeft)

        self.Layout.addWidget(self.Text5, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.Btn3, alignment= Qt.AlignLeft)

        self.Layout.addWidget(self.line4, alignment= Qt.AlignLeft)
        self.Layout.addWidget(self.line5, alignment= Qt.AlignLeft)
        
        self.Layout.addWidget(self.Btn4, alignment= Qt.AlignCenter)
        



        self.Text22 = QLabel("00:00:15")
        self.Layout.addWidget(self.Text22)
        self.setLayout(self.Layout)
    
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def timer_1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer_2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer_2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.Text22.setText(time.toString("hh:mm:ss"))
        
        self.Text22.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.Text22.setText(time.toString("hh:mm:ss"))
        
        self.Text22.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()
        

