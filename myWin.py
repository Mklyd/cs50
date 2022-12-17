from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class UiFirstMenu(object):
    def setup_ui(self, first_menu):
        first_menu.setGeometry(300, 300, 400, 400)
        first_menu.setObjectName("first_menu")
        first_menu.setStyleSheet("background: #70688a")
        first_menu.setFont(QFont('Arial', 18))
        first_menu.resize(800, 600)
        self.central_widget = QtWidgets.QWidget(first_menu)
        self.central_widget.setObjectName("centralwidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("verticalLayout")

        self.movie_btn = QtWidgets.QPushButton(self.central_widget)
        self.movie_btn.setObjectName("pushButton")
        self.movie_btn.setStyleSheet('background: #dadae3;padding: 15px; margin: 15px 100px;border: 1px solid #dadae3; '
                                     'border-radius: 10px;')
        self.movie_btn.setFont(QFont('Arial', 18))
        self.vertical_layout.addWidget(self.movie_btn)

        self.book_btn = QtWidgets.QPushButton(self.central_widget)
        self.book_btn.setObjectName("pushButton_2")
        self.book_btn.setStyleSheet('background: #dadae3;padding: 15px; margin: 15px 100px;border: 1px solid #dadae3; '
                                    'border-radius: 10px;')
        self.book_btn.setFont(QFont('Arial', 18))
        self.vertical_layout.addWidget(self.book_btn)

        self.hobby_btn = QtWidgets.QPushButton(self.central_widget)
        self.hobby_btn.setObjectName("pushButton_2")
        self.hobby_btn.setStyleSheet('background: #dadae3;padding: 15px; margin: 15px 100px;border: 1px solid '
                                     '#dadae3; border-radius: 10px;')
        self.hobby_btn.setFont(QFont('Arial', 18))
        self.vertical_layout.addWidget(self.hobby_btn)

        first_menu.setCentralWidget(self.central_widget)
        self.retranslate_ui(first_menu)
        QtCore.QMetaObject.connectSlotsByName(first_menu)

    def retranslate_ui(self, first_menu):
        _translate = QtCore.QCoreApplication.translate
        first_menu.setWindowTitle(_translate("first_menu", "What Should I Do ?"))
        self.movie_btn.setText(_translate("first_menu", "PushButton"))
        self.book_btn.setText(_translate("first_menu", "PushButton"))
        self.hobby_btn.setText(_translate("first_menu", "PushButton"))
