from PyQt5.QtWidgets import QMainWindow
from .main_window import Ui_MainWindow
from .borrower import BorrowerForm
from .borrower_table_model import BorrowerTableModel
from models.borrowerController import BorrowerController


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.table_model = BorrowerTableModel()

        self.controller = BorrowerController()
        self.ui.tableView.setModel(self.table_model)

        self.load_borrowers()
        self.borrower_form = None
        self.ui.manage_borrowers_pushButton.clicked.connect(self.open_borrower_form)

    def open_borrower_form(self):
        if self.borrower_form is None:
            self.borrower_form = BorrowerForm()
            self.borrower_form.borrower_created.connect(self.load_borrowers)
        self.borrower_form.show()

    def load_borrowers(self):
        print("+++++++++++++++++++")
        borrowers_data = self.controller.get_all_borrowers()
        self.table_model.update_data(borrowers_data)
