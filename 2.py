from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys
import os
from About import About
import matplotlib.pyplot as plt
from file_select import FileSelect

class Icecream_App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Icecream truck")
        self.setGeometry(200,200,470,170)

        self.temperatures = []
        self.revenues = []
        self.selected_file = ''
    
        self.interface()

    def interface(self):

        self.load = QPushButton("Load your file:", self)
        self.load.setGeometry(20, 20, 160, 30)
        self.load.clicked.connect(self.load_file)

        self.about = QPushButton("About", self)
        self.about.setGeometry(270, 20, 160, 30)
        self.about.clicked.connect(self.show_about)

        self.graph = QPushButton("Show graph", self)
        self.graph.setGeometry(150, 80, 160, 35)
        self.graph.clicked.connect(self.plot_temp_graph)

    def show_about(self):
        self.about_window = About()
        self.about_window.show()

    def load_file(self):
            self.file_window = FileSelect(self)
            self.file_window.show()

    def read(self):
        self.temperatures = []
        self.revenues = []
    
        with open(self.selected_file, "r") as f:
                lines = f.readlines()
    
        for line in lines[1:]:
            parts = line.strip().split(",")
            if len(parts) >= 2:
                self.temperatures.append(float(parts[0].strip()))
                self.revenues.append(float(parts[1].strip()))

            self.plot_temp_graph()

    def plot_temp_graph(self):

        x = [10, 15, 20, 25, 30]
        y = [100, 180, 250, 340, 420]

        plt.figure()
        plt.plot(x, y, marker="o", color="#2980b9")
        plt.title("Temporary graph")
        plt.xlabel("X Axis")
        plt.ylabel("Y Axis")
        plt.grid(True)
        plt.show()    







if __name__ == "__main__":
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())

    window = Icecream_App()
    window.show()
    sys.exit(app.exec())


