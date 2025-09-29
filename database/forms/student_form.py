from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem
from ui.student_management_form import Ui_Dialog
from db import Database

class StudentForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.db = Database()
        self.load_students()


    def load_students(self):
        self.ui.tableWidget.setRowCount(0)
        query = "SELECT * FROM students"
        students = self.db.fetch_all(query)
        self.ui.tableWidget.setColumnCount(len(dict(students[0]).keys()))
        self.ui.tableWidget.setHorizontalHeaderLabels(dict(students[0]).keys())
        self.ui.tableWidget.setRowCount(0)
        for row_num, row in enumerate(students):
            self.ui.tableWidget.insertRow(row_num)
            col_index = 0
            for col_num, data in dict(row).items():
                self.ui.tableWidget.setItem(row_num, col_index, QTableWidgetItem(str(data)))
                col_index += 1
