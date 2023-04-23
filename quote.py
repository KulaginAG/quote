import requests
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # Заголовок окна
        self.setWindowTitle('Цитаты')

        # Изменение фона цвета
        self.setStyleSheet('background-color: black;')

        # Создание вертикального layout для виджета
        layout = QVBoxLayout()

        # Создание label для вывода цитаты
        self.quote_label = QLabel('')
        self.quote_label.setStyleSheet('color: white; font-size: 36px; font-family: Roboto;')
        layout.addWidget(self.quote_label)
        self.quote_label.setWordWrap(True)

        # Создание кнопки "Покажи еще"
        self.show_button = QPushButton('Покажи еще')
        self.show_button.setStyleSheet('color: white; font-size: 28px; font-family: Roboto;')
        self.show_button.clicked.connect(self.show_quote)
        layout.addWidget(self.show_button)

        # Создание кнопки "Закрыть"
        self.close_button = QPushButton('Закрыть')
        self.close_button.setStyleSheet('color: white; font-size: 14px; font-family: Roboto;')
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)

        # Установка выравнивания по центру для layout'а
        layout.setAlignment(QtCore.Qt.AlignCenter)

        # Создание виджета и установка layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Инициализация цитаты
        self.show_quote()
        self.resize(1500, 500)
        self.setWindowState(QtCore.Qt.WindowFullScreen)

    def show_quote(self):
        # Запрос к API для получения цитаты
        url = 'https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=ru'
        response = requests.get(url)
        quote = response.json()

        # Извлечение текста цитаты и автора (если указан)
        text = quote['quoteText']
        author = quote.get('quoteAuthor', 'Unknown')

        # Установка текста цитаты в label
        self.quote_label.setText(f'{text}\n\n{author}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # Установка размера шрифта для label и кнопок
    font = QFont('Roboto')
    font.setPointSize(36)
    window.quote_label.setFont(font)
    window.show_button.setFont(font)
    window.close_button.setFont(font)

    window.show()
    sys.exit(app.exec_())
