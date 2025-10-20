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

        self.ui.pushButton_add.clicked.connect(self.add_student)


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


    def add_student(self):
        firstname = self.ui.lineEdit.text()
        lastname = self.ui.lineEdit_2.text()
        birthdate = self.ui.lineEdit_3.text()
        address = self.ui.lineEdit_4.text()
        class_id = self.ui.lineEdit_5.text()
        parent_phone = self.ui.lineEdit_6.text()

        if not firstname:
            QMessageBox.warning(self, 'error',  'please enter the firstname')
            return
        q = "INSERT INTO students VALUES(DEFAULT, %s, %s, %s, %s, %s, %s)"
        self.db.execute(q, (firstname, 
                                                                                         lastname,
                                                                                         birthdate,
                                                                                         int(class_id),
                                                                                         address,
                                                                                         parent_phone))
        
        self.load_students()
        self.clear_input()


    def clear_input(self):
        self.ui.lineEdit.clear()


    def delete_student(self):
        selected = self.ui.tableWidget.currentRow()
        student_id = self.ui.tableWidget.item(selected, 0).text()