from PyQt5 import QtWidgets, QtCore
from form_login import Ui_MainWindow
import sys


class FirstForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(FirstForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEdit_password.setStyleSheet("color: rgb(80, 80, 80);")
#         event for button
        self.ui.button_sign_in.clicked.connect(self.btn_click)

    def btn_click(self):
        self.ui.lineEdit_password.setText("")
        self.ui.lineEdit_login.setText("")


def main():
    app = QtWidgets.QApplication([])
    application = FirstForm()
    application.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
