from PyQt5 import QtCore, QtGui, QtWidgets
from styles import styles

class Ui_MovieMainWindow(object):

    def setup_ui(self, movie_main_window):
        self.setStyleSheet(styles)

        movie_main_window.setGeometry(1200, 300, 400, 600)

        movie_main_window.setObjectName("MainWindow")
        movie_main_window.resize(400, 600)
        movie_main_window.setMinimumSize(QtCore.QSize(400, 600))
        movie_main_window.setMaximumSize(QtCore.QSize(400, 600))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons8-Ios7-Cinema-Documentary.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        movie_main_window.setWindowIcon(icon)

        movie_main_window.setAccessibleName("")
        self.central_widget = QtWidgets.QWidget(movie_main_window)
        self.central_widget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.central_widget)
        #self.label.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.label.setObjectName("label")

        self.movie_btn = QtWidgets.QPushButton(self.central_widget)
        #self.movie_btn.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.movie_btn.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(self.central_widget)
        #self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_2.setObjectName("label_2")

        self.comboBox = QtWidgets.QComboBox(self.central_widget)
        #self.comboBox.setGeometry(QtCore.QRect(10, 80, 121, 22))
        self.comboBox.setMaxVisibleItems(8)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        movie_main_window.setCentralWidget(self.central_widget)

        self.retranslate_ui(movie_main_window)
        QtCore.QMetaObject.connectSlotsByName(movie_main_window)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WSID"))
        self.label.setText(_translate("MainWindow", "Help you choose a movie ?!"))
        self.movie_btn.setText(_translate("MainWindow", "Click on me"))
        self.label_2.setText(_translate("MainWindow", "Select genre:"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Action"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Action"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Fantasy"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Drama"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Romance"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Animation"))

