import random
from random import randint
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QApplication, QWidget
from objs.grid import Ui_Form
from objs.colors import color_list


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # self.ui.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 161))

        def random_color():
            total_lines = len(color_list)
            random_line = randint(1, total_lines)
            label_color = str(color_list[random_line - 1])
            for char2 in '[]':  # удаление квадратных скобок
                label_color = label_color.replace(char2, '')
            # print("border-radius: 17; background-color: " + label_color)
            return "border-radius: 50; background-color: " + label_color
        self.shake_options = [-1, 0, 1]  # Варианты встряхивания

        quantity = 40

        i = 10

        while i < quantity:
            i_str = str(i)  # перевод числа в строку
            i_str_split = str([int(x) for x in i_str])  # сплит строки i_str на символы
            for char in '[]':  # удаление квадратных скобок
                i_str_split = i_str_split.replace(char, '')
            row = int(i_str_split[0])
            column = int(i_str_split[3])

            # label_color = random_color()
            # print(label_color)
            self.ui.label = QtWidgets.QLabel(self.ui.gridLayoutWidget)
            # self.ui.label.setObjectName("label")
            # self.ui.label.setText(i_str)
            # self.ui.label.setGeometry(QtCore.QRect(0, 0, 94, 94))
            self.ui.label.setStyleSheet(random_color())
            self.ui.label.setLineWidth(0)
            self.ui.gridLayout.addWidget(self.ui.label, row, column, 1, 1)

            i = i + 1


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
