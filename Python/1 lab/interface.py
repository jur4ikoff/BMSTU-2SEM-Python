import sys
import random

from PyQt6.QtGui import QPolygon
from sys import argv, exit
from PyQt6 import uic
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QPainter, QColor
from random import choice, randint
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6 import uic

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtWidgets import QLCDNumber, QLabel, QMainWindow
from PyQt6 import QtCore


# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
#    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
#    QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        # self.setFixedSize(1280, 900)
        # self.pushButton = QPushButton(self)
        # self.pushButton.resize(100, 50)
        # self.pushButton.move(500, 800)
        # self.pushButton.setText('новый круг')
        # self.pushButton.clicked.connect(self.paint)

    def initUI(self):
        # Зададим размер и положение нашего виджета,
        self.setGeometry(300, 300, 600, 900)
        # self.setFixedSize(600, 900)
        # А также его заголовок
        self.setWindowTitle('Калькулятор систем счисления')
        self.btn = QPushButton('Кнопка', self)
        # Подстроим размер кнопки под надпись на ней
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 150)
        # Обратите внимание: функцию не надо вызывать :)
        self.btn.clicked.connect(self.inc_click)

        self.label = QLabel(self)
        # Текст задается также, как и для кнопки
        self.label.setText("Количество нажатий на кнопку")
        self.label.move(80, 30)

        self.LCD_count = QLCDNumber(self)
        self.LCD_count.move(110, 80)

        self.count = 0

    def inc_click(self):
        self.count += 1
        # В QLCDNumber для отображения данных используется метод display()
        self.LCD_count.display(self.count)


class FirstForm(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.initUI()
        uic.loadUi('calc.ui', self)
        self.setFixedSize(400, 600)

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Главная форма')

        self.btn = QPushButton('Другая форма', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(100, 100)

        self.btn.clicked.connect(self.open_second_form)

    def open_second_form(self):
        self.second_form = SecondForm(self, "Данные для второй формы")
        self.second_form.show()


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(argv)
    ex = FirstForm()
    ex.show()
    exit(app.exec())
