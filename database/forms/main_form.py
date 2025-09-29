from PyQt5.QtWidgets import QMainWindow, QMessageBox
from ui.main_form import Ui_MainWindow
from forms.student_form import StudentForm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.exit_menu.triggered.connect(self.close_app)
        self.ui.students_menu.triggered.connect(self.open_students)
        self.ui.classes_menu.triggered.connect(self.open_classes)
        self.ui.subjects_menu.triggered.connect(self.open_subjects)
        self.ui.enrollments_menu.triggered.connect(self.open_enrollments)

    def close_app(self):
        self.close()

    def open_students(self):
        window = StudentForm()
        # window.showFullScreen()
        window.exec_()
    def open_classes(self):
        pass
    def open_subjects(self):
        pass
    def open_enrollments(self):
        pass