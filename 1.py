from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSpinBox, QTableWidget, QTableWidgetItem
import sys
import os
import subprocess
from About import About
from file_select import FileSelect

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
        self.load.clicked.connect(self.load_file)

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
        self.bonus_input.lineEdit().returnPressed.connect(self.add_bonus)

        self.update = QPushButton("Update file", self)
        self.update.setGeometry(500, 470, 100, 30)
        self.update.clicked.connect(self.update_file)

        self.about = QPushButton("About", self)
        self.about.clicked.connect(self.show_about)
        self.about.setGeometry(20, 525, 150, 30)


    def show_about(self):
        self.about_window = About()
        self.about_window.show()


    def load_file(self):
        self.file_window = FileSelect(self)
        self.file_window.show()

    def read(self):
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []

        with open(self.selected_file, "r") as f:
            lines = f.readlines()

        for line in lines[1:]:
            parts = line.strip().split(",")
            if len(parts) >= 2:
                student_id = parts[0].strip()
                grade = int(parts[1].strip())

                self.student_ids.append(student_id)
                self.original_grades.append(grade)
                self.corrected_grades.append(grade)

        self.update_table()

    def update_table(self):
        self.table.clearContents()
        for row in range(len(self.student_ids)):
            self.table.setItem(row, 0, QTableWidgetItem(str(self.student_ids[row])))
            self.table.setItem(row, 1, QTableWidgetItem(str(self.original_grades[row])))
            self.table.setItem(row, 2, QTableWidgetItem(str(self.corrected_grades[row])))

    def add_bonus(self):
        bonus = self.bonus_input.value()

        for i in range(len(self.original_grades)):
            new_grade = self.original_grades[i] + bonus
            if new_grade > 100:
                new_grade = 100
            self.corrected_grades[i] = new_grade

        self.update_table()

    def update_file(self):

        with open(self.selected_file, "r") as f:
            header = f.readline()

        with open(self.selected_file, "w") as f:
            if header:
                f.write(header if header.endswith("\n") else header + "\n")
            for i in range(len(self.student_ids)):
                f.write(f"{self.student_ids[i]},{self.corrected_grades[i]}\n")

        if sys.platform == "win32":
            os.startfile(self.selected_file)
        elif sys.platform == "darwin":
            subprocess.run(["open", self.selected_file])
        else:
            subprocess.run(["xdg-open", self.selected_file])


if __name__ == "__main__":
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())

    window = Grades()
    window.show()
    sys.exit(app.exec())
