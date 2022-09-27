#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, в которой имеется несколько объединенных в группу радиокнопок,
индикатор которых выключен (indicatoron=0). Если какая-нибудь кнопка включается, то в
метке должна отображаться соответствующая ей информация. Обычных кнопок в окне быть
не должно.
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QPushButton, QLabel, QRadioButton, QGridLayout
from PyQt5.QtCore import Qt
app = QApplication(sys.argv)

persons = {
    'Вася': '+7 909 466-60-43',
    'Петя': '+7 900 100-13-13',
    'Маша': '+7 948 133-10-10'
}

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 100, 300, 100)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.radio_button_1 = QPushButton('Вася')
        self.radio_button_1.setCheckable(True)
        self.radio_button_2 = QPushButton('Петя')
        self.radio_button_2.setCheckable(True)
        self.radio_button_3 = QPushButton('Маша')
        self.radio_button_3.setCheckable(True)
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.radio_button_1)
        self.button_group.addButton(self.radio_button_2)
        self.button_group.addButton(self.radio_button_3)
        self.button_group.buttonClicked.connect(self._on_radio_button_clicked)
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.radio_button_1, 1, 0)
        grid.addWidget(self.radio_button_2, 2, 0)
        grid.addWidget(self.radio_button_3, 3, 0)
        grid.addWidget(self.label, 2, 2)
        self.setLayout(grid)

    def _on_radio_button_clicked(self, button):
        print(button)
        self.label.setText(persons[button.text()])


application = Window()
application.show()


if __name__ == '__main__':
    sys.exit(app.exec())