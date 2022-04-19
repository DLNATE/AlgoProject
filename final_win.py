# напиши здесь код третьего экрана приложения
from json.tool import main
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
    def results(self):
        self.index = (4*(int(self.test1_result)+int(self.test2_result)+int(self.test3_result))- 200) / 10
        if self.age == 7 or self.age == 8:
            if self.index <= 6.4:
                self.resultTest = 'Высокий'
            elif self.index >= 6.5 and self.index <= 11.9:
                self.resultTest = 'Выше среднего'
            elif self.index >= 12 and self.index <= 16.9:
                self.resultTest = 'Средний'
            elif self.index >= 17 and self.index <= 20.9:
                self.resultTest = 'Удовлетворительный'
            elif self.index >= 21:
                self.resultTest = 'Низкий'
        elif self.age == 9 or self.age == 10:
            if self.index <= 4.9:
                self.resultTest = 'Высокий'
            elif self.index >= 5 and self.index <= 10.4:
                self.resultTest = 'Выше среднего'
            elif self.index >= 10.5 and self.index <= 15.4:
                self.resultTest = 'Средний'
            elif self.index >= 15.5 and self.index <= 19.4:
                'Удовлетворительный'
            elif self.index >= 19.5:
                self.resultTest = 'Низкий'
        elif self.age == 11 or self.age == 12:
            if self.index <= 3.4:
                self.resultTest = 'Высокий'
            elif self.index >= 3.5 and self.index <= 8.9:
                self.resultTest = 'Выше среднего'
            elif self.index >= 9 and self.index <= 13.9:
                self.resultTest = 'Средний'
            elif self.index >= 14 and self.index <= 17.9:
                self.resultTest = 'Удовлетворительный'
            elif self.index >= 18:
                self.resultTest = 'Низкий'
        elif self.age == 13 or self.age == 14:
            if self.index <= 1.9:
                self.resultTest = 'Высокий'
            elif self.index >= 2 and self.index <= 7.4:
                self.resultTest = 'Выше среднего'
            elif self.index >= 7.5 and self.index <= 12.4:
                self.resultTest = 'Средний'
            elif self.index >= 12.5 and self.index <= 16.4:
                self.resultTest = 'Удовлетворительный'
            elif self.index >= 18:
                self.resultTest = 'Низкий'
        elif self.age >= 15:
            if self.inidex <= 0.4:
                self.resultTest = 'Высокий'
            elif self.index >= 0.5 and self.index <= 5.9:
                self.resultTest = 'Выше среднего'
            elif self.index >= 6 and self.index <= 10.9:
                self.resultTest = 'Средний'
            elif self.index >= 11 and self.index <= 14.9:
                self.resultTest = 'Удовлетворительный'
            elif self.index >= 15:
                self.resultTest = 'Низкий'
    def set_appear(self):
        self.setWindowTitle(txt_finalwin)
        self.setFixedSize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.thkForUsing = QMessageBox()
        self.thkForUsing.setWindowTitle('Спасибо за использование!')
        self.thkForUsing.setText(programmers)
        self.thkForUsing.show()
        self.mainLayout = QVBoxLayout()
        self.yourIndex = QLabel('Ваш индекс Руфье: '+ str(self.index))
        self.yourResults = QLabel('Ваш результат: '+self.resultTest)
        self.mainLayout.addWidget(self.yourIndex, alignment= Qt.AlignCenter)
        self.mainLayout.addWidget(self.yourResults, alignment= Qt.AlignCenter)
        self.setLayout(self.mainLayout)
    def connects(self):
        pass
    def __init__(self, age, test1_result, test2_result, test3_result):
        super().__init__()
        self.age = int(age)
        self.test1_result = test1_result
        self.test2_result = test2_result
        self.test3_result = test3_result
        self.results()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()