from PyQt5.QtWidgets import QDialog
from ui.login_form import Ui_Dialog
from authentication.auth import AuthManager


class LoginForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_Dialog = Ui_Dialog()
        self.ui_Dialog.setupUi(self)
        self.auth_manager = AuthManager()
        self.ui_Dialog.LoginButton.clicked.connect(self.check_login)

    def check_login(self):
        if self.auth_manager.login(
            self.ui_Dialog.lineEditPassword.text(),
            self.ui_Dialog.lineEditUsername.text(),
        ):
            self.accept()
            print("login success")
