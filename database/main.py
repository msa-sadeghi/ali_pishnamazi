import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from forms.login_form import LoginForm
from forms.main_form import MainWindow

app  = QApplication(sys.argv)
login = LoginForm()

if login.exec_() == LoginForm.Accepted:
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
