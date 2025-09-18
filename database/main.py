import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from forms.login_form import LoginForm


app  = QApplication(sys.argv)
login = LoginForm()

if login.exec_() == LoginForm.Accepted:
    pass
    # sys.exit(app.exec_())
else:
    print("not valid")


