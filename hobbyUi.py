from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HobbyMainWindow(object):
    def setup_ui(self, hobby_main_window):
        hobby_main_window.setObjectName("MainWindow")
        hobby_main_window.resize(400, 220)                        # 400
        hobby_main_window.setMinimumSize(QtCore.QSize(400, 220))  # 400
        hobby_main_window.setMaximumSize(QtCore.QSize(400, 220))  # 400
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons8-Ios7-Cinema-Documentary.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hobby_main_window.setWindowIcon(icon)
        hobby_main_window.setAccessibleName("")
        self.central_widget = QtWidgets.QWidget(hobby_main_window)
        self.central_widget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 21))
        self.label.setObjectName("label")
        self.manga_btn = QtWidgets.QPushButton(self.central_widget)
        self.manga_btn.setGeometry(QtCore.QRect(10, 140, 121, 31))
        self.manga_btn.setObjectName("pushButton")
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
        hobby_main_window.setCentralWidget(self.central_widget)

        self.retranslate_ui(hobby_main_window)
        QtCore.QMetaObject.connectSlotsByName(hobby_main_window)

    def retranslate_ui(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Know You Better"))
        self.label.setText(_translate("MainWindow", "Help you choose a hobby ?!"))
        self.manga_btn.setText(_translate("MainWindow", "Click on me"))
        self.label_2.setText(_translate("MainWindow", "Select genre"))
        self.comboBox.setCurrentText(_translate("MainWindow", "General"))
        self.comboBox.setItemText(0, _translate("MainWindow", "General"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Education"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Competition"))