import project
from PyQt5 import QtCore, QtWidgets
from random import choice

from myWin import UiFirstMenu
from movieUi import Ui_MovieMainWindow
from animeUi import Ui_AnimeMainWindow
from bookUi import Ui_BookMainWindow
from hobbyUi import Ui_HobbyMainWindow


class MovieWindow(QtWidgets.QMainWindow, Ui_MovieMainWindow):
    def __init__(self):
        super(MovieWindow, self).__init__()
        self.setup_ui(self)

        self.resize(300, 300)

        self.label_3 = QtWidgets.QLabel()
        self.label_4 = QtWidgets.QLabel()

        grid = QtWidgets.QGridLayout(self.central_widget)
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.label_2, 1, 0)
        grid.addWidget(self.comboBox, 2, 0)
        grid.addWidget(self.label_3, 3, 0)
        grid.addWidget(self.label_4, 4, 0)
        grid.addWidget(self.movie_btn, 5, 0)

        self.movie_btn.clicked.connect(self.movie_action)
        self.comboIndex = 0
        self.comboBox.activated[int].connect(self.on_activated_text_movie)

    @QtCore.pyqtSlot(int)
    def on_activated_text_movie(self, index):
        self.comboIndex = index

    def movie_action(self):
        data = project.data_movie()
        response_text_title = data[0]
        response_text_genre_action_title = data[1]
        response_text_genre_romance_title = data[2]
        response_text_genre_drama_title = data[3]
        response_text_genre_any_title = data[4]

        if self.comboIndex == 0:
            self.label_3.setText(response_text_title[self.comboIndex])
            self.label_4.setText(choice(response_text_genre_action_title))
        elif self.comboIndex == 1:
            self.label_3.setText(response_text_title[self.comboIndex])
            self.label_4.setText(choice(response_text_genre_romance_title))
        elif self.comboIndex == 2:
            self.label_3.setText(response_text_title[self.comboIndex])
            self.label_4.setText(choice(response_text_genre_drama_title))


class AnimeWindow(QtWidgets.QMainWindow, Ui_AnimeMainWindow):
    def __init__(self):
        super(AnimeWindow, self).__init__()
        self.setup_ui(self)

        self.resize(300, 300)

        self.label_3 = QtWidgets.QLabel()

        grid = QtWidgets.QGridLayout(self.central_widget)
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.label_2, 1, 0)
        grid.addWidget(self.comboBox, 2, 0)
        grid.addWidget(self.label_3, 3, 0)
        grid.addWidget(self.anime_btn, 4, 0)

        self.anime_btn.clicked.connect(self.anime_action)
        self.comboIndex = 0
        self.comboBox.activated[int].connect(self.on_activated_text_anime)

    @QtCore.pyqtSlot(int)
    def on_activated_text_anime(self, index):
        self.comboIndex = index

    def anime_action(self):
        data = project.data_anime()
        response_text_genre_romance_title = data[0][0]
        response_text_genre_drama_title = data[0][1]
        response_text_genre_action_title = data[0][2]

        if self.comboIndex == 0:
            self.label_3.setText(choice(response_text_genre_romance_title))
        elif self.comboIndex == 1:
            self.label_3.setText(choice(response_text_genre_drama_title))
        elif self.comboIndex == 2:
            self.label_3.setText(choice(response_text_genre_action_title))


class BookWindow(QtWidgets.QMainWindow, Ui_BookMainWindow):
    def __init__(self):
        super(BookWindow, self).__init__()
        self.setup_ui(self)

        self.resize(300, 300)

        self.label_3 = QtWidgets.QLabel()

        grid = QtWidgets.QGridLayout(self.central_widget)
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.label_2, 1, 0)
        grid.addWidget(self.comboBox, 2, 0)
        grid.addWidget(self.label_3, 3, 0)
        grid.addWidget(self.book_btn, 4, 0)

        self.book_btn.clicked.connect(self.book_action)
        self.comboIndex = 0
        self.comboBox.activated[int].connect(self.on_activated_text_book)

    @QtCore.pyqtSlot(int)
    def on_activated_text_book(self, index):
        self.comboIndex = index

    def book_action(self):
        data = project.data_book()
        response_text_genre_romance_title = data[0][0]
        response_text_genre_horror_title = data[0][1]
        response_text_genre_detective_title = data[0][2]

        if self.comboIndex == 0:
            self.label_3.setText(choice(response_text_genre_romance_title))
        elif self.comboIndex == 1:
            self.label_3.setText(choice(response_text_genre_horror_title))
        elif self.comboIndex == 2:
            self.label_3.setText(choice(response_text_genre_detective_title))


class HobbyMain(QtWidgets.QMainWindow, Ui_HobbyMainWindow):
    def __init__(self):
        super(HobbyMain, self).__init__()
        self.setup_ui(self)

        self.resize(300, 300)

        self.label_3 = QtWidgets.QLabel()

        grid = QtWidgets.QGridLayout(self.central_widget)
        grid.addWidget(self.label, 0, 0)
        grid.addWidget(self.label_2, 1, 0)
        grid.addWidget(self.comboBox, 2, 0)
        grid.addWidget(self.label_3, 3, 0)
        grid.addWidget(self.manga_btn, 4, 0)

        self.manga_btn.clicked.connect(self.hobby_action)
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
            self.label_3.setText(response_text_genre_general['hobby'])
        elif self.comboIndex == 1:
            self.label_3.setText(response_text_genre_education['hobby'])
        elif self.comboIndex == 2:
            self.label_3.setText(response_text_genre_competition['hobby'])


class MainWindow(QtWidgets.QMainWindow, UiFirstMenu):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setup_ui(self)

        self.movie_btn.setText('Movie. Open the window.')
        self.movie_btn.setCheckable(True)
        self.movie_btn.clicked.connect(self.go_to_movie)

        self.anime_btn.setText('Anime. Open the window.')
        self.anime_btn.setCheckable(True)
        self.anime_btn.clicked.connect(self.go_to_anime)

        self.book_btn.setText('Book. Open the window.')
        self.book_btn.setCheckable(True)
        self.book_btn.clicked.connect(self.go_to_book)

        self.manga_btn.setText('You don\'t khow what you want to do. Open the window.')
        self.manga_btn.setCheckable(True)
        self.manga_btn.clicked.connect(self.go_to_hobby)

        self.movie_window = MovieWindow()
        self.anime_window = AnimeWindow()
        self.book_window = BookWindow()
        self.hobby_window = HobbyMain()

    def go_to_movie(self, state):
        if state:
            self.movie_window.show()
            self.movie_btn.setText('Close the window.')
        else:
            self.movie_window.hide()
            self.movie_btn.setText('Movie. Open the window.')

    def go_to_anime(self, state):
        if state:
            self.anime_window.show()
            self.anime_btn.setText('Close the window.')
        else:
            self.anime_window.hide()
            self.anime_btn.setText('Anime. Open the window.')

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
            self.manga_btn.setText('Close the window')
        else:
            self.hobby_window.hide()
            self.manga_btn.setText('You don\'t khow what you want to do. Open the window.')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
