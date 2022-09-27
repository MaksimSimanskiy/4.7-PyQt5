#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу, состоящую из однострочного и многострочного текстовых полей и двух кнопок "Открыть" и "Сохранить".
При клике на первую должен открываться на чтение файл, чье имя указано в поле класса Entry, а содержимое файла
должно загружаться в поле типа Text. При клике на вторую кнопку текст, введенный пользователем в экземпляр Text, должен
сохраняться в файле под именем, которое пользователь указал в однострочном текстовом поле.
Файлы будут читаться и записываться в том же каталоге, что и файл скрипта, если указывать имена файлов без адреса.
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout, QTextEdit,QFileDialog
from PyQt5.QtCore import Qt
app = QApplication(sys.argv)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task4")
        self.setGeometry(470, 390, 470, 390)
        self.inp1 = QTextEdit()
        self.inp2 = QLineEdit()
        self.create()

    def create(self):
        vbox = QVBoxLayout()
        grid = QHBoxLayout()
        vbox.addLayout(grid)
        btn1 = QPushButton("Сохранить")
        btn1.clicked.connect(self.save)
        btn2 = QPushButton("Открыть")
        btn2.clicked.connect(self.open)
        grid.addWidget(self.inp2)
        grid.addWidget(btn1)
        grid.addWidget(btn2)
        vbox.addWidget(self.inp1)
        self.setLayout(vbox)

    def save(self):

        save_file = QFileDialog.getSaveFileName(defaultextension=".txt", filetypes=(("Текстовый файл", "*.txt"),))
        data = self.inp2.text()
        with open(save_file, 'w', encoding="utf-8") as f:
            f.write(data)

    def open(self):
        self.inp1.clear()
        name = QFileDialog.getOpenFileName()
        with open(name, 'r', encoding="utf-8") as f:
            data = f.read()
        self.inp1.setText(str(data))


application = Window()
application.show()


if __name__ == '__main__':
    sys.exit(app.exec())