from PySide6.QtWidgets import QApplication, QWidget, QPushButton
import sys
import os
from About import About
import matplotlib.pyplot as plt
from file_select import FileSelect
import numpy as np

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
        plt.figure("Revenue vs temperature")
        plt.clf()

        if self.temperatures and self.revenues:
            plt.scatter(self.temperatures, self.revenues, s=1, color="#2980b9")

            m, b = np.polyfit(self.temperatures, self.revenues, 1)
            x_vals = np.array(self.temperatures)
            plt.plot(x_vals, m * x_vals + b, color="#e74c3c", linewidth=1.5, label=f"y = {m:.2f}x + {b:.2f}")
            plt.legend()

            plt.title("Revenue vs temperature")
            plt.xlabel("Temperature[°C]")
            plt.ylabel("Revenue[$]")
        else:
            plt.plot([10, 15, 20, 25, 30], [100, 180, 250, 340, 420], marker="o", color="#2980b9")
            plt.title("Temporary Graph")
            plt.xlabel("X Axis")
            plt.ylabel("Y Axis")

        ax = plt.gca()
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        plt.grid(True)
        plt.show(block=False)







if __name__ == "__main__":
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())

    window = Icecream_App()
    window.show()
    sys.exit(app.exec())


