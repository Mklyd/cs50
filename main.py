import requests
from PyQt5.QtGui import QPixmap, QImage

import project
from PyQt5 import QtCore, QtWidgets
from random import choice
from PyQt5.QtCore import Qt

from myWin import UiFirstMenu
from movieUi import Ui_MovieMainWindow
from bookUi import Ui_BookMainWindow
from hobbyUi import Ui_HobbyMainWindow
from styles import styles


class MovieWindow(QtWidgets.QMainWindow, Ui_MovieMainWindow):
    def __init__(self):
        super(MovieWindow, self).__init__()
        self.setStyleSheet(styles)

        self.setup_ui(self)
        #self.resize(300, 300)

        self.title = QtWidgets.QLabel()
        self.image = QtWidgets.QLabel()

        grid = QtWidgets.QGridLayout(self.central_widget)
        grid.addWidget(self.label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.label_2, 1, 0,  alignment=Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.comboBox, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(self.title, 2, 0,)
        grid.addWidget(self.image, 3, 0)
        grid.addWidget(self.movie_btn, 4, 0, alignment=Qt.AlignmentFlag.AlignCenter)

        self.movie_btn.clicked.connect(self.movie_action)
        self.comboIndex = 0
        self.comboBox.activated[int].connect(self.on_activated_text_movie)

    @QtCore.pyqtSlot(int)
    def on_activated_text_movie(self, index):
        self.comboIndex = index

    def movie_action(self):
        data = project.data_movie()
        response_text_genre_action_title = data[0]
        response_text_genre_fantasy_title = data[1]
        response_text_genre_drama_title = data[2]
        response_text_genre_romance_title = data[3]
        response_text_genre_animation_title = data[4]

        if self.comboIndex == 0:
            movie = choice(list(response_text_genre_action_title.items()))
            movie_cover = movie[1]
            image = QImage()
            image.loadFromData(requests.get(movie_cover).content)
            self.title.setText(movie[0])
            self.title.setStyleSheet('background: #70688a; padding: 10px;  '
                                     'border-radius: 10px;')
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')
        elif self.comboIndex == 1:
            movie = choice(list(response_text_genre_fantasy_title.items()))
            movie_cover = movie[1]
            image = QImage()
            image.loadFromData(requests.get(movie_cover).content)
            self.title.setStyleSheet('background: #70688a; padding: 10px;  '
                                     'border-radius: 10px;')
            self.title.setText(movie[0])
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')
        elif self.comboIndex == 2:
            movie = choice(list(response_text_genre_drama_title.items()))
            movie_cover = movie[1]
            image = QImage()
            image.loadFromData(requests.get(movie_cover).content)
            self.title.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.title.setText(movie[0])
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')
        elif self.comboIndex == 3:
            movie = choice(list(response_text_genre_romance_title.items()))
            movie_cover = movie[1]
            image = QImage()
            image.loadFromData(requests.get(movie_cover).content)
            self.title.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.title.setText(movie[0])
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')
        elif self.comboIndex == 4:
            movie = choice(list(response_text_genre_animation_title.items()))
            movie_cover = movie[1]
            image = QImage()
            image.loadFromData(requests.get(movie_cover).content)
            self.title.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.title.setText(movie[0])
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')

class BookWindow(QtWidgets.QMainWindow, Ui_BookMainWindow):
    def __init__(self):
        super(BookWindow, self).__init__()
        self.setup_ui(self)
        #self.resize(300, 300)

        self.author = QtWidgets.QLabel()
        self.title = QtWidgets.QLabel()
        self.image = QtWidgets.QLabel()

        grid = QtWidgets.QGridLayout(self.central_widget)
        grid.addWidget(self.label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.label_2, 1, 0,  alignment=Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.comboBox, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(self.author, 2, 0)
        grid.addWidget(self.title, 3, 0)
        grid.addWidget(self.image, 4, 0)
        grid.addWidget(self.book_btn, 5, 0,  alignment=Qt.AlignmentFlag.AlignCenter)

        self.book_btn.clicked.connect(self.book_action)
        self.comboIndex = 0
        self.comboBox.activated[int].connect(self.on_activated_text_book)
    @QtCore.pyqtSlot(int)
    def on_activated_text_book(self, index):
        self.comboIndex = index

    def book_action(self):
        data = project.data_book()
        response_text_genre_childrens_lit_title = data[0]
        response_text_genre_novel_title= data[1]
        response_text_genre_poetry_title = data[2]
        response_text_genre_tragedy_title = data[3]

        if self.comboIndex == 0:
            book_cover = "https://images.unsplash.com/photo-1512903516382-12773959d96c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDV8fGJvb2slMjBkcmFtYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
            image = QImage()
            image.loadFromData(requests.get(book_cover).content)
            book = choice(list(response_text_genre_childrens_lit_title.items()))
            self.author.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.title.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.author.setText(book[0])
            self.title.setText(book[1])
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')
        elif self.comboIndex == 1:
            book_cover = "https://images.unsplash.com/photo-1562232573-0305012a8818?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTR8fGJvb2slMjBkcmFtYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
            image = QImage()
            image.loadFromData(requests.get(book_cover).content)
            book = choice(list(response_text_genre_novel_title.items()))
            self.author.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.title.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.author.setText(book[0])
            self.title.setText(book[1])
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')
        elif self.comboIndex == 2:
            book_cover = "https://images.unsplash.com/photo-1598738865218-7809c17181c3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjR8fGJvb2slMjBwb2V0cnl8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"
            image = QImage()
            image.loadFromData(requests.get(book_cover).content)
            book = choice(list(response_text_genre_poetry_title.items()))
            self.author.setStyleSheet('background: #70688a; padding: 10px;'
                                      'border-radius: 10px;')
            self.title.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.author.setText(book[0])
            self.title.setText(book[1])
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')
        elif self.comboIndex == 3:
            book_cover = "https://images.unsplash.com/photo-1495640388908-05fa85288e61?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mzl8fGJvb2slMjBwb2V0cnl8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"
            image = QImage()
            image.loadFromData(requests.get(book_cover).content)
            book = choice(list(response_text_genre_tragedy_title.items()))
            self.author.setStyleSheet('background: #70688a; padding: 10px; '
                                      'border-radius: 10px;')
            self.title.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.author.setText(book[0])
            self.title.setText(book[1])
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')

class HobbyMain(QtWidgets.QMainWindow, Ui_HobbyMainWindow):
    def __init__(self):
        super(HobbyMain, self).__init__()
        self.setup_ui(self)

        #self.resize(300, 300)

        self.label_3 = QtWidgets.QLabel()
        self.image = QtWidgets.QLabel()

        grid = QtWidgets.QGridLayout(self.central_widget)
        grid.addWidget(self.label, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        grid.addWidget(self.label_2, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        grid.addWidget(self.comboBox, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(self.label_3, 2, 0)
        grid.addWidget(self.image, 3, 0)
        grid.addWidget(self.hobby_btn, 4, 0, alignment=Qt.AlignmentFlag.AlignCenter)

        self.hobby_btn.clicked.connect(self.hobby_action)
        self.comboIndex = 0
        self.comboBox.activated[int].connect(self.on_activated_text_hobby)

    @QtCore.pyqtSlot(int)
    def on_activated_text_hobby(self, index):
        self.comboIndex = index

    def hobby_action(self):
        data = project.data_hobby()
        response_text_genre_general = data[0]
        response_text_genre_education = data[1]
        response_text_genre_competition = data[2]

        if self.comboIndex == 0:
            hobby_cover = "https://images.unsplash.com/photo-1466584241662-8cb021032c1a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8aG9iYnl8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"
            image = QImage()
            image.loadFromData(requests.get(hobby_cover).content)

            self.label_3.setStyleSheet('background: #70688a; padding: 10px; border-radius: 10px;')
            self.label_3.setText(response_text_genre_general['hobby'])
            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')
        elif self.comboIndex == 1:
            hobby_cover = "https://images.unsplash.com/photo-1561089489-f13d5e730d72?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1374&q=80"
            image = QImage()
            image.loadFromData(requests.get(hobby_cover).content)

            self.label_3.setStyleSheet('background: #70688a; padding: 10px; '
                                     'border-radius: 10px;')
            self.label_3.setText(response_text_genre_education['hobby'])

            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')
        elif self.comboIndex == 2:
            hobby_cover = "https://images.unsplash.com/photo-1583782385538-c55baa9420ff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzR8fGNvbXBldGl0aW9ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
            image = QImage()
            image.loadFromData(requests.get(hobby_cover).content)

            self.label_3.setStyleSheet('background: #70688a; padding: 10px;'
                                     'border-radius: 10px;')
            self.label_3.setText(response_text_genre_competition['hobby'])

            high_rez = QtCore.QSize(300, 350)
            pixmap = QPixmap(image)

            pixmap = pixmap.scaled(high_rez)
            self.image.setPixmap(pixmap)
            self.image.setStyleSheet('margin: 0 auto')


class MainWindow(QtWidgets.QMainWindow, UiFirstMenu):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui(self)

        self.movie_btn.setText('Movie. Open the window.')
        self.movie_btn.setCheckable(True)
        self.movie_btn.clicked.connect(self.go_to_movie)

        self.book_btn.setText('Book. Open the window.')
        self.book_btn.setCheckable(True)
        self.book_btn.clicked.connect(self.go_to_book)

        self.hobby_btn.setText('You don\'t know what you want to do. Open the window.')
        self.hobby_btn.setCheckable(True)
        self.hobby_btn.clicked.connect(self.go_to_hobby)

        self.movie_window = MovieWindow()
        self.book_window = BookWindow()
        self.hobby_window = HobbyMain()

    def go_to_movie(self, state):
        if state:
            self.movie_window.show()
            self.movie_btn.setText('Close the window.')
        else:
            self.movie_window.hide()
            self.movie_btn.setText('Movie. Open the window.')

    def go_to_book(self, state):
        if state:
            self.book_window.show()
            self.book_btn.setText('Close the window')
        else:
            self.book_window.hide()
            self.book_btn.setText('Book. Open the window.')

    def go_to_hobby(self, state):
        if state:
            self.hobby_window.show()
            self.hobby_btn.setText('Close the window')
        else:
            self.hobby_window.hide()
            self.hobby_btn.setText('You don\'t know what you want to do. Open the window.')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
