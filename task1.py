#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите простейший калькулятор, состоящий из
двух текстовых полей,куда пользователь вводит числа, и четырех кнопок "+", "-", "*", "/".
Результат вычисления должен отображаться в метке.
Если арифметическое действие выполнить невозможно(например, если были введены буквы, а не числа),
 то в метке должно появляться слово "ошибка".
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt
app = QApplication(sys.argv)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task1")
        self.setGeometry(170, 190, 170, 190)
        self.inp1 = QLineEdit()
        self.inp2 = QLineEdit()
        self.create()

    def create(self):
        vbox = QVBoxLayout()
        btn1 = QPushButton("+")
        btn1.clicked.connect(self.sum)
        btn2 = QPushButton("-")
        btn2.clicked.connect(self.sub)
        btn3 = QPushButton("*")
        btn3.clicked.connect(self.mul)
        btn4 = QPushButton("/")
        btn4.clicked.connect(self.div)
        self.label = QLabel("Text")
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.inp1)
        vbox.addWidget(self.inp2)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def sum(self):
        res = int(self.inp1.text()) + int(self.inp2.text())
        self.label.setText(str(res))

    def sub(self):
        res = int(self.inp1.text()) - int(self.inp2.text())
        self.label.setText(str(res))

    def mul(self):
        res = int(self.inp1.text()) * int(self.inp2.text())
        self.label.setText(str(res))

    def div(self):
        a = int(self.inp1.text())
        b = int(self.inp2.text())
        if a or b != 0:
            res = a / b
            self.label.setText(str(res))


application = Window()
application.show()


if __name__ == '__main__':
    sys.exit(app.exec())