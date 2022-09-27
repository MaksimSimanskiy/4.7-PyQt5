#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Решите задачу: напишите программу, состоящую из семи кнопок, цвета которых
соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен
вставляться код цвета, а в метку – название цвета.
атеричной кодировке: #ff0000 – красный, #ff7d00 – оранжевый,
#ffff00 – желтый, #00ff00 – зеленый, #007dff – голубой, #0000ff – синий, #7d00ff –
фиолетовый.

"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit,QHBoxLayout
from PyQt5.QtCore import Qt
app = QApplication(sys.argv)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ")
        self.label = QLabel("Text")
        self.setGeometry(230, 200, 230, 200)
        self.e1 = QLineEdit()
        self.dar = {'#ff0000': 'Красный',
        '#ff7d00': 'Оранжевый',
        '#ffff00': 'Желтый',
        '#00ff00': 'Зеленый',
        '#007dff': 'Голубой',
        '#0000ff': 'Синий',
        '#7d00ff': 'Фиолетовый'}
        vbox = QVBoxLayout()
        grid = QHBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.e1)
        vbox.addLayout(grid)
        self.label.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)
        for key, colour in self.dar.items():
            sa = lambda k=key, ruc=self.dar[key]: self.onclick(key, ruc)
            b = QPushButton(" ")
            grid.addWidget(b)
            b.setStyleSheet(f"background-color: {key};")
            b.clicked.connect(sa)

    def onclick(self, colour, ru_colour):
        self.label.setText(str(ru_colour))
        self.e1.setText(str(colour))


application = Window()
application.show()


if __name__ == '__main__':
    sys.exit(app.exec())