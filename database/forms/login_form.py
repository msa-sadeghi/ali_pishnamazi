from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox

from ui.ui_login import Ui_Dialog


class LoginForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        if username == "admin" and password == "1234":
            # QMessageBox.about(self,  "خوش آمدید", "ورود موفقیت آمیز!")
           
            self.accept()

        else:
            QMessageBox.warning(self, "خطا", "نام کاربری یا کلمه عبور اشتباه است!")
            self.reject()