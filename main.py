import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import design  # Это наш конвертированный файл дизайна
import json


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.show_info)
        with open('data_file.json', 'r') as f:
            self.data = json.load(f)
            print(self.data)

    def show_info(self):
        self.textBrowser.setText(self.data[self.lineEdit.text()])
        print(self.lineEdit.text())
        picture = self.lineEdit.text().split()
        self.label.setPixmap(QPixmap('image/%s.jpg'%picture[1]))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
