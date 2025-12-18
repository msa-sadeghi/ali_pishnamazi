from PyQt5.QtWidgets import QDialog
from ui.login_form import Ui_Dialog
class LoginForm(QDialog):
    def __init__(self):
        super().__init__()
        ui_Dialog = Ui_Dialog()
        ui_Dialog.setupUi(self)