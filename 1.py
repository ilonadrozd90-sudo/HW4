from PySide6.QWidgets import QApplication, QWidget, QPushButton, QLabel, QSpinBox
import sys
import os

class Grades(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("mainWindow")
        self.setWindowTitle("Grades Correction System")
        self.setFixedSize(500, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())

    window = Grades()
    window.show()
    sys.exit(app.exec())
