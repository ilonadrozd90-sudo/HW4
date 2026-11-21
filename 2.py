from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSpinBox, QTableWidget, QTableWidgetItem
import sys
import os
from About import About
import matplotlib.pyplot as plt









if __name__ == "__main__":
    app = QApplication(sys.argv)

    qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
    if os.path.exists(qss_path):
        with open(qss_path, "r", encoding="utf-8") as style_file:
            app.setStyleSheet(style_file.read())

    window = IceCreamApp()
    window.show()
    sys.exit(app.exec())


