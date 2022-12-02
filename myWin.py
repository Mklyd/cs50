from PyQt5 import QtCore, QtWidgets


class UiFirstMenu(object):
    def setup_ui(self, first_menu):
        first_menu.setObjectName("first_menu")
        first_menu.setStyleSheet("QTextEdit {background-color:red}")
        first_menu.resize(800, 600)
        self.central_widget = QtWidgets.QWidget(first_menu)
        self.central_widget.setObjectName("centralwidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("verticalLayout")

        self.movie_btn = QtWidgets.QPushButton(self.central_widget)
        self.movie_btn.setObjectName("pushButton")
        self.vertical_layout.addWidget(self.movie_btn)

        self.anime_btn = QtWidgets.QPushButton(self.central_widget)
        self.anime_btn.setObjectName("pushButton_2")
        self.vertical_layout.addWidget(self.anime_btn)

        self.book_btn = QtWidgets.QPushButton(self.central_widget)
        self.book_btn.setObjectName("pushButton_2")
        self.vertical_layout.addWidget(self.book_btn)

        self.manga_btn = QtWidgets.QPushButton(self.central_widget)
        self.manga_btn.setObjectName("pushButton_2")
        self.vertical_layout.addWidget(self.manga_btn)

        first_menu.setCentralWidget(self.central_widget)
        self.retranslate_ui(first_menu)
        QtCore.QMetaObject.connectSlotsByName(first_menu)

    def retranslate_ui(self, first_menu):
        _translate = QtCore.QCoreApplication.translate
        first_menu.setWindowTitle(_translate("first_menu", "MainWindow"))
        self.movie_btn.setText(_translate("first_menu", "PushButton"))
        self.anime_btn.setText(_translate("first_menu", "PushButton"))
        self.book_btn.setText(_translate("first_menu", "PushButton"))
        self.manga_btn.setText(_translate("first_menu", "PushButton"))

