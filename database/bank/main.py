# from PyQt5.QtWidgets import QApplication, QDialog
# from ui.login import LoginForm
# import sys

# app = QApplication([])

# login_dialog = LoginForm()
# login_dialog.show()
# app.exec_()

from authentication.auth import AuthManager
a = AuthManager()
a.login('sara', '12345')
