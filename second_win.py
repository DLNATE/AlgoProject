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

class SecondWin(QWidget):
    def clicked(self):
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test1.clicked.connect(self.timer_test)
        self.btn_test2.clicked.connect(self.timer_sits)
        self.btn_test3.clicked.connect(self.timer_final)
    def next_window(self):
        pass
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.setFixedSize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.Layout = QVBoxLayout()
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
        self.Layout.addWidget(self.Text1)
        self.Layout.addWidget(self.line1)

        self.Layout.addWidget(self.Text2)
        self.Layout.addWidget(self.line2)

        self.Layout.addWidget(self.Text3)
        self.Layout.addWidget(self.Btn1)
        self.Layout.addWidget(self.line3)

        self.Layout.addWidget(self.Text4)
        self.Layout.addWidget(self.Btn2)

        self.Layout.addWidget(self.Text5)
        self.Layout.addWidget(self.Btn3)

        self.Layout.addWidget(self.line3)
        self.Layout.addWidget(self.line5)
        self.Layout.addWidget(self.Btn4, alignment= Qt.AlignCenter)
        

    def connects(self):
        pass
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


