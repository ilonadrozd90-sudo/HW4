from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSpinBox, QTableWidget
import sys
import os

class Grades(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("mainWindow")
        self.setWindowTitle("Grades Correction System")
        self.setGeometry(200,200,500,400)

        self.face()

    def face(self):
        self.load = QPushButton("Load your file:", self)
        self.load.setGeometry(20, 20, 160, 38)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())

    window = Grades()
    window.show()
    sys.exit(app.exec())
