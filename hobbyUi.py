from PyQt5 import QtCore, QtGui, QtWidgets
from styles import styles

class Ui_HobbyMainWindow(object):
    def setup_ui(self, hobby_main_window):
        self.setStyleSheet(styles)
        hobby_main_window.setGeometry(1200, 300, 400, 600)

        hobby_main_window.setObjectName("MainWindow")
        hobby_main_window.resize(400, 600)                        # 400
        hobby_main_window.setMinimumSize(QtCore.QSize(400, 600))  # 400
        hobby_main_window.setMaximumSize(QtCore.QSize(400, 600))  # 400
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons8-Ios7-Cinema-Documentary.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        hobby_main_window.setWindowIcon(icon)
        hobby_main_window.setAccessibleName("")

        self.central_widget = QtWidgets.QWidget(hobby_main_window)
        self.central_widget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setObjectName("label")

        self.hobby_btn = QtWidgets.QPushButton(self.central_widget)
        self.hobby_btn.setObjectName("pushButton")

        self.label_2 = QtWidgets.QLabel(self.central_widget)
        self.label_2.setObjectName("label_2")

        self.comboBox = QtWidgets.QComboBox(self.central_widget)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "WSID"))
        self.label.setText(_translate("MainWindow", "Help you choose a hobby ?!"))
        self.hobby_btn.setText(_translate("MainWindow", "Click on me"))
        self.label_2.setText(_translate("MainWindow", "Select genre"))
        self.comboBox.setCurrentText(_translate("MainWindow", "General"))
        self.comboBox.setItemText(0, _translate("MainWindow", "General"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Education"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Competition"))