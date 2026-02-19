from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.borrower_form import Ui_MainWindow
from models.borrowerController import BorrowerController
from PyQt5.QtCore import pyqtSignal

class BorrowerForm(QMainWindow):
    borrower_created = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui_Dialog = Ui_MainWindow()
        self.ui_Dialog.setupUi(self)
        self.ui_Dialog.pushButton.clicked.connect(self.submit)
        self.controller = BorrowerController()

    def submit(self):
        data = {
            "first_name": self.ui_Dialog.lineEdit.text(),
            "last_name": self.ui_Dialog.lineEdit_2.text(),
            "national_code": self.ui_Dialog.lineEdit_3.text(),
            "phone": "1234",
        }

        if self.controller.create_borrower(data):
            QMessageBox.information(self, "Success", "Borrower created Succussfully")
            self.borrower_created.emit()
            self.close()
