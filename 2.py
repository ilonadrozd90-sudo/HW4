from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSpinBox, QTableWidget, QTableWidgetItem
import sys
import os
from About import About
import matplotlib.pyplot as plt

class Icecream_App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Icecream truck")
        self.setGeometry(200,200,500,400)

        self.selected_file = ''
    
        self.interface()

    def interface(self):

        self.load = QPushButton("Load your file:", self)
        self.load.setGeometry(20, 20, 160, 30)


        self.about = QPushButton("About", self)
        self.about.setGeometry(250, 20, 160, 30)

        self.graph = QPushButton("Show graph", self)
        self.graph.setGeometry(50, 100, 160, 30)







if __name__ == "__main__":
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())

    window = Icecream_App()
    window.show()
    sys.exit(app.exec())


