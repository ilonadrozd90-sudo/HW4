from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSpinBox, QTableWidget
import sys
import os
from About import About

class Grades(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("mainWindow")
        self.setWindowTitle("Grades Correction System")
        self.setGeometry(200,200,650,600)

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''

        self.face()

    def face(self):
        self.load = QPushButton("Load your file:", self)
        self.load.setGeometry(20, 20, 160, 30)

        self.table = QTableWidget(50, 3, self)
        self.table.setGeometry(20, 60, 600, 400)
        self.table.setHorizontalHeaderLabels(["ID", "Original Grades", "Corrected Grades"])
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)

        bonus_label = QLabel("Enter bonus:", self)
        bonus_label.setGeometry(20, 470, 100, 30)

        self.bonus_input = QSpinBox(self)
        self.bonus_input.setRange(0, 100)
        self.bonus_input.setValue(0)
        self.bonus_input.setGeometry(110, 470, 100, 30)

        self.update = QPushButton("Update file", self)
        self.update.setGeometry(500, 470, 100, 30)

        self.about = QPushButton("About", self)
        self.about.clicked.connect(self.show_about)
        self.about.setGeometry(20, 525, 150, 30)


    def show_about(self):
        self.about_window = About()
        self.about_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())

    window = Grades()
    window.show()
    sys.exit(app.exec())
