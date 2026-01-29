from PyQt5.QtWidgets import QApplication, QDialog
from ui.login import LoginForm
from ui.main_form import MainForm
import sys

app = QApplication([])

login_dialog = LoginForm()
if login_dialog.exec_() == login_dialog.Accepted:
    main_form = MainForm()
    main_form.show()

app.exec_()

