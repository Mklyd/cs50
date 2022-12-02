from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AnimeMainWindow(object):
    def setup_ui(self, anime_main_window):
        anime_main_window.setObjectName("MainWindow")
        anime_main_window.resize(400, 220)                        # 400
        anime_main_window.setMinimumSize(QtCore.QSize(400, 220))  # 400
        anime_main_window.setMaximumSize(QtCore.QSize(400, 220))  # 400
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons8-Ios7-Cinema-Documentary.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        anime_main_window.setWindowIcon(icon)
        anime_main_window.setAccessibleName("")
        self.central_widget = QtWidgets.QWidget(anime_main_window)
        self.central_widget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.label.setObjectName("label")
        self.anime_btn = QtWidgets.QPushButton(self.central_widget)
        self.anime_btn.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.anime_btn.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 111, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.central_widget)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 121, 22))
        self.comboBox.setMaxVisibleItems(8)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        anime_main_window.setCentralWidget(self.central_widget)

        self.retranslate_ui(anime_main_window)
        QtCore.QMetaObject.connectSlotsByName(anime_main_window)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Know You Better"))
        self.label.setText(_translate("MainWindow", "Help you choose a anime ?!"))
        self.anime_btn.setText(_translate("MainWindow", "Click on me"))
        self.label_2.setText(_translate("MainWindow", "Select genre"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Romance"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Romance"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Drama"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Action"))