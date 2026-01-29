from PyQt5.QtWidgets import QMainWindow
from .main_window import Ui_MainWindow
from .borrower import BorrowerForm


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.borrower_form = None
        self.ui.manage_borrowers_pushButton.clicked.connect(self.open_borrower_form)

    def open_borrower_form(self):
        if self.borrower_form is None:
            self.borrower_form = BorrowerForm()
        self.borrower_form.show()
